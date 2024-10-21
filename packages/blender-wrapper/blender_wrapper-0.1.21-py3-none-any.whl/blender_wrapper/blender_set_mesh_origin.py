
import bpy
import sys
import bmesh
from os.path import dirname
import os

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa

param = parse_args()


# parse the new origin values
origin = list(map(lambda x: float(x), param.argv))

print(f'Set mesh origin to the specific mesh {param.mesh_name}: new origin {origin}')

with mesh_edit(mesh_name=param.mesh_name) as bm:
    bmesh.ops.translate(
        bm,
        verts=bm.verts,
        vec=origin)

param.export()
