import bpy
import os
import sys
from os.path import dirname

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.Blender_enable_cuda import enable_gpus  # noqa

enable_gpus()


argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

if len(argv) < 6:
    print(f'Missing required parameters: {argv}')
    sys.exit(1)

# parse parameters
file_path = argv.pop(0)
output_path = argv.pop(0)
material_name = argv.pop(0)
bake_mode = argv.pop(0).upper()
scale = float(argv.pop(0))
texture_size = int(argv.pop(0))

# Set the texture path
environment_texture_path = argv.pop(0)
bpy.context.scene.world.node_tree.nodes['Environment Texture'].image = bpy.data.images.load(
    environment_texture_path)
bpy.context.scene.world.node_tree.nodes["Background"].inputs[1].default_value = float(
    argv.pop(0))

output_scene = argv.pop(0) if argv else None

BAKE_MODES = ['DIFFUSE', 'AO', 'SHADOW', 'NORMAL', 'UV', 'ROUGHNESS',
              'EMIT', 'ENVIRONMENT', 'GLOSSY', 'TRANSMISSION', 'COMBINED']

# validate bake mode
if bake_mode not in BAKE_MODES:
    raise ValueError(f'Invalid bake mode: {bake_mode}')

# parse the filename
mesh_name = os.path.basename(file_path)[:-4]

# load ply file
ext_name = file_path[-3:].lower()

if ext_name == 'ply':
    bpy.ops.wm.ply_import(filepath=file_path)
elif ext_name == 'obj':
    bpy.ops.wm.obj_import(
        filepath=file_path, forward_axis='Y', up_axis='Z')
elif ext_name == 'fbx':
    bpy.ops.import_scene.fbx(filepath=file_path)
elif ext_name in ['glb', 'gltf']:  # load gltf file
    bpy.ops.import_scene.gltf(
        filepath=file_path, import_shading='NORMALS', import_pack_images=False)
else:
    print(f'Unsupported file {file_path}')
    sys.exit(1)

mesh_obj = bpy.data.objects.get(mesh_name)

# set mesh_obj origin to geometry
mesh_obj.select_set(True)
bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')

# set mesh_obj location to (0, 0, 0)
mesh_obj.location = (0, 0, 0)

bpy.context.view_layer.objects.active = mesh_obj

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.remove_doubles()
bpy.ops.mesh.faces_shade_smooth()

# start to flat uv map
bpy.ops.object.editmode_toggle()

mesh_obj = bpy.context.selected_objects[0]

current_uv_layer_counts = len(mesh_obj.data.uv_layers)

if not current_uv_layer_counts:
    print('No found valid UVMap, abort baking textures!')
    sys.exit(1)

"""
Resize mesh object
========================================================
"""
bpy.ops.transform.resize(value=[scale]*3)

"""
Create output textures
========================================================
"""
texture_name = 'Bake_Texture'
texture_img = bpy.data.images.new(texture_name, texture_size, texture_size)


"""
Get materials
========================================================
"""

main_mat = bpy.data.materials.get(material_name)

if not main_mat:
    print(f'No found matched material object! {material_name}')
    sys.exit(1)

"""
Create texture node in the associated material
========================================================
"""
# setup main material
main_mat_nodes = main_mat.node_tree.nodes
# create dc node and hook up dc image
texture_node = main_mat_nodes.new('ShaderNodeTexImage')
texture_node.name = 'Bake_Texture'
texture_node.select = True
main_mat_nodes.active = texture_node
texture_node.image = texture_img

"""
Get mesh object and initialize the materials slots
========================================================
"""
model_obj = bpy.data.objects.get(mesh_name)

model_obj.data.materials.clear()

model_obj.data.materials.append(main_mat)


bpy.context.view_layer.objects.active = model_obj

bpy.context.scene.render.bake.margin = 2
bpy.context.scene.render.bake.margin_type = 'ADJACENT_FACES'

bpy.ops.object.bake(type=bake_mode, save_mode='EXTERNAL')


texture_img.save_render(filepath=output_path)

if output_scene:
    bpy.ops.wm.save_as_mainfile(filepath=output_scene)
