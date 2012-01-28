#/usr/bin/env python

import math
import bpy
import os

def Initialize( intensity=1., resolution=512 ):
   # variables to use
   scn = bpy.context.scene
   ctxt = scn.render

   # unlink stuff we don't want
   for obj in bpy.data.objects:
      if obj.type in ('CAMERA','LAMP'):
         scn.objects.unlink(obj)
   scn.update()

   # set the camera up
   cam = bpy.data.cameras.new('persp')
   cam.lens=28
   camobj = bpy.data.objects.new(name="Camera1", object_data=cam)
   camobj.location = -9.0, 0.0, 5.0
   camobj.rotation_mode = 'XYZ'
   camobj.rotation_euler = math.pi / 3., 0.0, -math.pi / 2.
   scn.objects.link(camobj)
   scn.update()
   scn.camera = camobj

   # Overhead Spot
   sun = bpy.data.lamps.new('Area1','AREA')
   sun.use_specular = False
   sun.energy = .4*intensity
   sunobj = bpy.data.objects.new(name='MyLamp2', object_data=sun)
   sunobj.location = 9.0, -9.0, 14.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, math.pi / 4., -math.pi / 4.
   scn.objects.link(sunobj)

   # Forward Upper Spot
   sun = bpy.data.lamps.new('Spot1','SPOT')
   sun.energy = .32*intensity
   sunobj = bpy.data.objects.new(name='MyLamp3', object_data=sun)
   sunobj.location = 0.0, -15.0, 7.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 1.13446, 0.0, 0.0
   scn.objects.link(sunobj)

   # Forward Lower Spot
   sun = bpy.data.lamps.new('Spot2','SPOT')
   sun.energy = .64*intensity
   sunobj = bpy.data.objects.new(name='MyLamp4', object_data=sun)
   sunobj.location = 0.0, -15.0, -7.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 2.00712, 0.0, 0.0
   scn.objects.link(sunobj)

   # Forward Middle Hemi
   sun = bpy.data.lamps.new('Hemi1','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp5', object_data=sun)
   sunobj.location = 0.0, -15.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 1.57079, 0.0, 0.0
   scn.objects.link(sunobj)

   # Back Middle Hemi
   sun = bpy.data.lamps.new('Hemi2','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp6', object_data=sun)
   sunobj.location = 0.0, 15.0, -3.5
   sunobj.rotation_quaternion = sunobj.rotation_quaternion[0], 4.71238, 0.0, 0.0
   scn.objects.link(sunobj)

   # Left Middle Hemi
   sun = bpy.data.lamps.new('Hemi3','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp7', object_data=sun)
   sunobj.location = -15.0, 0.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 1.57079, 3.14159
   scn.objects.link(sunobj)

   # Right Middle Hemi
   sun = bpy.data.lamps.new('Hemi4','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp8', object_data=sun)
   sunobj.location = 15.0, 0.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, -1.57079, 3.14159
   scn.objects.link(sunobj)

   # Side Lamp
   sun = bpy.data.lamps.new('MyLamp9','POINT')
   sun.use_specular = False
   sun.energy = .6*intensity
   sunobj = bpy.data.objects.new(name='MyLamp10', object_data=sun)
   sunobj.location = -4.0, -0.0, 1.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.0, 0.0
   scn.objects.link(sunobj)

   # Overhead Lamp
   sun = bpy.data.lamps.new('MyLamp11','POINT')
   sun.energy = .8*intensity
   sunobj = bpy.data.objects.new(name='MyLamp12', object_data=sun)
   sunobj.location = 0.0, 0.0, 12.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.0, 0.0
   scn.objects.link(sunobj)

   # Test Sun
   sun = bpy.data.lamps.new('MyLamp13','SUN')
   sun.use_specular = False
   sun.energy = .48*intensity
   sunobj = bpy.data.objects.new(name='MyLamp14', object_data=sun)
   sunobj.location = 0.0, 0.0, 25.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.0, 0.0
   scn.objects.link(sunobj)

   # Overhead Hemi
   sun = bpy.data.lamps.new('MyLamp15','HEMI')
   sun.use_specular = False
   sun.energy = .2*intensity
   sunobj = bpy.data.objects.new(name='MyLamp16', object_data=sun)
   sunobj.location = 9.0, -9.0, 18.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.61086, -0.78539
   scn.objects.link(sunobj)

   # set the rendering context up
   ctxt.image_settings.file_format = 'PNG';
   ctxt.image_settings.color_mode = 'RGBA';
   ctxt.alpha_mode = 'PREMUL'
   ctxt.resolution_x = resolution
   ctxt.resolution_y = resolution
   ctxt.threads = 5
   ctxt.use_antialiasing = True
   ctxt.filepath = os.getcwd() + "/"

if __name__ == "__main__":
   Initialize()
