import importlib
import os

from pg_common import SingletonBase, log_info
from pg_environment import config


__all__ = ("LoaderManager", )

__auth__ = "baozilaji@gmail.com"


class _LoaderManager(SingletonBase):
    def __init__(self):
        pass

    @staticmethod
    def scan_loaders():
        from pg_resourceloader.define import KEY_RESOURCE_LOADER, KEY_RESOURCE_LOADER_BIN_LOADER_DIR
        _loader_dir = config.get_sub_conf(KEY_RESOURCE_LOADER_BIN_LOADER_DIR, KEY_RESOURCE_LOADER, "loaders")
        log_info(f"loader dirs: {_loader_dir}")

        for _root, _dirs, _files in os.walk(_loader_dir):
            for _file in _files:
                if _file.endswith(".py"):
                    _module_name = _root.replace("/", ".")
                    _module_name = f"{_module_name}.{_file[:-3]}"
                    _module = importlib.import_module(_module_name)
                    log_info(f"load loader {_module_name}")


LoaderManager = _LoaderManager()
