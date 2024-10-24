import importlib.util
import logging
import os
import sys
from subprocess import run

from dotenv import load_dotenv

from ..node.settings import settings
from ..node.wsnode import WSNode

HTTPSERVER = "httpserver"
REGISTRY = "registry"

log = logging.getLogger(__name__)


def run_agentic(*, mode: str, port: int, dev: bool, registry: str) -> None:
    if not os.path.isfile("pyproject.toml"):
        log.error("!!!!")
        log.error(
            "ERROR:You have to run this command in the root folder of your project"
        )
        log.error("!!!!")
        sys.exit(1)
    if mode == HTTPSERVER:
        cmd = ["fastapi"]
        cmd += ["dev", "--reload"] if dev else ["run"]
        cmd += ["--port", str(port)]
        cmd += ["src/agentic/agentic_node.py"]
        log.info("Running command: ", cmd)
        run(cmd, check=True)
    elif mode == REGISTRY:
        load_dotenv(verbose=True, dotenv_path=os.getcwd() + "/.env")
        # import workflows from the config file
        config_path = os.path.join(os.getcwd(), settings.AGENTIC_CONFIG_PATH)
        spec = importlib.util.spec_from_file_location("agentic_config", config_path)
        if spec is None:
            raise ValueError("Invalid config file")
        module = importlib.util.module_from_spec(spec)
        if spec.loader is None:
            raise ValueError("Invalid config file")
        src_path = settings.AGENTIC_CONFIG_PATH.split("/")[0]
        sys.path.append(os.getcwd() + "/" + src_path)
        spec.loader.exec_module(module)
        WSNode(config=module.config, registry=registry).connect_to_registry()

    else:
        raise ValueError("Invalid mode")
