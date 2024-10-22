from pathlib import Path
from typing import Final

from tomllib import load as load_toml


CONFIG_FILE: Final[Path] = Path("./trainerbase.toml")


with CONFIG_FILE.resolve().open("rb") as trainerbase_toml:
    trainerbase_config = load_toml(trainerbase_toml)


pymem_config = trainerbase_config["pymem"]
logging_config = trainerbase_config.get("logging")
