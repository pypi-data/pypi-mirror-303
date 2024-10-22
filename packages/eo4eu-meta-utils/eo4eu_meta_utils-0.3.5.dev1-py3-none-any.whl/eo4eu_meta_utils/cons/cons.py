from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint
import logging

from .logs import logger
from .builder import ImageBuilder
from .recipe import parse_recipe_file


def run():
    parser = ArgumentParser(add_help = False)
    parser.add_argument("commands", type = str, nargs = "*")
    parser.add_argument("--debug", "-d", action = "store_true")
    parser.add_argument("--lockfile-dir", default = ".cons.lock")

    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    lockfile_dir = Path(args.lockfile_dir)
    if not lockfile_dir.is_absolute():
        lockfile_dir = Path.cwd().joinpath(lockfile_dir)

    commands = args.commands
    if len(commands) < 1:
        logger.error("Need at least 1 command")
        return

    command, rest = commands[0], commands[1:]
    action_dict = {
        "build": False,
        "deploy": True,
    }
    if command in action_dict:
        if len(rest) < 1:
            logger.critical(f"Command \"{command}\" needs at least 1 argument")
            return

        push = action_dict[command]
        for filename in rest:
            builders = parse_recipe_file(filename)
            for key, builder in builders.items():
                # print(key)
                # print(builder)
                logger.info(f"Building {key}: version {builder.version}...")
                builder.build(push)
    else:
        logger.critical(f"Command \"{command}\" not recognized.")
