"""Data loading utilites example
"""

import pathlib
import yaml

PATH_DATA_ROOT = pathlib.Path(__file__).parent / 'data'


def load_config(name: str) -> dict:
    """Load configuration file included in the package data directory

    Args:
        name:
            str, name of the configuration file to load

    Returns:
        dict: configuration data
    """
    if not name.lower().endswith('.yaml'):
        name += '.yaml'
    path_file = PATH_DATA_ROOT / name

    with open(path_file.as_posix(), 'r') as file:
        return yaml.safe_load(file)
