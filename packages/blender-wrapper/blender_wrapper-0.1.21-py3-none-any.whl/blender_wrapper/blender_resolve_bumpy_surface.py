

import sys
from os.path import dirname

import bmesh
import bpy
from bmesh.types import BMFace

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_file_loader import parse_args  # noqa
from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_resolve_bumpy_surface import select_bumpy_faces  # noqa

param = parse_args()

# declare the angle degree threshold for the bumpy surface
# the surface is considered as bumpy if the angle between the faces are less than this threshold
max_angle_threshold = 90

with mesh_edit(mesh_name=param.mesh_name) as bm:

    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles()

    selected_faces = select_bumpy_faces(bm.faces, max_angle_threshold)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.select == True], context='FACES')

param.export()
