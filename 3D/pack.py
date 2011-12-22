#/usr/bin/env python

import math
import bpy

if __name__ == "__main__":
 #  Blender.PackAll()
   bpy.ops.file.pack_all()
   filename = os.path.basename(bpy.data.filepath)
   bpy.ops.wm.save_mainfile(filename,False)

   bpy.ops.wm.quit_blender()
