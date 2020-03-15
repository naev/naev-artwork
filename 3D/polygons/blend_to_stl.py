# A small file to automatically export from Blender to STL
# This script should be called from shell via :
# blender myAwesomeShip.blend --background --python blend_to_stl.py

import bpy
import os

# Extract name of file
filename = os.path.basename(bpy.data.filepath)

# Select layer 1
bpy.ops.object.select_by_layer(layers=1)

# Export
bpy.ops.export_mesh.stl("EXEC_DEFAULT",  use_selection=True, filepath=(filename + '.stl'))
