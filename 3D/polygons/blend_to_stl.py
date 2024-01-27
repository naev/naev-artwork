# A small file to automatically export from Blender to STL
# This script should be called from shell via :
# blender myAwesomeShip.blend --background --python blend_to_stl.py

import bpy
import os

# Extract name of file
filename = os.path.basename( bpy.data.filepath )

# Unselect all
for obj in bpy.data.objects:
    obj.select_set(False)

# Collection 1 should contain the main ship (old format)
for obj in bpy.data.collections['Collection 1'].all_objects:
    if obj.type!="MESH":
        continue

    obj.select_set(True)

# Export
bpy.ops.export_mesh.stl("EXEC_DEFAULT",  use_selection=True, filepath=(filename + '.stl'))
