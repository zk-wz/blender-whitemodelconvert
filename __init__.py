
bl_info = {
    "name" : "白模切换",
    "author" : "掌控-物质",
    "description" : "练手小插件",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Render"
}

import bpy


from .ui import white_convert_ui

from .operator import *

from .utils import convert_back


def register():
    bpy.utils.register_class(m_OT_converter)
    bpy.utils.register_class(m_OT_convert_back)
    bpy.utils.register_class(white_convert_ui)

def unregister():
    bpy.utils.unregister_class(m_OT_converter)
    bpy.utils.unregister_class(m_OT_convert_back)
    bpy.utils.unregister_class(white_convert_ui)
