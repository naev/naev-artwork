#/usr/bin/env python

import math
import Blender
import os


def Initialize( intensity=1. ):
   # variables to use
   scn = Blender.Scene.GetCurrent() # global scene
   ctxt = scn.getRenderingContext()
   print("Intensity " + str(intensity))

   # unlink stuff we don't want
   for obj in Blender.Object.Get(): # destroy old cameras
      if obj.getType() in ('Camera','Lamp'):
         scn.objects.unlink(obj)

   # set the camera up
   cam = Blender.Camera.New('ortho')
   cam.scale = 10.
   camobj = Blender.Object.New('Camera')
   camobj.link(cam)
   camobj.LocZ = 9.
   camobj.LocX = -9.
   camobj.LocY = 0.
   camobj.RotX = math.pi / 4.
   camobj.RotY = 0.
   camobj.RotZ = - math.pi / 2.
   scn.objects.link(camobj)
   scn.objects.camera = camobj

   # Overhead Spot
   sun = Blender.Lamp.New('Area')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( .4*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 14.
   sunobj.LocY = -9.
   sunobj.LocX = 9.
   sunobj.RotY = math.pi / 4.
   sunobj.RotZ = - math.pi / 4.
   scn.objects.link(sunobj)
   
   # Forward Upper Spot
   sun = Blender.Lamp.New('Spot')
   sun.setEnergy( .32*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 7.
   sunobj.LocY = -15.
   sunobj.LocX = 0.
   sunobj.RotX = 1.13446
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)
   
   # Forward Lower Spot
   sun = Blender.Lamp.New('Spot')
   sun.setEnergy( .64*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = -7.
   sunobj.LocY = -15.
   sunobj.LocX = 0.
   sunobj.RotX = 2.00712
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)
   
   # Forward Middle Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.setEnergy( .08*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = -3.5
   sunobj.LocY = -15.
   sunobj.LocX = 0.
   sunobj.RotX = 1.57079
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)
   
   # Back Middle Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.setEnergy( .08*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = -3.5
   sunobj.LocY = 15.
   sunobj.LocX = 0.
   sunobj.RotX = 4.71238
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)
   
   # Left Middle Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.setEnergy( .08*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = -3.5
   sunobj.LocY = 0.
   sunobj.LocX = -15.
   sunobj.RotX = 0.
   sunobj.RotY = 1.57079
   sunobj.RotZ = 3.14159
   scn.objects.link(sunobj)

   # Right Middle Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.setEnergy( .08*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = -3.5
   sunobj.LocY = 0.
   sunobj.LocX = 15.
   sunobj.RotX = 0.
   sunobj.RotY = -1.57079
   sunobj.RotZ = 3.14159
   scn.objects.link(sunobj)

   # Side Lamp
   sun = Blender.Lamp.New('Lamp')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( .6*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 1.
   sunobj.LocY = -0.
   sunobj.LocX = -4.
   sunobj.RotX = 0.
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)

   # Overhead Lamp
   sun = Blender.Lamp.New('Lamp')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( .8*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 12.
   sunobj.LocY = 0.
   sunobj.LocX = 0.
   sunobj.RotX = 0.
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)
   
      # Test Sun
   sun = Blender.Lamp.New('Sun')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( .48*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 25.
   sunobj.LocY = 0.
   sunobj.LocX = 0.
   sunobj.RotX = 0.
   sunobj.RotY = 0.
   sunobj.RotZ = 0.
   scn.objects.link(sunobj)

   # Overhead Hemi
   sun = Blender.Lamp.New('Hemi')
   sun.mode |= Blender.Lamp.Modes["NoSpecular"]
   sun.setEnergy( .2*intensity )
   sunobj = Blender.Object.New('Lamp')
   sunobj.link(sun)
   sunobj.LocZ = 18.
   sunobj.LocY = -9.
   sunobj.LocX = 9.
   sunobj.RotY = 0.61086
   sunobj.RotZ = -0.78539
   scn.objects.link(sunobj)

   # set the rendering context up
   ctxt.extensions = True
   ctxt.setImageType(Blender.Scene.Render.PNG)
   ctxt.enablePremultiply()
   ctxt.enableRGBAColor()
   ctxt.imageSizeX(512)
   ctxt.imageSizeY(512)
   ctxt.threads = 5
   ctxt.OSALevel = 8
   ctxt.oversampling = True
   ctxt.renderPath = os.getcwd() + "/"


if __name__ == "__main__":
   Initialize()

