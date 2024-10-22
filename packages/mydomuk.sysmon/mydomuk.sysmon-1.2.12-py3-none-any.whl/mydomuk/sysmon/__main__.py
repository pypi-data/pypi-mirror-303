#!/usr/bin/env python3
'''
SysMon Module
'''
from datetime import datetime
import argparse
from os import name as os_name, path as os_path
from sys import platform as sys_platform
import time
import atexit
# import aaa.xxx.constants as const
# import sysmon.constants as const
from .includes.logger import initlog, infolog, errorlog, debuglog, LOGLEVEL
from .includes.ha_sensor import HomeAssistantSensor
from .includes.mqttinfo import MQTTInfo
from .includes.faninfo import FanInfo
from .includes.ha_info import HomeAssistantInfo
from .includes.ha_device import HomeAssistantDevice
from .includes.ha_info import HomeAssistantInfo
from .includes.tools import gethostname, get_timestamp
from .includes.constants import *
import json
from importlib import resources

initlog()

def exit_handler(mqtti: MQTTInfo, sensor: "HomeAssistantSensor"):
    infolog("Cleaning Up and Closing")
    if mqtti.connected:
        mqtti.send_mqtt(sensor.state_topic, "offline", True, timeout=5)



def load_source(filename:str):
    '''
    Load a Source File for Configuration Variables
    '''
    mqtti = MQTTInfo()
    fan = FanInfo()
    hass = HomeAssistantInfo()
    if os_path.exists(filename):
        with open(filename, "rt", encoding="UTF-8") as file_no:
            lines = file_no.readlines()
            for line in lines:
                line = line.strip()
                if len(line) <= 0:
                    continue
                if line[0] == "#":
                    continue
                if " #"  in line:
                    idx = line.index(" #")
                    line = line[:idx].rstrip()
                elements = line.split("=",1)
                if len(elements) != 2:
                    continue
                name, value = elements
                if mqtti.update(name, value, "mqtt_") is True:
                    continue
                if fan.update(name, value, "fan_") is True:
                    continue
                if hass.update(name, value, "hass_") is True:
                    continue
    return mqtti, fan, hass


def print_example_source_file():
    print("# Configuration File save this as a .src file and edit it")
    print("# ************** START ********************")
    try:
        import mydomuk.sysmon.resources as mydomresources
        print(resources.files(mydomresources).joinpath("example.src").read_text(encoding="UTF-8"))
    except ImportError:
        curpath = os_path.dirname(__file__)
        example = os_path.join(curpath, "resources", "example.src")
        with open(example, encoding="UTF-8", mode="rt") as ef:
            print(ef.read())
    print("# ************** ENDS  ********************")


def send_bulk(mqtti: MQTTInfo, printresults: bool):
    sendqueue: list[tuple] = []
    blob = {}
    bulktopic: str = mqtti.make_bulk_topic()
    for sensor in mqtti.sensors():
        if sensor is None:
            continue
        message = sensor.get_value()
        if message is None and sensor.isvip:
            break
        if printresults:
            infolog(f"{sensor.name:16s} : {message}")
        if sensor.sendsolo:
            sendqueue.append((sensor.state_topic, message))
        else:
            blob[sensor.uid_suffix] = message

    blobdata = json.dumps(blob)
    sendqueue.append((bulktopic, blobdata))
    for topic, data in sendqueue:
        mqtti.send_mqtt(topic, data)


def main():
    '''
    Main Loop
    '''

    sensor_status: HomeAssistantSensor = None
    sensor_cpu: HomeAssistantSensor = None
    sensor_mem: HomeAssistantSensor = None
    sensor_temperature: HomeAssistantSensor = None
    sensor_lastupdate: HomeAssistantSensor = None



    parser = argparse.ArgumentParser(prog="sysmon")
    parser.add_argument("-src",dest="source", help="Source Configuration File")
    parser.add_argument("-host", dest="host", help="MQTT Host")
    parser.add_argument("-port", dest="port", type=int, help="MQTT port")
    parser.add_argument("-user", dest="user", help="MQTT User")
    parser.add_argument("-pass", dest="password", help="MQTT password")
    parser.add_argument("-cs", dest="createsource", action="store_true", help="Create empty source configuration")
    parser.add_argument("-d", dest="debug", action="store_true", help="Enable debugging")
    parser.add_argument("-v", dest="verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("-rd", dest="reset_discovery", action="store_true", help="Reset discovery information")
    parser.add_argument("-s",dest="sleep", type=float, default=60, help="Seconds to sleep between loops")
    parser.add_argument("-l",dest="loop", type=int, default=1, help="Number of loops to do, 0 is infinite")
    parser.add_argument("-pi",dest="raspberrypi", action="store_true", default=False, help="Redundant raspberry pi flag")
    parser.add_argument("-pr", dest="printresults", action="store_true", default=False, help="Print results")
    parser.add_argument("-f1", dest="fanon", type=int,
                        help="Temperature to turn fan on at")
    parser.add_argument("-f0", dest="fanoff", type=int,
                        help="Temperature to turn fan off at")

    parser.add_argument("-pt", dest="printtime", action="store_true", default=False, help="Print timestamp")
    args = parser.parse_args()

    infolog(f"Sysmon Version {SYSMON_VERSION} running on {os_name} system {sys_platform}")

    if args.verbose:
        infolog("Changing LogLevel to Verbose")
        initlog(LOGLEVEL.LEVEL_VERBOSE)
    elif args.debug:
        infolog("Changing Loglevel to Debug")
        initlog(LOGLEVEL.LEVEL_DEBUG)



    loopcount = args.loop
    if loopcount == 0:
        infinite = 1
        loopcount = 1
    else:
        infinite = 0

    sleeptime = args.sleep

    if args.createsource:
        print_example_source_file()
        exit(0)

    if args.source:
        mqtti, fan, hass = load_source(args.source)
    else:
        mqtti = MQTTInfo()
        fan = FanInfo()
        hass = HomeAssistantInfo()

    if args.host:
        mqtti.broker = args.host
    if args.port:
        mqtti.port = args.port
    if args.user:
        mqtti.user = args.user
    if args.password:
        mqtti.password = args.password
    if args.fanon:
        fan.fan_on = args.fanon
    if args.fanoff:
        fan.fan_off = args.fanoff

    hass.reset_discovery = args.reset_discovery

    mqtti.validate()
    hass.validate()

    if mqtti.broker:
        mqtti.initialise(hass)
        mqtti.make_sensors()
        sensor_status = mqtti.get_state_sensor()

        if mqtti.connected is False:
            mqtti.connect_broker(sensor_status.state_topic, "offline")

        atexit.register(exit_handler, mqtti, sensor_status)

    if loopcount > 0:
        infolog("Starting Monitor Loop")

    interval_start = datetime.now()
    send_discoveries: bool = False
    while loopcount > 0:
        loopcount = loopcount - 1 + infinite
        interval_offset = datetime.now()
        interval_diff = interval_offset - interval_start
        if interval_diff.total_seconds() >= RUN_LOOP_HOUR:                   
            infolog("Run loop still working")
            interval_start = interval_offset
            if mqtti.protocol_version_5:
                send_discoveries = True
        debuglog(f"Performing Run Loop")

        if mqtti.broker:
            if mqtti.connected is False:
                mqtti.connect_broker(sensor_status.state_topic, "offline")

            if mqtti.connected:
                if send_discoveries:
                    mqtti.send_ha_discovery(quiet=True)
                    send_discoveries = False
                HomeAssistantSensor.firstrun()
                t = "Time"
                if args.printresults or args.printtime:
                    infolog(f"{t:16s} : {get_timestamp()}")
                # send_data(mqtti, args.printresults)
                send_bulk(mqtti, args.printresults)
                if args.printresults:
                    infolog("*"*48)
        if loopcount > 0:
            if sleeptime > 0:
                time.sleep(sleeptime)

    infolog("Monitor Loop Exited")
    if mqtti.connected:
        if sensor_status is not None:
            mqtti.send_mqtt(sensor_status.state_topic, "offline")
        mqtti.disconnect()

if __name__ == "__main__":
  main()
