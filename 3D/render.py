#/usr/bin/env python

import math
import Blender

import render_init

import sys
import optparse


#
#  global variables
#
filename = Blender.Get('filename')
scn      = Blender.Scene.GetCurrent() # global scene
ctxt     = scn.getRenderingContext()


#
# Renders the 36 sprites with names like 000.png, 001.png, ...
#
def Render( sx, sy ):
   total = sx*sy
   for i in range(0,total):
      for obj in Blender.Object.Get():
         if i != 0 and obj.getType() in ['Mesh','Empty']:
            obj.RotZ = obj.RotZ + ((math.pi * 2) / total)
         elif obj.getType() in ['Mesh','Empty'] and options.rotz:
           obj.RotZ = obj.RotZ + (options.rotz / 180. * math.pi)

      ctxt.render()
      ctxt.saveRenderedImage( str(i).zfill(3)+".png" )

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
   parser.add_option('-l', '--layers', dest='layers', help='Enable rendering of arbitrary layers.', type='string')
   parser.add_option('-r', '--rotz', dest='rotz', help="Begins render with arbitrary Z rotation.", type='float')

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

   if options.layers:
      layers = options.layers

   # Set up layers if needed
   if options.engine == "true":
      Blender.Window.ViewLayers( [1, 2, 3, 4, 5, 6, 7, 8, 9] )
   if options.layers:
      layerlist = ( [1, 2, 3, 4, 5, 6, 7, 8] )
      layers = layers.split()
      layers=map(int, layers)
      layerlist.extend(layers)
      Blender.Window.ViewLayers(layerlist)
   else:
      Blender.Window.ViewLayers( [1, 2, 3, 4, 5, 6, 7, 8] )

   render_init.Initialize( intensity )
   Render( sx, sy )
   Blender.Quit()

