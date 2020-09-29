from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from qtpyvcp_conversational_gcode.widgets.facing import *
from qtpyvcp_conversational_gcode.widgets.facing import FacingWidget
from qtpyvcp_conversational_gcode.widgets.xy_coord import XYCoordWidget
from qtpyvcp_conversational_gcode.widgets.hole_circle import HoleCircleWidget
from qtpyvcp_conversational_gcode.widgets.int_line_edit import IntLineEdit
from qtpyvcp_conversational_gcode.widgets.float_line_edit import FloatLineEdit
from qtpyvcp_conversational_gcode.widgets.pocket import PocketWidget


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


class PocketWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return PocketWidget
