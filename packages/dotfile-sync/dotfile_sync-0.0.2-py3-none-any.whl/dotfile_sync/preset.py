import os

import yaml

CURDIR = os.path.dirname(__file__)
PRESET = os.path.join(CURDIR, 'preset.yaml')


class Preset:
    def __init__(self):
        self._preset = yaml.safe_load(open(PRESET))

    def parse(self, expression):
        keys = expression.split('.')
        if len(keys) == 1:
            return self._preset[keys[0]].values()
        elif len(keys) == 2:
            return [self._preset[keys[0]][keys[1]]]
