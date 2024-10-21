import bpy
import json
import sys
import os


def create_curve_from_points(points):
    curve_data = bpy.data.curves.new(name="GeneratedCurve", type='CURVE')
    curve_data.dimensions = '3D'

    polyline = curve_data.splines.new('POLY')
    polyline.points.add(len(points) - 1)

    for i, point in enumerate(points):
        x, y, z = point
        polyline.points[i].co = (x, y, z, 1)

    curve_obj = bpy.data.objects.new("GeneratedCurveObject", curve_data)
    bpy.context.collection.objects.link(curve_obj)

    return curve_obj


def get_mesh_x_length(obj):
    dims = obj.dimensions
    return dims.x


def get_spline_length(curve_obj):
    curve_obj.data.update()
    return sum(spline.calc_length() for spline in curve_obj.data.splines)


def add_modifiers_to_mesh(obj, curve_obj, deform_axis):
    # Array modifier
    array_modifier = obj.modifiers.new(name="Array", type='ARRAY')
    array_modifier.fit_type = 'FIT_CURVE'
    array_modifier.curve = curve_obj

    mesh_length = get_mesh_x_length(obj)
    spline_length = get_spline_length(curve_obj)

    if mesh_length != 0:
        count = spline_length / mesh_length
        array_modifier.count = round(count)

    # Curve modifier
    curve_modifier = obj.modifiers.new(name="Curve", type='CURVE')
    curve_modifier.object = curve_obj
    curve_modifier.deform_axis = deform_axis.upper()


def main():
    # Load data from JSON file
    with open(sys.argv[-1], 'r') as f:
        data = json.load(f)

    # Import FBX
    bpy.ops.import_scene.fbx(filepath=data["mesh"])
    imported_objects = bpy.context.selected_objects

    # We assume the first selected object is the main FBX mesh.
    if not imported_objects:
        print("No objects imported from FBX!")
        return

    main_obj = imported_objects[0]

    # Create curve from points
    curve_obj = create_curve_from_points(data["points"])

    # Add modifiers to the imported mesh
    add_modifiers_to_mesh(main_obj, curve_obj, data["deform_axis"])

    # Export to FBX
    bpy.ops.export_scene.fbx(filepath=data["output"])


if __name__ == "__main__":
    main()
