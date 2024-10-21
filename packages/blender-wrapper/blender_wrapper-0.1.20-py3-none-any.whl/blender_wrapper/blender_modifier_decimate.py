
import sys
from os.path import dirname

import bpy

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_file_loader import parse_args  # noqa

param = parse_args()

decimate_ratio = float(param.argv.pop(0))

# Add remesh modifier to the import mesh object
modifier = bpy.data.objects[param.mesh_name].modifiers.new(name="Decimate", type='DECIMATE')
modifier.use_collapse_triangulate = True
modifier.ratio = decimate_ratio
modifier.decimate_type = 'COLLAPSE'


param.export()
