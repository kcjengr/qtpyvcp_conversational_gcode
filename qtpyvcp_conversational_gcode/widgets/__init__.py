from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from qtpyvcp_conversational_gcode.widgets.hole_circle import *
class HoleCircleWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return HoleCircleWidget

