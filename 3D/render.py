#/usr/bin/env python2.7

import math
import sys

#import render_init
#import render_comm

import optparse
import bpy
import os

#
#  global variables
#
#filename = os.path.basename(bpy.data.filepath)
scn = bpy.context.scene
ctxt = scn.render

def InitializeNormal( intensity=1., resolution=512 ):
   # variables to use
   scn = bpy.context.scene
   ctxt = scn.render

   # unlink stuff we don't want
   for obj in bpy.data.objects:
      if obj.type in ('CAMERA','LAMP'):
         scn.objects.unlink(obj)
   scn.update()

   # set the camera up
   cam = bpy.data.cameras.new('ORTHO')
   cam.type = 'ORTHO'
   cam.ortho_scale = 10.
   camobj = bpy.data.objects.new(name="Camera1", object_data=cam)
   camobj.location = -9.0, 0.0, 9.0
   camobj.rotation_mode = 'XYZ'
   camobj.rotation_euler = math.pi / 4., 0.0, -math.pi / 2.
   scn.objects.link(camobj)
   scn.update()
   scn.camera = camobj

   # Overhead Spot
   sun = bpy.data.lamps.new('Area1','AREA')
   sun.use_specular = False
   sun.energy = .4*intensity
   sunobj = bpy.data.objects.new(name='MyLamp1', object_data=sun)
   sunobj.location = 9.0, -9.0, 14.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, math.pi / 4., - math.pi / 4.

   scn.objects.link(sunobj)
   scn.update()
   
   # Forward Upper Spot
   sun = bpy.data.lamps.new('Spot1','SPOT')
   sun.energy = .32*intensity
   sunobj = bpy.data.objects.new(name='MyLamp2', object_data=sun)
   sunobj.location = 0.0, -15.0, 7.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 1.13446, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Forward Lower Spot
   sun = bpy.data.lamps.new('Spot2','SPOT')
   sun.energy = .64*intensity
   sunobj = bpy.data.objects.new(name='MyLamp3', object_data=sun)
   sunobj.location = 0.0, -15.0, -7.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 2.00712, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Forward Middle Hemi
   sun = bpy.data.lamps.new('Hemi1','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp4', object_data=sun)
   sunobj.location = 0.0, -15.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 1.57079, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Back Middle Hemi
   sun = bpy.data.lamps.new('Hemi2','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp5', object_data=sun)
   sunobj.location = 0.0, -15.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 4.71238, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
   # Left Middle Hemi
   sun = bpy.data.lamps.new('Hemi3','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp6', object_data=sun)
   sunobj.location = -15.0, 0.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 1.57079, 3.14159
   scn.objects.link(sunobj)
   scn.update()

   # Right Middle Hemi
   sun = bpy.data.lamps.new('Hemi4','HEMI')
   sun.energy = .08*intensity
   sunobj = bpy.data.objects.new(name='MyLamp7', object_data=sun)
   sunobj.location = 15.0, 0.0, -3.5
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, -1.57079, 3.14159
   scn.objects.link(sunobj)
   scn.update()

   # Side Lamp
   sun = bpy.data.lamps.new('Lamp8','POINT')
   sun.use_specular = False
   sun.energy = .6*intensity
   sunobj = bpy.data.objects.new(name='MyLamp9', object_data=sun)
   sunobj.location = -4.0, -0.0, 1.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()

   # Overhead Lamp
   sun = bpy.data.lamps.new('Lamp10','POINT')
   sun.energy = .8*intensity
   sunobj = bpy.data.objects.new(name='MyLamp11', object_data=sun)
   sunobj.location = 0.0, 0.0, 0.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()
   
      # Test Sun
   sun = bpy.data.lamps.new('Lamp12','SUN')
   sun.use_specular = False
   sun.energy =.48*intensity
   sunobj = bpy.data.objects.new(name='MyLamp12', object_data=sun)
   sunobj.location = 0.0, 0.0, 25.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.0, 0.0
   scn.objects.link(sunobj)
   scn.update()

   # Overhead Hemi
   sun = bpy.data.lamps.new('Lamp13','HEMI')
   sun.use_specular = False
   sun.energy = .2*intensity
   sunobj = bpy.data.objects.new(name='MyLamp13', object_data=sun)
   sunobj.location = 9.0, -9.0, 18.0
   sunobj.rotation_mode = 'XYZ'
   sunobj.rotation_euler = 0.0, 0.61086, -0.78539
   scn.objects.link(sunobj)
   scn.update()

   # set the rendering context up
   ctxt.image_settings.file_format = 'PNG';
   ctxt.image_settings.color_mode = 'RGBA';
   #ctxt.alpha_mode = 'TRANSPARENT'
   ctxt.alpha_mode = 'SKY'
   ctxt.resolution_x = resolution
   ctxt.resolution_y = resolution
   ctxt.threads = 5
   ctxt.use_antialiasing = True
   ctxt.filepath = os.getcwd() + "/"


def InitializeComm( intensity=1., resolution=512 ):
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
   #ctxt.alpha_mode = 'TRANSPARENT'
   ctxt.alpha_mode = 'SKY'
   ctxt.resolution_x = resolution
   ctxt.resolution_y = resolution
   ctxt.threads = 5
   ctxt.use_antialiasing = True
   ctxt.filepath = os.getcwd() + "/"


#
# Renders the 36 sprites with names like 000.png, 001.png, ...
#
def Render( sx, sy ):
   total = sx*sy
   for i in range(0,total):
      for obj in bpy.data.objects:
         obj.rotation_mode = 'XYZ'
         if i != 0 and obj.type in ['MESH','EMPTY']:
            obj.rotation_euler[2] = obj.rotation_euler[2] + ((math.pi * 2) / total)
         elif obj.type in ['MESH','EMPTY'] and options.rotz:
            obj.rotation_euler[2] = obj.rotation_euler[2] + (options.rotz / 180. * math.pi)

      ctxt.filepath = str(i).zfill(3)+".png"
      ctxt.use_file_extension = True
      bpy.ops.render.render(write_still=True)

#
# Actual commands to run.
#
if __name__ == "__main__":
   # get the args passed to blender after "--", all of which are ignored by blender specifically
   # so python may receive its own arguments
   argv= sys.argv

   if '--' not in argv:
      argv = [] # as if no args are passed
   else:
      argv = argv[argv.index('--')+1: ] # get all args after "--"

   # When --help or no args are given, print this help
   usage_text =  'Run blender in background mode with this script:\n'
   usage_text += '  blender -b -P ' + "render.py" + ' -- [options]'

   parser = optparse.OptionParser(usage = usage_text)

   # Example background utility, add some text and renders or saves it (with options)
   # Possible types are: string, int, long, choice, float and complex.
   parser.add_option('-x', '--spritex', dest='sx', help='X sprites to render.', type='int')
   parser.add_option('-y', '--spritey', dest='sy', help='Y sprites to render.', type='int')
   parser.add_option('-e', '--engine', dest='engine', help='Enable engine glow on layer 9.', type='string')
   parser.add_option('-i', '--intensity', dest='intensity', help="Controls the intensity level.", type='float')
   parser.add_option('-l', '--layer', dest='layers', help='Enable rendering of arbitrary layers.', type='string')
   parser.add_option('-r', '--rotz', dest='rotz', help="Begins render with arbitrary Z rotation.", type='float')
   parser.add_option('-R', '--resolution', dest='resolution', help="Renders at an arbitrary resolution.", type='int')
   parser.add_option('-c', '--comm', dest='comm', help="Renders using the comm camera.", type='int')

   options, args = parser.parse_args(argv) # In this example we wont use the args
   sx = options.sx or 8
   sy = options.sy or sx
   intensity = options.intensity or 1.
   resolution = options.resolution or 512

   # Disable layers 1-9 by default.
   for i in range(8,19):
      bpy.context.scene.layers[i] = False

   if options.engine == 'true':
      bpy.context.scene.layers[8] = True

   if options.layers:
      for i in range(8):
         bpy.context.scene.layers[i] = True
      for i in map(int, options.layers.split()):
         bpy.context.scene.layers[i] = True

   # Use the comm render script if necessary.
   if options.comm == 1:
      InitializeComm( intensity, resolution )
   else:
      InitializeNormal( intensity, resolution )

   Render( sx, sy )
   bpy.ops.wm.quit_blender()
