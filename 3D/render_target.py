#/usr/bin/env python

import math
import Blender


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
   cam = Blender.Camera.New('ortho')
   camobj = Blender.Object.New('Camera')
   camobj.link(cam)
   camobj.LocX = 7.
   camobj.LocY = 0.
   camobj.LocZ = 0.
   camobj.RotX = math.pi/2.
   camobj.RotY = 0.
   camobj.RotZ = math.pi/2.
   scn.objects.link(camobj)
   scn.objects.camera = camobj

   # set lighting up
   sun = Blender.Lamp.New('Spot')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( 4 )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 25.
   sunobj.LocY = -25. / math.sqrt(2)
   sunobj.LocX = 25. / math.sqrt(2)
   sunobj.RotY = 45.
   sunobj.RotZ = -45.
   scn.objects.link(sunobj)

   # set the rendering context up
   ctxt.extensions = True
   ctxt.setImageType(Blender.Scene.Render.PNG)
   ctxt.enablePremultiply()
   ctxt.enableRGBAColor()
   ctxt.imageSizeX(512)
   ctxt.imageSizeY(512)
   ctxt.threads = 3
   ctxt.OSALevel = 8
   ctxt.oversampling = True
   ctxt.renderPath = os.getcwd() + "/"


if __name__ == "__main__":
   Initialize()
