from .infoclass import InfoClass


class FanInfo(InfoClass):
    '''
    Fan Info Class
    '''
    def __init__(self) -> None:
        self.temperature: str = "0.0"
        self.fan_off: int = -1
        self.fan_on: int = -1

    def __repr__(self) -> str:
        return f"{{'current':{self.temperature},'on':{self.fan_on},'off':{self.fan_off}}}"
