#/usr/bin/env python

import math
import bpy
import os
from os import path
from os.path import dirname

#
#  global variables
#
filename = os.path.basename(bpy.data.filepath)
scn = bpy.context.scene
ctxt = scn.render

def Initialize():
   # unlink stuff we don't want
   for obj in bpy.data.objects:
      if obj.type in ('CAMERA','LAMP'):
         scn.objects.unlink(obj)
   scn.update()

   # set the camera up
   cam = bpy.data.cameras.new('ORTHO')
   camobj = bpy.data.objects.new(name="Camera1", object_data=cam)
   camobj.location = 7.0, 0.0, 0.0
   sunobj.rotation_mode = 'XYZ'
   camobj.rotation_euler = math.pi/2., 0.0, math.pi/2.
   scn.objects.link(camobj)
   scn.objects.camera = camobj

   # set lighting up
   sun = bpy.data.lamps.new('Spot1','SPOT')
   sun.use_specular = False
   sun.energy = 4
   sunobj = bpy.data.objects.new(name='MyLamp1', object_data=sun)
   sunobj.location = 25. / math.sqrt(2), -25. / math.sqrt(2), 25.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euelr = 0.0, 45.0, -45.0
   scn.objects.link(sunobj)

   # set the rendering context up
   ctxt.image_settings.file_format = 'PNG';
   ctxt.alpha_mode = 'PREMUL'
   ctxt.resolution_x = 512
   ctxt.resolution_y = 512

   ctxt.threads = 3
   ctxt.use_antialiasing = True
   ctxt.filepath = os.getcwd() + "/"

if __name__ == "__main__":
   Initialize()
