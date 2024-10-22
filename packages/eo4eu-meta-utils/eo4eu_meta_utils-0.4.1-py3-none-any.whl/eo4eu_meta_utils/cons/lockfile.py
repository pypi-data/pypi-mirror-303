from pydantic import BaseModel
from pathlib import Path
from typing import Dict
import tomllib
import json


def read_version(version_filepath: Path) -> str:
    version_txt = version_filepath.read_text()
    if version_filepath.name == "pyproject.toml":
        data = tomllib.loads(version_txt)
        return data["project"]["version"]
    if version_filepath.suffix == ".json":
        data = json.loads(version_txt)
        return data["version"]
    else:
        return version_txt


class ImageLockInfoV1(BaseModel):
    version: str
    hash: str


class LockFileV1(BaseModel):
    version: str
    images: Dict[str,ImageLockInfoV1]
