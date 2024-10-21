import sys
import copy
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .recipe import Recipe
from .message import KafkaMessage
from .defaults import default_kafka, default_autotest


class TestConfig:
    def __init__(self, recipes: list[Recipe], **kwargs):
        self._recipes = recipes
        self._attrs = kwargs

    def recipes(self) -> list[Recipe]:
        return self._recipes

    def to_dict(self, script_path: str|None = None) -> dict:
        if script_path is None:
            script_path = f"${{PWD}}/{sys.argv[0]}"

        result = copy.deepcopy(self._attrs)
        recipe_services = {
            recipe.name(): recipe.to_dict()
            for recipe in self._recipes
        }
        if "services" in result:
            result["services"] |= recipe_services
        else:
            result["services"] = recipe_services
        if "kafka" not in result["services"]:
            result["services"]["kafka"] = default_kafka()
        if "consume" not in result["services"]:
            result["services"]["consume"] = default_autotest(
                config_path = script_path,
                name = "at-cons",
                command = "autotest-consume",
                healthcheck = {
                    "test": ["CMD", "autotest-healthcheck"],
                    "retries": 1,
                    "start_period": "5s",
                    "start_interval": "0s"
                }
            )
        if "produce" not in result["services"]:
            result["services"]["produce"] = default_autotest(
                config_path = script_path,
                name = "at-prod",
                command = "autotest-produce",
                depends_on = {
                    recipe.name(): {"condition": "service_started"}
                    for recipe in self._recipes
                }
            )

        return result

    def to_yaml(self) -> str:
        return dump(self.to_dict(), Dumper = Dumper)

    def cleanup(self):
        shutil.rmtree(Recipe.LOCAL_CFG_DIR)

    def inputs(self) -> list[KafkaMessage]:
        result = []
        for recipe in self._recipes:
            result.extend(recipe.inputs())
        return result

    def outputs(self) -> list[KafkaMessage]:
        result = []
        for recipe in self._recipes:
            result.extend(recipe.outputs())
        return result
