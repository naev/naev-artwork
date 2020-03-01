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

   sun2 = bpy.data.lamps.new('Hemi3','HEMI')
   sun2.energy = 0.5

   # set the camera up
   cam_data = bpy.data.cameras.new('Camera1')
   camobj = bpy.data.objects.new(name="MyCam1", object_data=cam_data)
   camobj.location = -9.0, 0.0, 9.0
   camobj.rotation_mode = 'XYZ'
   camobj.rotation_euler = 0.0, 45.0, 0.0
   scn.objects.link(camobj)
   scn.update()

   # set lighting up
   sun = bpy.data.lamps.new('Spot1','SPOT')
   sun.use_specular = False
   sun.energy = 1.0
   sun_o = bpy.data.objects.new(name='MyLamp1', object_data=sun)
   scn.objects.link(sun_o)
   scn.update()

   sun_data = bpy.data.lamps.new('Lamp2', 'SUN')
   sunobj = bpy.data.objects.new(name='MyLamp2', object_data=sun_data)
   sunobj.location = 25. / math.sqrt(2), -25.0 / math.sqrt(2), 25.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 45.0, -45.0
   scn.objects.link(sunobj)
   scn.update()

   # set lighting up
   sun_o2 = bpy.data.objects.new(name='MyLamp3', object_data=sun2)
   scn.objects.link(sun_o2)
   scn.update()
   sunobj2 = bpy.data.lamps.new('Lamp4', 'SUN')
   sun_obj2 = bpy.data.objects.new(name='MyLamp4', object_data=sunobj2)
   sun_obj2.location = 25. / math.sqrt(2), -25.0 / math.sqrt(2), 25.0
   sun_obj2.rotation_mode = 'XYZ'
   sun_obj2.rotation_euler = 0.0, 45.0, -45.0
   scn.objects.link(sun_obj2)
   scn.update()

   # set the rendering context up
   ctxt.image_settings.file_format = 'PNG';
   ctxt.alpha_mode = 'TRANSPARENT'
   ctxt.filepath = "./"
   ctxt.resolution_x = 512
   ctxt.resolution_y = 512
   ctxt.threads = 3
   ctxt.use_antialiasing = True

def Render():
   ctxt.filepath = "000.png"
   ctxt.use_file_extension = True
   bpy.ops.render.render(write_still=True)

Initialize()
Render()
bpy.ops.wm.quit_blender()
