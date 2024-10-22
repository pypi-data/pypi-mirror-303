from .infoclass import InfoClass
from .logger import infolog, errorlog, isDebug, debuglog
import json
from typing import TYPE_CHECKING
from .constants import MQTT_MESSAGE_EXPIRY_SECONDS
if TYPE_CHECKING:
    from .mqttinfo import MQTTInfo


class HomeAssistantInfo(InfoClass):
    '''
    Home Assistant Information Class

    This class holds the user supplied information for communication with HomeAssistant
    '''
    def __init__(self) -> None:
        self.discovery: bool = False
        self.topic_prefix: str = "homeassistant"
        self.manufacturer: str = None
        self.model: str = None
        self.device: str = None
        self.deviceid: str = None
        self.reset_discovery: bool = False

    def validate(self):
        self.amend_hostnames()
        if self.device is None:
            raise ValueError("Missing HASS_DEVICE - Device description required")
        if self.deviceid is None:
            raise ValueError("Missing HASS_DEVICEID - Unique device ID required")

    def send_discoveries(self,
                       mqtti: "MQTTInfo",
                       prefix: str,
                       quiet: bool):
        infolog(f"Sending HA Discoveries for Device : {self.device}")
        for sensor in mqtti.sensors():
            discovery_topic = f"{self.topic_prefix}/sensor/{prefix}/{sensor.unique_id}/config"
            if self.reset_discovery:
                # Reset the Discovery First, Just in case!
                if isDebug():
                    debuglog(f"Resetting HA Discovery for Sensor : {sensor.name} - {discovery_topic}")
                else:
                    if quiet is False:
                        infolog(f"Resetting HA Discovery for Sensor : {sensor.name}")
                mqtti.send_mqtt(discovery_topic, None, False, True)

            if isDebug():
                debuglog(
                    f"Sending HA Discovery for Sensor : {sensor.name} - {discovery_topic}")
            else:
                if quiet is False:
                    infolog(
                        f"Sending HA Discovery for Sensor : {sensor.name}")
            retained_expiry_seconds: int = 0 if sensor.isavailability else MQTT_MESSAGE_EXPIRY_SECONDS
            mqtti.send_mqtt(discovery_topic, json.dumps(sensor.discovery_data()), True, True, retained_expiry_seconds=retained_expiry_seconds)

        # Only do the reset once!
        self.reset_discovery = False
