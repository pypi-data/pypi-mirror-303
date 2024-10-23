import os
from configparser import DuplicateSectionError
from typing import Optional

from aliot.core._config.constants import CONFIG_FILE_NAME, DEFAULT_FOLDER, DEFAULT_CONFIG_FILE_PATH
from aliot.core._config.config import make_config_section, get_default_code
from aliot.core._config.config import update_config, config_init, get_config
from aliot.core._config.templates import from_template


def make_init(folder: str):
    """Makes the _config.ini"""
    os.makedirs(folder, exist_ok=True)
    path = f"{folder}/{CONFIG_FILE_NAME}"
    if os.path.exists(path):
        return False, "Config file already exists"
    try:
        config_init(path)
    except ValueError as e:
        return None, f"Could not create config file: {e!r}"
    return True, None


def make_obj(obj_name: str, template: str = "complete", main_name: str = None):
    if main_name is None:
        main_name = obj_name
    path = f"{DEFAULT_FOLDER}/{obj_name}"
    if os.path.exists(path):
        return False, "Object already exists"
    try:
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/{main_name}.py", "w+", encoding="utf-8") as f:
            f.write(from_template(template, obj_name, path))
    except FileNotFoundError:
        return None, f"Could not create object script at {path!r}"

    return True, None


def make_obj_config(obj_name: str, fields_to_overwrite: dict = None):
    if fields_to_overwrite is None:
        fields_to_overwrite = {}
    try:
        config = get_config(DEFAULT_CONFIG_FILE_PATH)
        config.add_section(obj_name)
        tmp_dict = make_config_section(obj_name)
        tmp_dict.update(fields_to_overwrite)
        config[obj_name] = tmp_dict
        update_config(DEFAULT_CONFIG_FILE_PATH, config)
    except (ValueError, DuplicateSectionError) as e:
        return False, f"Could not update config file: {e!r}"
    except FileNotFoundError:
        return (
            None,
            f"Could not find config file at {DEFAULT_CONFIG_FILE_PATH!r} (try running `aliot init)`",
        )

    return True, None
