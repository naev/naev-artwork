#/usr/bin/env python

import math
import Blender


if __name__ == "__main__":
   Blender.PackAll()

   filename = Blender.Get('filename')
   Blender.Save(filename, 1)

   Blender.Quit()
