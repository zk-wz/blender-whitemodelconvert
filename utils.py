import bpy



# for mat in D.materials:
#     print(mat.name)
def mat_test():
    for mat in bpy.data.materials:
        if mat.name == "temp_mat":
            return True
    return False

# 添加临时材质
def mat_add():
    if mat_test() == False:
        bpy.data.materials.new("temp_mat")


# 转换为白模
def mat_convert():
    for obj in bpy.data.objects:
        if(obj.active_material != None and obj.active_material.name != "temp_mat"):
            obj['mat_temp']=obj.active_material.name
            obj.active_material = bpy.data.materials["temp_mat"]
            # print(obj.active_material.name)

# 转换回原材质
def convert_back():
    for obj in bpy.data.objects:
        if(obj.active_material != None and obj.active_material.name == "temp_mat"):
            obj.active_material = bpy.data.materials[obj['mat_temp']]