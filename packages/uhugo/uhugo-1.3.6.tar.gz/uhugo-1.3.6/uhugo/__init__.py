from importlib.metadata import version
from pathlib import Path

__version__ = version("uhugo")

# Creates a .uhugo folder in user folder
if not Path.home().joinpath(".uhugo").is_dir():
    Path.home().joinpath(".uhugo").mkdir(exist_ok=True)
