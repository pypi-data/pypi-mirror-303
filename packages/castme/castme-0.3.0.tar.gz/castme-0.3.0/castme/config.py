import os.path
import tomllib
from dataclasses import dataclass
from pathlib import PurePath
from typing import Optional

from castme.messages import debug


class ConfigNotFoundException(Exception):
    pass


@dataclass
class Config:
    user: str
    password: str
    subsonic_server: str
    chromecast_friendly_name: str
    default_backend: str

    @classmethod
    def load(cls, file_path: Optional[PurePath | str] = None) -> "Config":
        def _load(path: PurePath | str) -> "Config":
            debug("config", f"Loading config from {path}")
            with open(path, "rb") as fd:
                data = tomllib.load(fd)
            return cls(**data)

        if file_path:
            return _load(file_path)

        for f in [
            "castme.toml",
            os.path.expanduser("~/.config/castme.toml"),
            "/etc/castme.toml",
        ]:
            if os.path.isfile(f):
                return _load(f)

        raise ConfigNotFoundException()
