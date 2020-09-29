# required packages
# sudo apt-get install python-pyqt5.qtquick qml-module-qtquick-controls

import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

import linuxcnc
from qtpyvcp.actions.machine_actions import issue_mdi

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from qtpy.QtCore import Signal, Slot, QUrl, QObject
from qtpy.QtQuickWidgets import QQuickWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
STATUS = getPlugin('status')
WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class PocketWidget(QQuickWidget):

    setSafeZSig = Signal(float, arguments=['safe_z'])
    setPartZeroSig = Signal(float, arguments=['part_zero'])
    setStepDownSig = Signal(float, arguments=['step_down'])
    setFinishZSig = Signal(float, arguments=['finish_z'])

    def __init__(self, parent=None):
        super(PocketWidget, self).__init__(parent)

        if parent is None:
            return

        # self.dm = getPlugin('persistent_data_manager')

        self.stat = STATUS
        self.engine().rootContext().setContextProperty("handler", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "pocket.qml"))
        self.setSource(url)

        # self.tool_image = self.dm.getData('tool-touch-off.tool-image-table') or dict()

    @Slot(str)
    def safeZSig(self, safe_z):
        self.setSafeZSig.emit(float(safe_z))

    @Slot(str)
    def partZeroSigSig(self, part_zero):
        self.setPartZeroSig.emit(float(part_zero))

    @Slot(str)
    def stepDownSigSig(self, step_down):
        self.setStepDownSig.emit(float(step_down))

    @Slot(str)
    def finishZSigSig(self, finish_z):
        self.setFinishZSig.emit(float(finish_z))
