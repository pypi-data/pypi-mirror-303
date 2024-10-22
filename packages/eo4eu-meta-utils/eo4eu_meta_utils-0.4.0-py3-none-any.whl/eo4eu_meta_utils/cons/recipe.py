from typing import Optional, List, Dict
from pydantic import BaseModel
from pathlib import Path
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .builder import ImageBuilder
from .logs import logger



class RegistryConfigV1(BaseModel):
    reg: str
    url: str


class FilterConfigV1(BaseModel):
    tag:        Optional[List[str]] = None
    registry:   Optional[List[str]] = None
    dockerfile: Optional[List[str]] = None


class BuildConfigV1(BaseModel):
    tag:        Optional[str] = "latest"
    registry:   str
    dockerfile: Optional[str] = "Dockerfile"


class BuilderConfigV1(BaseModel):
    project_root: str
    version_file: str
    filters:      Optional[dict[str,FilterConfigV1]] = None
    registries:   Dict[str,RegistryConfigV1]
    builds:       List[BuildConfigV1]


def get_builder_config(version: str, input: dict) -> BuilderConfigV1:
    if version == "1":
        result = BuilderConfigV1.model_validate(input)
        if result.filters is None:
            result.filters = {}
        if "_default" not in result.filters:
            result.filters["_default"] = FilterConfigV1()
        return result
    else:
        logger.warning(f"Invalid version \"{version}\" of config file. Defaulting to \"1\"")
        return get_builder_config("1", input)

def parse_recipe_file(filename: str) -> dict[str,ImageBuilder]:
    filter_names = ["_default"]
    if ":" in filename:
        filename, filter_str = filename.split(":")
        filter_names = [filter_str]
        if "," in filter_str:
            filter_names = filter_str.split(",")

    logger.debug(f"Reading recipe file {filename} with filters {filter_names} enabled")
    try:
        data = yaml.load(Path(filename).read_text(), Loader = Loader)
    except Exception as e:
        logger.error(f"Failed to parse recipe file {filename}")
        raise e

    version = "1"
    if "version" in data:
        version = data["version"]
        del data["version"]
    else:
        logger.info(f"Version not specified, defaulting to \"1\"")

    result = {}
    for key, config_dict in data.items():
        try:
            config = get_builder_config(version, config_dict)
            local_filter_names = [
                filter_name for filter_name in filter_names
                if filter_name in config.filters
            ]
            if len(local_filter_names) == 0:
                local_filter_names = ["_default"]

            logger.debug(f"Parsing config for {key} with filters {local_filter_names}")
            builder = ImageBuilder.from_config_v1(config)
            for filter_name in local_filter_names:
                builder = builder.filter(config.filters[filter_name].model_dump())

            result[key] = builder
        except Exception as e:
            logger.error(f"Failed to configure builder {key}: {e}")
            continue

    return result
