from .tools import gethostname
from .logger import infolog


class InfoClass:
    def update(self, key: str, value, prefix: str) -> None:
        key = key.lower()
        key.startswith(prefix)
        if key.startswith(prefix) is False:
            return False

        key = key[len(prefix):]

        if len(value) > 2:
            if value[0] == "\"" and value[-1] == "\"":
                value = value[1:-1]

        if hasattr(self, key):
            cur = getattr(self, key)
            if type(cur) is int:
                setattr(self, key, int(value))
            elif type(cur) is bool:
                if value == 0 or str(value).lower()[0] == "f" or str(value).lower()[0] == "n":
                    setattr(self, key, False)
                else:
                    setattr(self, key, True)
            else:
                setattr(self, key, value)

        return True
    
    def amend_hostnames(self):
        hostname = gethostname()
        self.__class__
        for key in self.__dict__.keys():
            value = getattr(self, key)
            if isinstance(value, str) and "{{hostname}}" in value:
                newvalue = value.replace("{{hostname}}", hostname)
                infolog(f"Updating Hostname in {self.__class__.__name__}.{key} from '{value}' to '{newvalue}'")

                setattr(self, key, newvalue)
