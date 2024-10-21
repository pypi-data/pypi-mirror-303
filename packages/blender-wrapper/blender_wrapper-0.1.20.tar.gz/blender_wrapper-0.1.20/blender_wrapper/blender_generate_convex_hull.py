import bpy
import os
import sys


def import_ply(filepath):
    bpy.ops.import_mesh.ply(filepath=filepath)
    return bpy.context.selected_objects[0]


def merge_objects(objects):
    bpy.ops.object.select_all(action='DESELECT')
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.object.join()
    return bpy.context.active_object


def create_convex_hull(obj):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.convex_hull()
    return bpy.context.active_object


def simplify_mesh(obj, target_faces):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type='DECIMATE')
    modifier = obj.modifiers[-1]
    modifier.ratio = target_faces / len(obj.data.polygons)
    bpy.ops.object.modifier_apply(modifier="Decimate")
    return obj


def export_ply(obj, filepath):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.export_mesh.ply(filepath=filepath, use_selection=True)


def main():
    # Get command line arguments
    args = sys.argv[sys.argv.index("--") + 1:]

    if len(args) < 2:
        print("Usage: blender --background --python script.py -- <output_file.ply> <input_file1.ply> <input_file2.ply> ...")
        return

    output_file = args[0]
    input_files = args[1:]

    # Clear existing mesh objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Import and merge PLY files
    imported_objects = [import_ply(file) for file in input_files]
    merged_object = merge_objects(imported_objects)

    # Create convex hull
    convex_hull = create_convex_hull(merged_object)

    # Simplify mesh (adjust target_faces as needed)
    simplified_mesh = simplify_mesh(convex_hull, target_faces=1000)

    # Export as PLY
    export_ply(simplified_mesh, output_file)

    print(f"Processed mesh exported to {output_file}")


if __name__ == "__main__":
    main()
