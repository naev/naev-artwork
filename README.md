Artwork for Naev
================

**IMPORTANT**: Since render.sh is subject to change, the path to the output repo (naev-artwork-production) is grabbed from `3D/naevpath.sh`. Copy `3D/naevpath.sh.example` to `3D/naevpath.sh` and edit it to point to your NAEV Git checkout.

**WARNING**: The .sh files within `3D/` are subject to change, and being that they can contain user-specific data, it's wise to back them up.

Directories
-----------
* `.gitignore` by default will not commit 3D/raw or 3D/final, as they merely contain renders.
* `ships/`  -  This directory contains all of the current .blends. Ships go on layer 1, and their engine meshes go on layer 9.
* `ships/legacy` - This is a legacy directory, containing unused ships and texture variants. Since the current .blends are resized and repositioned, it's likely best to just take the textures from these and apply them to current .blends (in ships/). The files are gzipped for size, but Blender can read them without issue.
* `outfits/`
   - For the laser, only the base .blend is included. The Mk2 is created by merely increasing the muzzle size by 20% and changing the heatsink near the base to a green material.
   - The launcher graphics were created by combining the missile .blends with a desaturated Banshee launcher.
   - For creating your own graphics, turret.blend and turret2.blend are included. They're not actually used in-game, but they are the basis for the other turret models.

Rendering
---------
For an overview, see http://code.google.com/p/naev/wiki/HowtoGraphics

### Ship rendering

Ship rendering isn't an overly difficult task in NAEV. All ship sprites are based on Blender models, rendered with our scripts.

**Note**: Ships aren't automatically resized. To gauge size, open `examples/lighting-and-camera.blend` and import your meshes. An ideal size nearly touches the edge, such that there's minimal wasted space on the sprite.

#### Rendering steps
**Note**: This is for rendering one ship (or select ships). If you wish to do everything at once, running render.sh and dim.sh without arguments will do that.

1. Once you have a ship you wish to render, place it in `3D/ships` and add two entries for it to `3D/dim.sh` - One for the number of sprites, and one for the size of each sprite cell.
2. When you've done that, you can run render.sh with your ship's name as an argument, such as `./render.sh admonisher`
3. With the render finished, you can run `./resize.sh`  which will resize the sprite to a usable size, as defined in `dim.sh`

#### Using your ship

**Note**: Step 2 can be automated, if you edit `naev/gfx/ship/update.sh` to include your sprite locations.
      
1. Give the sprite an entry in `naev/dat/ship.xml`
2. Place the sprites in `naev/gfx/ship/$ship/` as you've defined in `ship.xml`
3. To ensure the best appearance, you should manually define mount points. This is done in pixels based on the first sprite frame.
4. Give the ship a target graphic, and you're done.

### Weapon sprite rendering
Given the small size of weapon sprites, they can often be 2D-based without looking out of place. If you want a 3D-based weapon sprite, see the ship rendering instructions.
      
**Note**: This assumes you're using GIMP, which is what the sprite-making script is written for.
      
1. Orient your 2D graphic such that the front of the projectile points due East.
2. Save the image and run `utils/gimp/mksprite` on it.
3. In order to use your sprite, place it in `gfx/outfit/space` and make a weapon in `outfit.xml` use it.
