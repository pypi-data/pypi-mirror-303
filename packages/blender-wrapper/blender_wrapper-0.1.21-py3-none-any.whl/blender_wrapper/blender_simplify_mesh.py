# Ignoring the interior surfaces of a mesh while generating a point cloud in Blender
# using a script can be a bit more complex. The goal is to ensure that points are only
# generated on the external surfaces of the mesh. Here are some steps you can take in
# your script to achieve this:
#
# Analyze Normals: Blender's mesh data structure includes normals for each face.
# Normals are vectors perpendicular to the face's surface. For an enclosed mesh, the
# normals of the external faces generally point outwards, while the normals of internal
# faces point towards the interior. You can use this property to distinguish between
# external and internal faces.
#
# Select External Faces Only: Modify your script to consider only those faces whose
# normals point outwards. This might involve calculating the average normal direction
# or using other geometric properties of the mesh.
#
# Point Generation on External Faces: Once you've identified the external faces, you can
# proceed to generate points on these faces as you did in the previous script.


from mathutils import Vector
import bpy
import bmesh
import sys
from os.path import dirname

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa


def delete_faces_by_distance(obj, distance_threshold):
    if obj.type != 'MESH':
        print("Selected object is not a mesh.")
        return

    # Ensure you're in object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Create a BMesh representation
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    # Update face normals
    bm.faces.ensure_lookup_table()
    bm.normal_update()

    # Distance to move the ray origin along the normal (to avoid self-intersection)
    offset_dist = 0.1

    # Lists to keep track of elements to delete
    faces_to_delete = set()
    verts_to_delete = set()
    # edges_to_delete = set()

    # Perform ray casting
    for face in bm.faces:
        origin = face.calc_center_median() + (face.normal * offset_dist)
        direction = face.normal
        hit, loc, norm, face_index = obj.ray_cast(
            obj.matrix_world @ origin, obj.matrix_world.to_3x3() @ direction)

        if hit:
            distance = (loc - origin).length
            if (distance_threshold == 0 or distance < distance_threshold) and face_index != face.index:
                faces_to_delete.add(face)
                for vert in face.verts:
                    if all(f in faces_to_delete for f in vert.link_faces):
                        verts_to_delete.add(vert)
#                for edge in face.edges:
#                    if all(f in faces_to_delete for f in edge.link_faces):
#                        edges_to_delete.add(edge)

    # Delete faces, vertices, and edges
    for face in faces_to_delete:
        bm.faces.remove(face)
    for vert in verts_to_delete:
        bm.verts.remove(vert)
#    for edge in edges_to_delete:
#        bm.edges.remove(edge)

    # Write the changes back to the mesh
    bm.to_mesh(obj.data)
    bm.free()


def separate_and_keep_largest(obj):
    # Ensure we're in object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Select the object and make it active
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Switch to edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Separate by loose parts
    bpy.ops.mesh.separate(type='LOOSE')

    # Switch back to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Find the object with the most triangles
    separated_objects = bpy.context.selected_objects
    largest_object = max(
        separated_objects, key=lambda obj: len(obj.data.polygons))

    # Delete all objects except the largest
    for obj in separated_objects:
        if obj != largest_object:
            bpy.data.objects.remove(obj, do_unlink=True)

    # Select and make active the largest object
    largest_object.select_set(True)
    bpy.context.view_layer.objects.active = largest_object


def apply_remesh(obj, mode: str = 'SMOOTH', octree_depth: int = 8):
    modifier = obj.modifiers.new(
        name="Remesh", type='REMESH')
    modifier.mode = mode
    modifier.octree_depth = octree_depth
    modifier.use_smooth_shade = True
    modifier.use_remove_disconnected = False
    bpy.ops.object.modifier_apply(modifier="Remesh")


param = parse_args()

# Set the distance threshold
# 0 means ignore the threshold
distance_threshold = float(param.argv.pop(0))

# Get the active object
active_obj = bpy.context.active_object

# Perform operation
delete_faces_by_distance(active_obj, distance_threshold)

apply_remesh(active_obj)

separate_and_keep_largest(active_obj)

param.export()
