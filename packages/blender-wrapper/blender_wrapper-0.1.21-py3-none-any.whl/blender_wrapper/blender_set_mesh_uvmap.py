import bpy
import os
import sys
import bmesh
import math


argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

# parse parameters
file_path = argv.pop(0)
output_path = argv.pop(0)


"""Blender batch mode: auto rebuild uv maps

Arguments:
    file_path (str): Represent the ply file path.
    output (str): Represent the output file path. If it was not specified, it would override the file_path.
    iterations (int): Represent the packing iteration times. Higher value could make better result, 
                      but it may slow down the process. we would recommend to set '2' iteration times

"""


# parse the filename
mesh_name = os.path.basename(file_path)[:-4]

cube_ob = bpy.data.objects.get('Cube')
if cube_ob:
    bpy.data.objects.remove(cube_ob, do_unlink=True)

# load ply file
ext_name = file_path[-3:].lower()
if ext_name == 'ply':  # load ply file
    bpy.ops.import_mesh.ply(filepath=file_path)
elif ext_name == 'obj':
    bpy.ops.import_scene.obj(filepath=file_path, axis_forward='Y', axis_up='Z')
elif ext_name == 'fbx':
    bpy.ops.import_mesh.fbx(filepath=file_path)
elif ext_name in ['glb', 'gltf']:  # load gltf file
    bpy.ops.import_scene.gltf(filepath=file_path, import_shading='NORMALS')
else:
    print(f'Unsupported file {file_path}')
    sys.exit(1)

# specify the packing iteration times
# higher value could make better result, but it may slow down the process
# we would recommend to set '2' iteration times
validation_repeating_times = int(argv.pop(0)) or 16

print(f'Iteration times: {validation_repeating_times}')

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
mesh_obj = bpy.data.objects.get(mesh_name)
mesh_obj.select_set(True)

print([obj.name for obj in bpy.data.objects])
current_uv_layer_counts = len(mesh_obj.data.uv_layers)
if current_uv_layer_counts:
    print(f'Found existing UVMap: {current_uv_layer_counts}')
    # clean up the existing uvmap
    for uv_layer in mesh_obj.data.uv_layers:
        mesh_obj.data.uv_layers.remove(uv_layer)
    print(f'Cleaned up the existing UVMap')

# create a new uv map
mesh_obj.data.uv_layers.new(name="Main")
print('Created a new uv layer to rebuild the UVMap')


"""
Clean up mesh before building UVMap
========================================================================
"""

"""
Start to build UVMap
=========================================================================
"""

# start to flat uv map
bpy.ops.object.editmode_toggle()


"""
Clean up mesh before building UVMap
========================================================================
"""

bpy.ops.mesh.remove_doubles()
print('[Blender] Merge close vertices')

bpy.ops.mesh.tris_convert_to_quads()
print('[Blender] Convert triangles to quads')

bpy.ops.mesh.faces_shade_smooth()
print('[Blender] Smooth faces')

"""
Clean up mesh before building UVMap
========================================================================
"""

# parse the mesh from activated object
bm = bmesh.from_edit_mesh(mesh_obj.data)
# parse current uv layer
uv_layer = bm.loops.layers.uv.verify()

bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0)

bpy.ops.uv.select_all(action='SELECT')

# Resolve overlaping UV through UVPackmaster2 (blender addon)
invalid_face_found = 0

for ite_index in range(validation_repeating_times):
    # Validate overlapping uv and select the  invalid uv faces
    bpy.ops.uvpackmaster2.uv_validate('EXEC_DEFAULT')

    # fetch the last validating message
    # last_status_msg = bpy.context.preferences.addons['uvpackmaster2'].preferences['op_status']
    # print('================================')
    # print(last_status_msg)
    # matched_invalid_face_number = re.search(r'^Number of invalid faces found:\s(\d+)', last_status_msg)
    # if matched_invalid_face_number:
    #     invalid_face_found = int(matched_invalid_face_number[1])

    # fetch the last validating message
    # bpy.ops.uvpackmaster2.uv_overlap_check()
    # last_status_msg = bpy.context.preferences.addons['uvpackmaster2'].preferences['op_status']
    # print('================================')
    # print(last_status_msg)
    # not_found_overlapping_island = re.match(r'No overlapping islands detected', last_status_msg)

    # force split the overlapping faces
    if ite_index == validation_repeating_times-1:
        print('Force split the overlapping faces which were not islands.')
        bpy.ops.uv.select_split()

    # start to split the invalid overlapping island faces
    bpy.ops.uvpackmaster2.split_overlapping_islands('EXEC_DEFAULT')

    # move split UV face
    # it could help to make good result when interating the validation of overlapping uv
    for f in bm.faces:
        for l in f.loops:
            luv = l[uv_layer]
            if luv.select:
                # moving uv to +y
                luv.uv.y += 1

    # save the uv edits to the mesh data
    bmesh.update_edit_mesh(mesh_obj.data)

# select all isolated uv and pack together
bpy.ops.uv.select_all(action='SELECT')
bpy.ops.uvpackmaster2.uv_pack('EXEC_DEFAULT')

bpy.ops.object.editmode_toggle()


"""
force select the export mesh object
=========================================================================
"""

ob = bpy.data.objects.get(mesh_name)
ob.select_set(True)

"""
assign a default material
=========================================================================
"""
mat_name = f'{mesh_name}_mat'
mat = bpy.data.materials.get(mat_name)
if mat is None:
    # create material
    mat = bpy.data.materials.new(name=mat_name)

# Assign it to object
if ob.data.materials:
    # assign to 1st material slot
    ob.data.materials[0] = mat
else:
    # no slots
    ob.data.materials.append(mat)


print(f'Export selected mesh:[{mesh_name}] to {output_path}')

ext_name = output_path[-3:].lower()
if ext_name == 'ply':

    bpy.ops.export_mesh.ply(filepath=output_path,
                            use_selection=True,
                            use_colors=False,
                            use_normals=True,
                            use_mesh_modifiers=True)
elif ext_name == 'obj':
    bpy.ops.export_scene.obj(filepath=output_path,
                             use_selection=True,
                             use_mesh_modifiers=True,
                             axis_forward='Y',
                             axis_up='Z')
elif ext_name == 'fbx':
    bpy.ops.export_scene.fbx(filepath=output_path,
                             use_selection=True,
                             use_mesh_modifiers=True,
                             axis_forward='Y',
                             axis_up='Z')
elif ext_name == 'glb':
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLB',
        export_normals=True,
        export_materials='EXPORT',
        export_copyright='Syngular Technology',
        export_colors=False,
        use_selection=True
    )
else:
    print(f'unsupported file extension: {ext_name}')
    sys.exit(1)
