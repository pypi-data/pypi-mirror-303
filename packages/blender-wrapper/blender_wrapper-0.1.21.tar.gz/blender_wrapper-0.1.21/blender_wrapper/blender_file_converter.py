
import bpy
import sys
from os.path import dirname

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa

param = parse_args()
scale_factor = float(param.argv.pop(0))

print(f'Convert format: {param.file_path} to: {param.export_path}')

"""
Resize mesh object
========================================================
"""
bpy.ops.transform.resize(value=[scale_factor]*3)

# apply scale transformation
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


with mesh_edit(mesh_name=param.mesh_name) as bm:

    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles()

param.export()
