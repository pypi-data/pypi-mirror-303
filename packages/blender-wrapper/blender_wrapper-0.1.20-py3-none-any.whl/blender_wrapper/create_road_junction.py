import bpy
import bmesh

# Ensure we are in edit mode
bpy.ops.object.mode_set(mode='EDIT')

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data

# Create a BMesh from the active mesh
bm = bmesh.from_edit_mesh(me)

# Get the selected edges
selected_edges = [e for e in bm.edges if e.select]

# Attempt to create a face from the selected edges
try:
    new_face = bm.faces.new([edge.verts[0] for edge in selected_edges])
    bmesh.update_edit_mesh(me, True)
    print("New face created.")
except ValueError:
    # This error occurs if the selected edges can't form a valid face
    print("Error: Selected edges can't form a valid face.")

# Switch back to object mode
bpy.ops.object.mode_set(mode='OBJECT')
