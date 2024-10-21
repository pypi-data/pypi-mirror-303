
import bpy
import sys
import bmesh
from os.path import dirname
import os

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa
from blender_utils.blender_remesh_opt import separate_chaos_vertices, flatten_bumpy_vertices  # noqa

param = parse_args()


print(f'Reconstruct Mesh {param.mesh_name}')

# remove chaos vertices (multiple surfaces share the same vertex)
for i in range(4):
    with mesh_edit(mesh_name=param.mesh_name) as bm:

        separate_chaos_vertices(bm, is_selected_only=False, max_linked_face_num=6)

        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
        bpy.ops.mesh.select_all(action="DESELECT")

with mesh_edit(mesh_name=param.mesh_name) as bm:
    for i in range(3, 6):
        verts = [v for v in bm.verts if v.select != True and len(v.link_edges) == i]
        flatten_bumpy_vertices(bm, verts=verts, max_distance_threshold=0.15)

    # Dissolve selected edges and vertices, limited by the angle of surrounding geometry
    # Reduces detail on planer faces and linear edges with an adjustable angle threshold.
    # bpy.ops.mesh.select_all(action='SELECT')
    # bpy.ops.mesh.dissolve_limited()

modifier = bpy.context.object.modifiers.new(name="CorrectiveSmooth", type="CORRECTIVE_SMOOTH")
modifier.smooth_type = 'LENGTH_WEIGHTED'
modifier.factor = 0.6
modifier.iterations = 7
modifier.use_only_smooth = True
bpy.ops.object.modifier_apply(modifier="CorrectiveSmooth")

modifier = bpy.context.object.modifiers.new(name="Smooth", type="SMOOTH")
modifier.iterations = 5
bpy.ops.object.modifier_apply(modifier="Smooth")

param.export()
