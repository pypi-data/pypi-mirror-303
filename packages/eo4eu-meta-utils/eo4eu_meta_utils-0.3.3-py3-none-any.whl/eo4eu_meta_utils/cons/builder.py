from typing import Self
from pathlib import Path
from pprint import pformat
import subprocess
import yaml
import copy

from .logs import logger
from .lockfile import read_version


class ImageBuild:
    def __init__(
        self,
        login_cmd: list[str],
        build_cmd: list[str],
        push_cmd: list[str],
        features: dict,
        image: str
    ):
        self.login_cmd = login_cmd
        self.build_cmd = build_cmd
        self.push_cmd = push_cmd
        self.features = features
        self.image = image
        self._output = {}

    @classmethod
    def default(
        cls,
        project_root: str,
        dockerfile: str|None,
        registry_name: str,
        registry_url: str,
        tag: str,
        features: dict
    ):
        image = f"{registry_url}:{tag}"
        if dockerfile is None:
            build_cmd = ["docker", "build", "-t", image, project_root]
        else:
            build_cmd = ["docker", "build", "-f", dockerfile, "-t", image, project_root]
        return ImageBuild(
            login_cmd = ["docker", "login", registry_name],
            build_cmd = build_cmd,
            push_cmd = ["docker", "push", registry_url],
            features = features,
            image = image
        )

    def _exec(self, name: str, command: list[str]) -> Self:
        logger.info(" ".join(command))
        output = subprocess.run(command, capture_output = True)
        stdout = output.stdout.decode("utf-8")
        stderr = output.stderr.decode("utf-8")
        stdout = f"{stdout}\n" if stdout != "" else stdout
        total = stdout + stderr
        self._output[name] = total
        if output.returncode != 0:
            raise OSError(
                f"Command returned exit status {output.returncode}:\n{total}"
            )
        else:
            logger.debug(total)

        return self

    def login(self) -> Self:
        return self._exec("login", self.login_cmd)

    def build(self) -> Self:
        return self._exec("build", self.build_cmd)

    def push(self) -> Self:
        return self._exec("push", self.push_cmd)

    # def get_hash(self) -> str|None:
    #     if "build" in self._output:
    #         build_output = self._output["build"].split("\n")
    #         for line in reversed(build_output):
    #             if "writing image" not in build_output:
    #                 continue
    #             a
    #     return None

    def __repr__(self) -> str:
        return pformat(self.features)


class ImageBuilder:
    def __init__(self, version: str, builds: list[ImageBuild]):
        self.version = version
        self.builds = builds

    @classmethod
    def from_config_v1(self, input) -> Self:
        try:
            builds = []
            project_root = Path.cwd().joinpath(input.project_root).resolve()
            version_file = project_root.joinpath(input.version_file)
            registries = input.registries

            for build in input.builds:
                registry = registries[build.registry]
                builds.append(ImageBuild.default(
                    project_root = str(project_root),
                    dockerfile = None if build.dockerfile == "Dockerfile" else str(
                        project_root.joinpath(build.dockerfile)
                    ),
                    registry_name = registry.reg,
                    registry_url = registry.url,
                    tag = build.tag,
                    features = build.model_dump()
                ))

            return ImageBuilder(
                version = read_version(version_file),
                builds = builds
            )
        except Exception as e:
            logger.error(f"Failed to configure ImageBuilder: {e}")
            return None

    def with_builds(self, builds: list[ImageBuild]) -> Self:
        return ImageBuilder(
            version = self.version,
            builds = builds
        )

    def filter(self, features: dict[str,list[str]]) -> Self:
        filtered_builds = []
        for build in self.builds:
            if all([
                values is None or len(values) == 0 or build.features[feature] in values
                for feature, values in features.items()
            ]):
                filtered_builds.append(build)

        return self.with_builds(filtered_builds)

    def build(self, push: bool = False):
        for build in self.builds:
            try:
                if push:
                    build.login().build().push()
                else:
                    build.build()
            except Exception as e:
                logger.error(f"Deployment failed: {e}")

    def __repr__(self) -> str:
        return "\n".join([
            f"version: {self.version}",
            pformat(self.builds)
        ])
