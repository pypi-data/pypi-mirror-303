
import bpy
import sys
from os.path import dirname
import os

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa

param = parse_args()

angle = float(param.argv.pop(0))

# convert angle to radian
angle = angle * 3.14159 / 180

print(f'Apply mesh smooth on: {param.mesh_name}')

with mesh_edit(mesh_name=param.mesh_name) as bm:

    bpy.ops.mesh.select_all(action="SELECT")

    # clear sharp edges
    bpy.ops.mesh.mark_sharp(clear=True)

    # Set sharpness by angle
    bpy.ops.mesh.set_sharpness_by_angle(angle=angle)


param.export()
