#/usr/bin/env python

import math
import sys

#sys.path.append( '/home/softcoder/Code/naev-artwork/3D' )
import render_init
import render_comm

import optparse
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
            obj.rotation_euler[2] = obj.rotation_euler[2] + (options.rotation_euler[2] / 180. * math.pi)

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

   # Set sprites to use.
   sx = 6
   if options.sx:
      sx = options.sx
   if options.sy:
      sy = options.sy
   else:
      sy = sx

   # Set intensity
   intensity = 1.
   if options.intensity:
      intensity = options.intensity
   resolution = 512
   if options.resolution:
      resolution = options.resolution

   if options.layers:
      layers = options.layers

   # Set up layers if needed
   if options.engine == "true":
      for i in range(9):
            bpy.context.scene.layers[i] = True
   if options.layers:
      layerlist = ( [1, 2, 3, 4, 5, 6, 7, 8] )
      layers = layers.split()
      layers=map(int, layers)
      layerlist.extend(layers)
      for i in layerlist:
            bpy.context.scene.layers[i] = True
   else:
      for i in range(8):
            bpy.context.scene.layers[i] = True

   # Use the comm render script if necessary.
   if options.comm == "1":
      render_comm.Initialize( intensity, resolution )
   else:
      render_init.Initialize( intensity, resolution )

   Render( sx, sy )
   bpy.ops.wm.quit_blender()
