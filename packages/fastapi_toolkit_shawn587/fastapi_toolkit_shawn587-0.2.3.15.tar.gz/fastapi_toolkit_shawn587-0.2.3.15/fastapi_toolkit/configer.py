from typing import Union, Any
from pathlib import Path

import yaml


class Configer:
    def __init__(self, config: Union[Path, str] = Path('fastapi_toolkit.yaml')):
        if isinstance(config, str):
            path = Path(config)
        else:
            path = config
        if path.is_file():
            self.config = yaml.load(path.read_text(), Loader=yaml.FullLoader)
        else:
            self.config = {}

    def __getitem__(self, key: str) -> Union[Any, None]:
        v = self.config
        for i in key.split('.'):
            if v is None:
                return None
            if isinstance(v, list):
                i = int(i)
                if i >= len(v):
                    return None
                v = v[i] or None
            elif isinstance(v, dict):
                v = v.get(i, None)
            else:
                return None
        return v

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError
