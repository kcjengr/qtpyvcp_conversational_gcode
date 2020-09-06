from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from qtpyvcp_conversational_gcode.widgets.facing import *
from qtpyvcp_conversational_gcode.widgets.xy_coord import *
from qtpyvcp_conversational_gcode.widgets.hole_circle import *
from qtpyvcp_conversational_gcode.widgets.int_line_edit import *
from qtpyvcp_conversational_gcode.widgets.float_line_edit import *


class FloatLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FloatLineEdit


class IntLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return IntLineEdit


class HoleCircleWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return HoleCircleWidget


class XYCoordWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return XYCoordWidget


class FacingWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FacingWidget
