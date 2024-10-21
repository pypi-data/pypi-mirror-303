from contextlib import contextmanager
from bmesh.types import BMesh
import bpy
import bmesh


@contextmanager
def mesh_edit(mesh_name: str, is_force_deselect=True, is_triangulate: bool = True, is_clean_up_mesh: bool = True) -> BMesh:
    try:
        if mesh_name:
            bpy.ops.object.select_all(action='DESELECT')
            obj = bpy.data.objects[mesh_name]
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj

        bpy.ops.object.mode_set(mode='EDIT')

        if is_triangulate:
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')

        if is_force_deselect:
            bpy.ops.mesh.select_all(action="DESELECT")

        bm = bmesh.from_edit_mesh(bpy.context.object.data)
        bm.edges.ensure_lookup_table()
        bm.verts.ensure_lookup_table()
        bm.faces.ensure_lookup_table()

        yield bm

    finally:
        # clean up mesh
        if is_clean_up_mesh:
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete_loose()
            bpy.ops.mesh.remove_doubles()

        bmesh.update_edit_mesh(bpy.context.object.data)
        bpy.ops.object.mode_set(mode='OBJECT')
