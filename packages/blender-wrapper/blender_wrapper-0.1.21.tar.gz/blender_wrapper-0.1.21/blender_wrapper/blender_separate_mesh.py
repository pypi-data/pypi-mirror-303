
from functools import reduce
import bpy
import sys
from os.path import dirname
import os
import json

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_context_manager import mesh_edit  # noqa
from blender_utils.blender_file_loader import parse_args  # noqa
from blender_utils import blender_const as keys  # noqa

param = parse_args()

output_config_path = param.argv.pop(0)
min_volume_threshold = float(param.argv.pop(0))

print(f'[Blender] Separate mesh: {param.mesh_name}')

output_config = {
    param.mesh_name: {
        keys.ARG_PATH: param.file_path,
        keys.ARG_FILE: os.path.basename(param.file_path),
        keys.ARG_VOLUME_RATIO: -1,  # skip base mesh
        keys.ARG_TEXTURE: False
    }
}

with mesh_edit(mesh_name=param.mesh_name) as bm:
    bpy.ops.mesh.separate(type='LOOSE')

meshes = {}
# iterate over all the separated meshes
# remove the mesh if the volume is smaller than the specified threshold
for index, obj in enumerate(bpy.data.objects):
    dimension = reduce(lambda x, y: x*y, obj.dimensions) / \
        1000000000  # (cm3 -> m3)
    meshes[obj.name] = dimension

# convert dimension to ratio
max_dimension = max(meshes.values())

# sort lists by volume size
object_context_list = sorted([(k, round(v/max_dimension, 2))
                             for k, v in meshes.items()], key=lambda item: item[1], reverse=True)

# ignore the sub meshes if the volume is smaller than the threshold
exports = {k: v for k, v in object_context_list if v > min_volume_threshold}

export_dir = dirname(param.export_path)

# export the meshes into each single file
# export the config file with the list of exported meshes
for index, (name, volume_ratio) in enumerate(exports.items()):
    bpy.ops.object.select_all(action='DESELECT')
    obj = bpy.data.objects[name]
    obj.select_set(True)
    obj.name = f'{param.mesh_name}_{index:02d}'
    param.export_path = os.path.join(
        export_dir, f'{obj.name}.{param.export_ext_name}')
    param.export(mesh_name=obj.name)
    output_config[obj.name] = {
        keys.ARG_PATH: param.export_path,
        keys.ARG_FILE: os.path.basename(param.export_path),
        keys.ARG_VOLUME_RATIO: volume_ratio,
        keys.ARG_TEXTURE: True
    }

json.dump(output_config, open(output_config_path, 'w'), indent=4)
