from .ha_sensor import HomeAssistantSensor

class HomeAssistantDevice:
    '''
    Home Assistant Device Information for this instance of Sysmon

    Sensors are subordinate to this device
    '''
    def __init__(self, name: str, uid: str) -> None:
        self.uid: str = uid
        self.name: str = name
        self.manufacturer: str = None
        self.model: str = None

    def json(self) -> dict:
        obj: dict = {"name": self.name, "identifiers": self.uid}
        if self.manufacturer:
            obj["manufacturer"] = self.manufacturer
        if self.model:
            obj["model"] = self.model
        return obj
    
    # def makesensor(
    #         self,
    #         sensorname: str,
    #         sensor_uidsuffix: str,
    #         unit_of_measurement: str = None
    #         ) -> "HomeAssistantSensor":
    #     sensor = HomeAssistantSensor(
    #                 sensorname,
    #                 sensor_uidsuffix,
    #                 self, unit_of_measurement)
    #     return sensor
