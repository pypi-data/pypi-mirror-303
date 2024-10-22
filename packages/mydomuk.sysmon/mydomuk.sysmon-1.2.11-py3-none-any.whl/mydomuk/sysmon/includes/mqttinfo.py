from .infoclass import InfoClass
from .tools import gethostname, isWindows
import paho.mqtt.client as mqtt
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.enums import CallbackAPIVersion, MQTTProtocolVersion

from .logger import infolog, errorlog, debuglog, verboselog
from .ha_sensor import HomeAssistantSensor
from .sensor_stats import SensorStats
from .ha_device import HomeAssistantDevice
from .ha_info import HomeAssistantInfo
from .constants import *
from .sensors import Sensor, SENSORS


class MQTTInfo(InfoClass):
    '''
    MQTT Info Class
    '''
    def __init__(self) -> None:
        self.broker: str = None
        self.port: int = 1883
        self.user: str = None
        self.password: str = None
        self.ssl: bool = False
        self.cacert: str = None
        self.insecure: bool = False
        self.topic_prefix: str = "MyDomUK"
        self.device_topic: str = "sysmon/{{hostname}}"
        self.protocol_version_5: bool = True
        self.vip_device: str = None
        self.vip_topic: str = None
        self.vip_monit: str = None
        self.nic_monit: str = None
        self.connected: bool = False
        self.client: mqtt.Client = None
        self._device: HomeAssistantDevice = None
        self._vipdevice: HomeAssistantDevice = None
        self._sensors: list[HomeAssistantSensor] = []
        self._hass: HomeAssistantInfo = None
        self._state_sensor: HomeAssistantSensor = None

    def initialise(self, hass: HomeAssistantInfo):
        self._hass = hass
        devicename = hass.device
        deviceid = hass.deviceid
        self._device = HomeAssistantDevice(devicename, deviceid)
        self._device.manufacturer = hass.manufacturer
        self._device.model = hass.model

        if self.vip_device:
            self._vipdevice = HomeAssistantDevice(
                "Virtual IP", deviceid.replace(gethostname(), self.vip_device))
            self._vipdevice.manufacturer = "Virtual"
            self._vipdevice.model = "VRRP"

    def get_state_sensor(self):
        return self._state_sensor

    def make_ha_sensor(self, sensor: Sensor) -> HomeAssistantSensor:
        ha_sensor = HomeAssistantSensor(sensor, self._device)
        self._sensors.append(ha_sensor)
        return ha_sensor

    def make_sensors(self):
        windows: bool = isWindows()
        # sensor: HomeAssistantSensor = None
        state_sensor: HomeAssistantSensor = None
        for sensor in SENSORS:
            ha_sensor = self.make_ha_sensor(sensor)
            if ha_sensor.isavailability:
                state_sensor = ha_sensor
                self._state_sensor = ha_sensor

        # self._sensor_status = self.make_sensor(SENSOR_NAME_STATUS, SENSOR_UID_STATUS)
        # self.make_sensor(
        #     SENSOR_NAME_SYSMON_VERSION, SENSOR_UID_SYSMON_VERSION)
        # self.make_sensor(SENSOR_NAME_CPU, SENSOR_UID_CPU, "%").state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_CPU_COUNT, SENSOR_UID_CPU_COUNT)
        # if windows is False:
        #     self.make_sensor(SENSOR_NAME_CPU_FREQ, SENSOR_UID_CPU_FREQ).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_CPU_AVG_1M, SENSOR_UID_CPU_AVG_1M, "%").state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_CPU_AVG_5M, SENSOR_UID_CPU_AVG_5M, "%").state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_CPU_AVG_15M, SENSOR_UID_CPU_AVG_15M, "%").state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_MEMORY_USED, SENSOR_UID_MEMORY_USED, "%").state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_MEMORY_BYTES_USED, SENSOR_UID_MEMORY_BYTES_USED).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_MEMORY_BYTES_FREE, SENSOR_UID_MEMORY_BYTES_FREE).state_class = "measurement"

        # self.make_sensor(SENSOR_NAME_MEMORY_BYTES_TOTAL, SENSOR_UID_MEMORY_BYTES_TOTAL).state_class = "measurement"

        # self.make_sensor(SENSOR_NAME_PID_COUNT, SENSOR_UID_PID_COUNT).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_ROOTFS, SENSOR_UID_ROOTFS, "%").state_class = "measurement"
        
        # if windows is False:
        #     self.make_sensor(SENSOR_NAME_TEMPERATURE, SENSOR_UID_TEMPERATURE, DEGREE_SIGN).state_class = "measurement"

        # self.make_sensor(SENSOR_NAME_NET_BYTES_SENT, SENSOR_UID_NET_BYTES_SENT).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_BYTES_RECV, SENSOR_UID_NET_BYTES_RECV).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_ERRORS_IN, SENSOR_UID_NET_ERRORS_IN).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_ERRORS_OUT, SENSOR_UID_NET_ERRORS_OUT).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_DROPS_IN, SENSOR_UID_NET_DROPS_IN).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_DROPS_OUT, SENSOR_UID_NET_DROPS_OUT).state_class = "measurement"

        # self.make_sensor(SENSOR_NAME_NET_TOTAL_ERRORS_IN, SENSOR_UID_NET_TOTAL_ERRORS_IN).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_TOTAL_ERRORS_OUT, SENSOR_UID_NET_TOTAL_ERRORS_OUT).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_TOTAL_DROPS_IN, SENSOR_UID_NET_TOTAL_DROPS_IN).state_class = "measurement"
        # self.make_sensor(SENSOR_NAME_NET_TOTAL_DROPS_OUT, SENSOR_UID_NET_TOTAL_DROPS_OUT).state_class = "measurement"

        # self.make_sensor(SENSOR_NAME_OS_NAME, SENSOR_UID_OS_NAME)
        # self.make_sensor(SENSOR_NAME_OS_RELEASE, SENSOR_UID_OS_RELEASE)
        # self.make_sensor(SENSOR_NAME_OS_VERSION, SENSOR_UID_OS_VERSION)
        # self.make_sensor(SENSOR_NAME_OS_ARCH, SENSOR_UID_OS_ARCH)

        # self.make_sensor(
        #     SENSOR_NAME_LASTBOOTTIME, SENSOR_UID_LASTBOOTTIME, device_class="timestamp")
        # self.make_sensor(
        #     SENSOR_NAME_LASTUPDATE, SENSOR_UID_LASTUPDATE, device_class="timestamp")

        if self.nic_monit is not None:
            for nic in self.nic_monit.split(","):
                nic = nic.strip()
                sensor = Sensor(name=f"NIC {nic}", isnic=True, value_function=SensorStats.get_nic_addr, fn_parms=nic)
                self.make_ha_sensor(sensor)
                # sensor_nic = self.make_sensor(f"NIC {nic}", SENSOR_UID_NIC)
                # sensor_nic.update_suffix(SENSOR_UID_NIC + f"_{nic}")
                # sensor_nic.fn_parms = nic

        if self.vip_monit is not None:
            for vip in self.vip_monit.split(","):
                vip = vip.strip()
                sensor = Sensor(name=f"VIP {vip}", isvip=True, sendsolo=True, value_function=SensorStats.get_vip_addr, fn_parms=vip, retain=True)
                ha_sensor = self.make_ha_sensor(sensor)
                ha_sensor.state_topic = self.make_vip_topic(vip)
                # sensor_vip = self.make_sensor(f"VIP {vip}", SENSOR_UID_VIP)
                # sensor_vip.update_suffix(SENSOR_UID_VIP + f"_{vip}")
                # sensor_vip.fn_parms = vip
                # sensor_vip.state_topic = self.make_vip_topic(vip)
                # sensor_vip.isvip = True
                # sensor_vip.retain = True

        for ha_sensor in self._sensors:
            if ha_sensor.isvip is False:
                ha_sensor.state_topic = self.make_sensor_topic(ha_sensor.uid_suffix, ha_sensor.sendsolo)
            if ha_sensor.isavailability is False:
                ha_sensor.availability_topic = self.make_sensor_topic(
                    state_sensor.uid_suffix, True
                )


    def validate(self):
        self.amend_hostnames()
        if self.device_topic is None:
            raise ValueError("Missing MQTT_DEVICE_TOPIC")
        if self.topic_prefix is None:
            raise ValueError("Missing MQTT_TOPIC_PREFIX")
        if self.broker is None:
            raise ValueError("Missing MQTT_BROKER, hostname or IP address required")

    def get_topic(self, suffix: str) -> str:
        return self.topic_prefix + "/" + suffix

    def make_sensor_topic(self, sensor_suffix: str, sendsolo: bool) -> str:
        if sendsolo:
            return self.get_topic(self.device_topic + "/" + sensor_suffix)
        else:
            return self.make_bulk_topic()

    def make_bulk_topic(self):
        return self.get_topic(self.device_topic + "/" + MQTT_MULTI_TOPIC_NODE)

    def make_vip_topic(self, vip_suffix: str) -> str:
        # safevip: str = vip_suffix.replace(".","")
        return self.get_topic(self.vip_topic + "/" + vip_suffix)

    def connect_broker(
            self,
            will_topic: str = None,
            will_message: str= None) -> None:
        infolog(f"Connecting to MQTT Broker : {self.broker} with user {self.user}")
        protocol: MQTTProtocolVersion = mqtt.MQTTv5 if self.protocol_version_5 else mqtt.MQTTv311
        self.client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, protocol=protocol,
                                reconnect_on_failure=True)
        self.client.on_connect_fail = self.on_mqtt_connect_fail
        self.client.on_disconnect = self.on_mqtt_disconnect
        if self.user is not None:
            self.client.username_pw_set(self.user, self.password)
        if self.ssl:
            self.client.tls_set()
        if self.cacert is not None:
            self.client.tls_set(ca_certs=self.cacert)
            self.client.tls_insecure_set(True)
        if will_message is not None and will_topic is not None:
            self.client.will_set(will_topic, will_message, retain=True)
        try:
            ec = self.client.connect(host=self.broker, port=self.port)
            if ec == 0:
                infolog(f"MQTT Connection Established to Broker : {self.broker}")
                self.client.loop_start()
                self.connected = True
                self.send_ha_discovery(quiet=False)

            else:
                infolog(f"Broker Connect Error Code : {ec}")
                self.connected = True
        except Exception as e:
            self.connected = False
            infolog(f"Broker Connect Failed : {e}")
        return self.connected

    def sensors(self) -> "list[HomeAssistantSensor]":
        return list(self._sensors)

    def send_ha_discovery(self, quiet: bool):
        hass = self._hass
        if hass.discovery:
            hass.send_discoveries(self, self.topic_prefix, quiet=quiet)


    def on_mqtt_connect_fail(self, client: any, userdata: any, flags: any, rc: any):
        ''' On MQTT Failure '''
        self.connected = False
        errorlog(f"MQTT Connect Failed to Broker : {self.broker}")
        errorlog(f"User Data : {userdata}")
        errorlog(f"Flags : {flags}")
        errorlog(f"RC : {rc}")


    def on_mqtt_disconnect(self, client: any, userdata: any, disconnect_flags, rc: any, properties):
        self.connected = False
        infolog(f"MQTT Disconnect - {rc}")

    def send_mqtt(
            self,
            topic:str,
            message:str,
            retain: bool = False,
            isHAdiscovery: bool = False,
            retained_expiry_seconds: int = 0,
            retries: int = 3,
            timeout: int = 1) -> bool:
        ''' 
        Send an MQTT Message 
        '''
        sent: bool = False
        errprefix: str = "MQTT Send"
        props: mqtt.Properties = None
        if retain and retained_expiry_seconds > 0 and self.protocol_version_5:
            try:
                props = mqtt.Properties(PacketTypes.PUBLISH)
                props.MessageExpiryInterval=retained_expiry_seconds
            except Exception as e:
                print(f"Props Error : {e}")
        if isHAdiscovery:
            if message is None:
                errprefix = "HA Discovery Reset"
            else:
                errprefix = "HA Discovery Message"
        
        verboselog(f"Sending Topic : {topic}, Message : {message}, Retain : {retain}")
        while sent is False:                        
            response = self.client.publish(topic, message, retain=retain, properties=props)
            try:
                response.wait_for_publish(timeout)
                sent = True
            except ValueError:
                retries -= 1
                if retries > 0:
                    errorlog(f"{errprefix} for : {topic}, failed retrying")
                else:
                    errorlog(f"{errprefix} for : {topic}, failed retry limit reached")
                    break
            except RuntimeError as er:
                errorlog(f"{errprefix} for {topic}, fatal runtime error : {er}")
                break
            except Exception as e:
                errorlog(f"{errprefix} for {topic}, fatal error : {e}")
                break
        return sent

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        self.connected = False
        self.client = None
