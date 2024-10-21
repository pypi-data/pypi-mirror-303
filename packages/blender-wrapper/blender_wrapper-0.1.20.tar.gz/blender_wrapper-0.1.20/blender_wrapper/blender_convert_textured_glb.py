
import bpy
import sys
from os.path import dirname

# add the utils directory to sys.path
sys.path.append(dirname(__file__))

from blender_utils.blender_file_loader import parse_args  # noqa

param = parse_args()

texture_path = param.argv.pop(0)

obj = bpy.context.active_object

bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')

obj.location = (0, 0, 0)

# Create a new material
mat = bpy.data.materials.new(name="MyMaterial")

# Set the material type to "Principled BSDF"
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]

# Create a new image texture node
tex_image = mat.node_tree.nodes.new("ShaderNodeTexImage")

# Load an external image file
tex_image.image = bpy.data.images.load(texture_path)

# Connect the image texture to the color channel of the Principled BSDF node
mat.node_tree.links.new(tex_image.outputs[0], bsdf.inputs[0])

# Assign the material to the active object
if obj.data.materials:
    obj.data.materials[0] = mat
else:
    obj.data.materials.append(mat)

# Apply the scale transformation
bpy.ops.object.transform_apply(scale=True)

param.export()
