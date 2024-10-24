import logging
import os
import sys
from pathlib import Path
from shutil import copy2

CONFIG_FILE = "agentic_config.py"
NODE_FILE = "agentic_node.py"

log = logging.getLogger(__name__)


def init_agentic(backend: str, force: bool) -> None:
    if not os.path.isfile("pyproject.toml"):
        log.error("!!!!")
        log.error(
            "ERROR:You have to run this command in the root folder of your project"
        )
        log.error("!!!!")
        sys.exit(1)

    # prepare paths
    target_path = Path("src") / "agentic"
    target_path.mkdir(parents=True, exist_ok=True)
    (target_path / "__init__.py").touch()
    source_folder = Path(__file__).parent / "templates"

    # copy files and templates if they don't exist already
    if force or not os.path.isfile(target_path / CONFIG_FILE):
        copy_template(source_folder / CONFIG_FILE, target_path / CONFIG_FILE)
    else:
        log.info("Config file already exists")

    if force or not os.path.isfile(target_path / NODE_FILE):
        copy2(source_folder / NODE_FILE, target_path)
    else:
        log.info("Node file already exists")


def copy_template(source_folder: Path, target_path: Path) -> None:
    folder_name = os.path.basename(os.getcwd()).replace("-", "_")
    class_name = (
        folder_name.replace("_", " ").replace("-", "_").title().replace(" ", "")
    )

    with open(source_folder, "r") as file:
        content = file.read()

    content = content.replace("{{folder_name}}", folder_name)
    content = content.replace("{{class_name}}", class_name)

    with open(target_path, "w") as file:
        file.write(content)
