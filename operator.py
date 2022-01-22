import bpy
from .utils import *


class m_OT_converter(bpy.types.Operator):
    bl_idname = "mat.convert_to_white"
    bl_label = "white_model_converter"
    # bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        mat_add()
        mat_convert()
        return {"FINISHED"}


class m_OT_convert_back(bpy.types.Operator):
    bl_idname = "mat.convert_back"
    bl_label = "white_model_converter——back"
    # bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        convert_back()
        return {"FINISHED"}
