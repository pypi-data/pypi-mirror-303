from circuitmatter.clusters.general.identify import Identify
from circuitmatter.clusters.general.on_off import OnOff

from .. import simple_device


class OnOffLight(simple_device.SimpleDevice):
    DEVICE_TYPE_ID = 0x0100
    REVISION = 3

    def __init__(self, name):
        super().__init__(name)

        self._identify = Identify()
        self.servers.append(self._identify)

        self._on_off = OnOff()
        self._on_off.on = self.on
        self._on_off.off = self.off
        self.servers.append(self._on_off)

    def on(self, session):
        print("on!")
        self._on_off.on_off = True

    def off(self, session):
        print("off!")
        self._on_off.on_off = False
