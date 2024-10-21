
import sys
from os.path import dirname
from inspect import getfullargspec

import bpy

bpy.ops.object.select_all(action='SELECT')
for non_mesh in [ob for ob in bpy.context.selected_objects if ob.type != 'MESH']:
    non_mesh.select_set(False)

bpy.ops.object.join()


obj = bpy.context.object
print(bpy.context.object.name)
for i in range(1, len(obj.material_slots)):
    obj.active_material_index = 1
    bpy.ops.object.material_slot_remove()

material_names = []
for material in bpy.data.materials:
    if material.name != obj.active_material.name:
        material_names.append(material.name)

for mat_name in material_names:
    bpy.data.materials.remove(bpy.data.materials[mat_name])

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles()
bpy.ops.mesh.face_make_planar()
bpy.ops.object.material_slot_assign()
bpy.ops.object.mode_set(mode='OBJECT')
