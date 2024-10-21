import bpy
import sys
import bmesh
import math
from bmesh.types import BMFace
from dataclasses import dataclass

mesh = bpy.context.object.data  # Get selected object's mesh
bm = bmesh.from_edit_mesh(mesh)

# bpy.ops.mesh.select_all(action="DESELECT")

# for active_face in bm.faces:  # [f for f in bm.faces if f.select]:
#     if len(active_face.edges) == 3 and sum([len(edge.link_faces) for edge in active_face.edges]) == 4:
#         active_face.select = True
seleceted_edges = []
for active_edge in [f for f in bm.edges if f.select]:  # bm.edges:
    if len(active_edge.link_faces) == 1:
        seleceted_edges.append(active_edge)

ignored_edges = []
for active_edge in seleceted_edges:
    # skip the edge if it is already processed
    if active_edge.index not in active_edge:
        verts = [v for v in active_edge.verts]
        if len(verts) == 2:
            # collect the edge groups by the vertices indexes
            vert_1_edges = {v.index: e for e in verts[0].link_edges if len(e.link_faces) == 1 for v in e.verts if v != verts[0]}
            vert_2_edges = {v.index: e for e in verts[1].link_edges if len(e.link_faces) == 1 for v in e.verts if v != verts[1]}
        for key in vert_1_edges.keys():
            # check if the edges are connected
            if key in vert_2_edges.keys():
                active_edge.select = True
                vert_1_edges[key].select = True
                vert_2_edges[key].select = True

                ignored_edges += [active_edge.index, vert_1_edges[key].index, vert_2_edges[key].index]
                break

        bpy.ops.mesh.fill()


bmesh.update_edit_mesh(mesh)
