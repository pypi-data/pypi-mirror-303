import bpy
import os
import sys


argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

# parse parameters
file_path = argv.pop(0)
output_path = argv.pop(0)

# parse the filename
mesh_name = os.path.basename(file_path)[:-4]

# load ply file
bpy.ops.import_mesh.ply(filepath=file_path)
