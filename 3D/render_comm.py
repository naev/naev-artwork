#/usr/bin/env python

import math
import Blender

import render_init


#
#  global variables
#
filename = Blender.Get('filename')
scn = Blender.Scene.GetCurrent() # global scene
ctxt = scn.getRenderingContext()


def Initialize():
   # unlink stuff we don't want
   for obj in Blender.Object.Get(): # destroy old cameras
      if obj.getType() in ('Camera','Lamp'):
         scn.objects.unlink(obj)

   # set the camera up
   cam = Blender.Camera.New('persp')
   camobj = Blender.Object.New('Camera')
   camobj.link(cam)
   camobj.LocX = 0.5
   camobj.LocY = -10.
   camobj.LocZ = 0.5
   camobj.RotX = 1.518
   camobj.RotY = 0.
   camobj.RotZ = 0.052
   scn.objects.link(camobj)
   scn.objects.camera = camobj

   # Top Right Spot
   sun = Blender.Lamp.New('Spot')
   sun.setEnergy( 2.8 )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 25.
   sunobj.LocY = -25. / math.sqrt(2)
   sunobj.LocX = 25. / math.sqrt(2)
   sunobj.RotY =  0.78539
   sunobj.RotZ = - 0.78539
   scn.objects.link(sunobj)

   # Top Left Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( 1.68 )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 25.
   sunobj.LocY = -25. / math.sqrt(2)
   sunobj.LocX = -25. / math.sqrt(2)
   sunobj.RotY =  0.78539
   sunobj.RotZ = -2.35619
   scn.objects.link(sunobj)
   
   # Bottom Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( 0.42 )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = -10.
   sunobj.LocY = -25. / math.sqrt(2)
   sunobj.LocX = 0.
   sunobj.RotX = 1.0471
   sunobj.RotY = 3.14159
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)


def Render():
   ctxt.render()
   ctxt.saveRenderedImage( "comm.png" )


if __name__ == "__main__":
   render_init.Initialize()
   Initialize()
   Render()
   Blender.Quit()
