import bpy
import re

MESH_NAME_PATTERN = r"^marsdicom_\w+"

bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
bpy.context.scene.cursor.rotation_euler = (0.0, 0.0, 0.0)

bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
model_root = bpy.context.active_object
model_root.name = "Models"

# select the mesh objects
for ob in bpy.context.visible_objects:
    if ob.type != 'MESH':
        continue
    elif re.match(MESH_NAME_PATTERN, ob.name, re.IGNORECASE):
        const = ob.constraints.new(type='CHILD_OF')
        const.target = model_root


bpy.ops.transform.rotate(value=3.14159, orient_axis='X', orient_type='GLOBAL')
bpy.ops.transform.resize(value=(0.015, 0.015, 0.015), orient_type='GLOBAl')
