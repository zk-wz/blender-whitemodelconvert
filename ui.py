import bpy
from .operator import *
D = bpy.data
C = bpy.context

class white_convert_ui(bpy.types.Panel):
    bl_idname = "MAT_PT_CONVERT"
    bl_label = "一键白模转换"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.scale_y = 3.0
        row.operator("mat.convert_to_white",text="转换为白模")

        row = layout.row()
        row.scale_y = 3.0
        row.operator("mat.convert_back",text="转回原材质")
