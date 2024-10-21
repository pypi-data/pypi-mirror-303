
import bpy
import sys
from os.path import dirname
import os

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa

param = parse_args()

is_smooth = param.argv.pop(0).lower() in ['true', 't', '1']

print(f'Apply mesh smooth on: {param.mesh_name}')

with mesh_edit(mesh_name=param.mesh_name) as bm:

    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles()
    if is_smooth:
        bpy.ops.mesh.faces_shade_smooth()

param.export()
