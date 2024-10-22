from .tools import gethostname
from typing import TYPE_CHECKING, Callable
import psutil
from datetime import datetime, timezone
from .logger import infolog, debuglog, errorlog
from .constants import *
from socket import AddressFamily
import paho.mqtt.client as mqtt
from .sensor_stats import SensorStats
from .sensors import Sensor

if TYPE_CHECKING:
    from .ha_device import HomeAssistantDevice


class HomeAssistantSensor:
    '''
    Home Assistant Sensor Class

    A HA Sensor relates to an HA Entity subordinate to an HA Device

    '''
    def __init__(
            self,
            sensor: Sensor,
            device: "HomeAssistantDevice") -> None:
        self.name: str = sensor.name
        self.state_topic: str = None
        self.device_class: str = sensor.device_class
        self.state_class: str = sensor.state_class
        self.value_template: str = None
        self.uid_suffix: str = None
        self._uidsuffix: str = sensor.id
        self.unique_id: str = None
        self.availability_topic: str = None
        self.device: HomeAssistantDevice = device
        self.unit_of_measurement: str = sensor.unit
        self.retain: bool = sensor.retain
        self.value_function: callable = sensor.value_function
        self.value = None
        self.fn_parms: any  = sensor.fn_parms
        self.isvip: bool = sensor.isvip
        self.isavailability: bool = sensor.isavailability
        self.sendsolo: bool = sensor.sendsolo
        self.windows_only: bool = sensor.windows_only
        self.non_windows_only: bool = sensor.non_windows_only

        self.update_suffix(sensor.id)
        # if sensor.isnic:
        #     self.value_function = self.get_nic_addr
        # elif sensor.isvip:
        #     self.value_function = self.get_vip_addr
        #     self.retain = True
        

    @classmethod
    def firstrun(cls):
        SensorStats.get_stats()

    def update_suffix(self, uidsuffix):
        self.uid_suffix = uidsuffix
        self.unique_id = self.device.uid + "_" + uidsuffix

    def discovery_data(self) -> dict:
        obj = {"name": self.name,
               "state_topic": self.state_topic,
               "unique_id": self.unique_id,
               "object_id": self.unique_id,
               "device": self.device.json()
              }
        if self.device_class is not None:
            obj["device_class"] = self.device_class
        if self.value_template is not None:
            obj['value_template'] = self.value_template
        if self.sendsolo is False:
            obj['value_template'] = "{{ value_json['" + self.uid_suffix + "'] }}"
        if self.availability_topic is not None:
            obj["payload_available"] = "online"
            obj["payload_not_available"] = "offline"
            obj['availability_topic'] = self.availability_topic
        if self.unit_of_measurement is not None:
            obj['unit_of_measurement'] = self.unit_of_measurement
        if self.state_class is not None:
            obj['state_class'] = self.state_class
        return obj

    def get_value(self):
        if self.fn_parms is None:
            return self.value_function()
        else:
            return self.value_function(self.fn_parms)

    # def get_value_function(self):
    #     functions = {
    #         SENSOR_UID_STATUS: lambda : "online",
    #         SENSOR_UID_CPU: lambda : round(SensorStats.cpu_utilisation, 2),
    #         SENSOR_UID_CPU_AVG_1M: lambda : round(SensorStats.cpu_load_average_1min, 2),
    #         SENSOR_UID_CPU_AVG_5M: lambda : round(SensorStats.cpu_load_average_5min, 2),
    #         SENSOR_UID_CPU_AVG_15M: lambda : round(SensorStats.cpu_load_average_15min, 2),
    #         SENSOR_UID_CPU_COUNT: lambda : SensorStats.cpu_count,
    #         SENSOR_UID_CPU_FREQ: lambda : round(SensorStats.cpu_freq, 2),
    #         SENSOR_UID_MEMORY_USED: lambda : round(SensorStats.memory_utilisation, 2),
    #         SENSOR_UID_MEMORY_BYTES_USED: lambda : SensorStats.memory_bytes_used,
    #         SENSOR_UID_MEMORY_BYTES_FREE: lambda : SensorStats.memory_bytes_total - SensorStats.memory_bytes_used,
    #         SENSOR_UID_MEMORY_BYTES_TOTAL: lambda : SensorStats.memory_bytes_total,
    #         SENSOR_UID_PID_COUNT: lambda : SensorStats.pid_count,
    #         SENSOR_UID_ROOTFS: self.get_root_usage,
    #         SENSOR_UID_TEMPERATURE: lambda : round(SensorStats.temperature, 2),
    #         SENSOR_UID_LASTBOOTTIME: lambda : SensorStats.boot_time,
    #         SENSOR_UID_LASTUPDATE: self.get_timestamp,
    #         SENSOR_UID_NET_BYTES_RECV: lambda : SensorStats.network_bytes_recv,
    #         SENSOR_UID_NET_BYTES_SENT: lambda : SensorStats.network_bytes_sent,
    #         SENSOR_UID_NET_ERRORS_IN: lambda : SensorStats.network_errors_in,
    #         SENSOR_UID_NET_ERRORS_OUT: lambda : SensorStats.network_errors_out,
    #         SENSOR_UID_NET_DROPS_IN: lambda : SensorStats.network_drops_in,
    #         SENSOR_UID_NET_DROPS_OUT: lambda : SensorStats.network_drops_out,
    #         SENSOR_UID_NET_TOTAL_ERRORS_IN: lambda : SensorStats.network_total_errors_in,
    #         SENSOR_UID_NET_TOTAL_ERRORS_OUT: lambda : SensorStats.network_total_errors_out,
    #         SENSOR_UID_NET_TOTAL_DROPS_IN: lambda : SensorStats.network_total_drops_in,
    #         SENSOR_UID_NET_TOTAL_DROPS_OUT: lambda : SensorStats.network_total_errors_out,
    #         SENSOR_UID_OS_NAME: lambda : SensorStats.os_name,
    #         SENSOR_UID_OS_RELEASE: lambda : SensorStats.os_release,
    #         SENSOR_UID_OS_VERSION: lambda : SensorStats.os_version,
    #         SENSOR_UID_OS_ARCH: lambda : SensorStats.os_architecture,
    #         SENSOR_UID_NIC: self.get_nic_addr,
    #         SENSOR_UID_VIP: self.get_vip_addr,
    #         SENSOR_UID_SYSMON_VERSION: lambda : SYSMON_VERSION
    #     }
    #     if self._uidsuffix in functions:
    #         return functions[self._uidsuffix]
    #     raise ValueError(f"Uncaught UID Suffix : {self._uidsuffix}")



    def get_vip_addr(self):
        vipaddr = self.get_nic_addr()
        if vipaddr is None:
            return None
        return gethostname()

    def get_nic_addr(self):
        if self.fn_parms is None:
            raise ValueError(f"Error : {self.uid_suffix} is missing fn_parms")
        nics = psutil.net_if_addrs()
        if self.fn_parms not in nics:
            return None
        
        nic = nics[self.fn_parms]
        for family, address, netmask, broadcast, ptp in nic:
            if family == AddressFamily.AF_INET:
                return address
        return None
