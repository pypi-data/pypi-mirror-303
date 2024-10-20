from pg_common import log_info
from pg_objectserialization import loads
from pg_environment import config as penv
from pg_resourceloader.define import *


__all__ = ("Loader", )


class Loader(object):

    def __init__(self, name: str):
        self.name = name
        self.bin_dir = "cfg_bin"
        self.data = {}
        _cfg = penv.get_conf(KEY_RESOURCE_LOADER)

        if _cfg:
            if KEY_RESOURCE_LOADER_BIN_DIR in _cfg and _cfg[KEY_RESOURCE_LOADER_BIN_DIR]:
                self.bin_dir = _cfg[KEY_RESOURCE_LOADER_BIN_DIR]

        if not self.bin_dir.startswith("/"):
            self.bin_dir = "%s/%s" % (penv.get_pwd(), self.bin_dir)

        self._load()

    def get_by_id(self, _id):
        return self.data[_id] if _id in self.data else None

    def _load(self):
        _name = "%s/%s.bin" % (self.bin_dir, self.name)
        with open(_name, "rb") as _bin:
            _bytes = _bin.read()
            _datas = loads(_bytes)
            for _d in _datas:
                self.data[_d['id']] = _d
                self.load_one(_d)

        log_info(f"loading cfg {_name} success.")

    def load_one(self, data):
        pass
