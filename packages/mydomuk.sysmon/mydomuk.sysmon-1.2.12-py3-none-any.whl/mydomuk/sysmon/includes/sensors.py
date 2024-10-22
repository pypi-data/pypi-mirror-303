from .sensor_stats import SensorStats
from .constants import *
from .tools import get_timestamp

class Sensor:
    def __init__(
            self,
            id: str = None,
            name: str = None,
            value_function: callable= None,
            fn_parms = None,
            device_class: str = None,
            unit: str = None,
            measurement: bool = False,
            non_windows_only: bool = False,
            windows_only: bool = False,
            sendsolo: bool = False,
            isavailability: bool = False,
            always_available: bool = False,
            retain: bool = False,
            isnic: bool = False,
            isvip: bool = False

        ) -> None:
        if name is None:
            raise ValueError("Name required for Sensor definition")
        if value_function is None:
            raise ValueError(f"Sensor : {name} missing value_function and required")
        if id is None:
            id = name.lower().replace(" ", "_")
        self.id: str = id
        self.name: str = name
        self.value_function: callable = value_function
        self.fn_parms = fn_parms
        self.device_class: str = device_class
        self.unit: str = unit                           ### Unit of measurement
        self.state_class: str = None
        if measurement:
            self.state_class = "measurement"
        self.non_windows_only: bool = non_windows_only
        self.windows_only: bool = windows_only
        self.sendsolo: bool = sendsolo
        self.isavailability: bool = isavailability
        self.always_available: bool = always_available
        self.isnic: bool = isnic
        self.isvip: bool = isvip
        self.retain: bool = retain


SENSORS = [
    Sensor(name="Status", sendsolo = True, always_available = True, isavailability = True,
           value_function=lambda : "online"),
    Sensor(name="Sysmon Version", 
           value_function=lambda : SYSMON_VERSION),
    Sensor(name="CPU", unit="%", measurement=True,
            value_function=lambda : round(SensorStats.cpu_utilisation, 2)),
    Sensor(name="CPU Count",
           value_function=lambda :  SensorStats.cpu_count),
    Sensor(name="CPU Frequency", measurement=True,
           value_function=lambda : round(SensorStats.cpu_freq, 2)),
    Sensor(name="CPU Average Load Over 1 minute", id="cpu_average_1min", unit="%", measurement=True,
           value_function=lambda : round(SensorStats.cpu_load_average_1min, 2)),
    Sensor(name="CPU Average Load Over 5 minutes", id="cpu_average_5min", unit="%", measurement=True,
           value_function=lambda : round(SensorStats.cpu_load_average_5min, 2)),
    Sensor(name="CPU Average Load Over 15 minutes", id="cpu_average_15min", unit="%", measurement=True,
           value_function=lambda : round(SensorStats.cpu_load_average_15min, 2)),
    Sensor(name="Memory Used", id="memory_used_percent", unit="%", measurement=True,
           value_function=lambda : round(SensorStats.memory_utilisation, 2)),
    Sensor(name="Memory Used Bytes", measurement=True,
           value_function=lambda : SensorStats.memory_bytes_used),
    Sensor(name="Memory Free Bytes", measurement=True,
           value_function=lambda : SensorStats.memory_bytes_total - SensorStats.memory_bytes_used),
    Sensor(name="Memory Total Bytes", measurement=True,
           value_function=lambda : SensorStats.memory_bytes_total),
    Sensor(name="PID Count", measurement=True,
           value_function=lambda : SensorStats.pid_count),
    Sensor(name="RootFS Usage", unit="%", measurement=True,
           value_function=lambda : SensorStats.root_fs_usage),
    Sensor(name="Temperature", unit=DEGREE_SIGN, measurement=True, non_windows_only=True,
           value_function=lambda : round(SensorStats.temperature, 2)),
    Sensor(name="Network Bytes Sent", measurement=True,
           value_function=lambda : SensorStats.network_bytes_sent),
    Sensor(name="Network Bytes Received", measurement=True,
           value_function=lambda : SensorStats.network_bytes_recv),
    Sensor(name="Network Input Errors", id="network_errors_in", measurement=True,
           value_function=lambda : SensorStats.network_errors_in),
    Sensor(name="Network Output Errors", id="network_errors_out", measurement=True,
           value_function=lambda : SensorStats.network_errors_out),
    Sensor(name="Network Input Drops", id="network_drops_in", measurement=True,
           value_function=lambda : SensorStats.network_drops_in),
    Sensor(name="Network Output Drops", id="network_drops_out", measurement=True,
           value_function=lambda : SensorStats.network_drops_out),
    Sensor(name="Network Total Input Errors", id="network_total_errors_in", measurement=True,
           value_function=lambda : SensorStats.network_total_errors_in),
    Sensor(name="Network Total Output Errors", id="network_total_errors_out", measurement=True,
           value_function=lambda : SensorStats.network_total_errors_out),
    Sensor(name="Network Total Input Drops", id="network_total_drops_in", measurement=True,
           value_function=lambda : SensorStats.network_total_drops_in),
    Sensor(name="Network Total Output Drops", id="network_total_drops_out", measurement=True,
           value_function=lambda : SensorStats.network_total_drops_out),
    Sensor(name="OS Name", 
           value_function=lambda : SensorStats.os_name),
    Sensor(name="OS Release",
           value_function=lambda : SensorStats.os_release),
    Sensor(name="OS Version",
           value_function=lambda : SensorStats.os_version),
    Sensor(name="OS Architecture",
           value_function=lambda : SensorStats.os_architecture),
    Sensor(name="Last Boot", id="lastboottime", device_class="timestamp",
           value_function=lambda : SensorStats.boot_time),
    Sensor(name="Last Update", id="lastupdate", device_class="timestamp", always_available= True,
           value_function=get_timestamp)
]


