# *-* encoding=utf-8 *-*
import os
from ConfigParser import RawConfigParser
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class RuleLoader:
    def __init__(self):
        for item in glob.glob(os.path.join(BASE_DIR, 'conf', "*.conf")):
            self.cp = RawConfigParser()
            self.cp.read(item)

    def get_rules(self, data_type):
        return self.cp.items(data_type)

    def get_option(self, data_type, key):
        return self.cp.get(data_type, key)
