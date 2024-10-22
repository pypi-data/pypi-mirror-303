import os
from pathlib import Path

from .message import KafkaMessage


class Recipe:
    LOCAL_CFG_DIR = Path.cwd().joinpath(".config")
    CONTAINER_CFG_DIR = Path("/")

    def __init__(
        self,
        name: str,
        image: str,
        configs: dict[str,str]|None = None,
        secrets: dict[str,str]|None = None,
        env: dict[str,str]|None = None,
        inputs: list[KafkaMessage]|None = None,
        outputs: list[KafkaMessage]|None = None,
        depends_on: dict[str,dict[str,str]]|None = None,
        also_add: dict|None = None,
        **kwargs
    ):
        if configs is None:
            configs = {}
        if secrets is None:
            secrets = {}
        if env is None:
            env = {}
        if inputs is None:
            inputs = []
        if outputs is None:
            outputs = []
        if depends_on is None:
            depends_on = {}
        if also_add is None:
            also_add = {}
        if "consume" not in depends_on:
            depends_on["consume"] = {
                "condition": "service_healthy"
            }

        self._name = name
        self._image = image
        self._configs = configs
        self._secrets = secrets
        self._env = env
        self._inputs = inputs
        self._outputs = outputs
        self._depends_on = depends_on
        self._also_add = also_add
        self._kwargs = kwargs

    def name(self) -> str:
        return self._name

    def inputs(self) -> list[KafkaMessage]:
        return self._inputs

    def outputs(self) -> list[KafkaMessage]:
        return self._outputs

    def also_add(self) -> dict:
        return self._also_add

    def to_dict(self) -> dict:
        cfg_dir = self.LOCAL_CFG_DIR.joinpath(self._name)
        for mountpoint, content in self._configs.items():
            path = cfg_dir.joinpath(mountpoint)
            if not path.parent.is_dir():
                path.parent.mkdir(parents = True)
            path.write_text(content)

        return {
            "image": self._image,
            "container_name": self._name,
            "environment": [
                f"{key}={val}"
                for key, val in self._env.items()
            ],
            "secrets": [
                {"source": secret_name, "target": str(Path("/").joinpath(mountpoint))}
                for mountpoint, secret_name in self._secrets.items()
            ],
            "volumes": [
                ":".join([
                    "${PWD}/" + str(cfg_dir.joinpath(mountpoint).relative_to(Path.cwd())),
                    str(self.CONTAINER_CFG_DIR.joinpath(mountpoint))
                ])
                for mountpoint in self._configs.keys()
            ],
            "depends_on": self._depends_on,
            **self._kwargs
        }
