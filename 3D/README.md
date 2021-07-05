## Naev 3D Rendering scripts

The scripts here are horribly broken and need major updating to newer versions.
That said, it is possible to manually render ships using the render.py script
using Ubuntu 12.04's blender. This can be installed using debootstrap as follows:

```sh
sudo debootstrap --no-check-gpg --variant=buildd precise /opt/ubuntu1204 http://archive.ubuntu.com/ubuntu/
```

To compile mkspr and run the scripts you will need the following packages:

```sh
apt-get install blender libpng-dev libsdl-image1.2-dev
```

Afterwards set up schroot to enter the new chroot and install blender. You
should be able to run the scripts as below:

```sh
blender ships/hyena.blend -P ./render.py
```

You can also set parameters such as number of x and y sprites with the following parameters:

```
  -h, --help            show this help message and exit
  -x SX, --spritex=SX   X sprites to render.
  -y SY, --spritey=SY   Y sprites to render.
  -e ENGINE, --engine=ENGINE
                        Enable engine glow on layer 9.
  -i INTENSITY, --intensity=INTENSITY
                        Controls the intensity level.
  -l LAYERS, --layer=LAYERS
                        Enable rendering of arbitrary layers.
  -r ROTZ, --rotz=ROTZ  Begins render with arbitrary Z rotation.
  -R RESOLUTION, --resolution=RESOLUTION
                        Renders at an arbitrary resolution.
  -c COMM, --comm=COMM  Renders using the comm camera.
```

For example, the following would render a ship with a 12x12 sprite sheet where each sprite is 128 by 128 pixels you can do:

```sh
blender ships/hyena.blend -P ./render.py -- -x 12 -y 12 -R 128
```

You can also automatically generate all the images using the provided `render.sh` script:

```sh
./render.sh
```

## Outfits

I don't know how to export the Blender files in outfits/ correctly. (Viktor has mostly made it work.)
If you can do it, you can use `wtfuelpod.py` to generate a medium fuel pod from an exported `fueltank` image.
Does this method make sense? Not really, but it perfectly mimics the way `medium_fuel_pod.png` was originally generated.
The older `large_fuel_pod.png` appears to be a new model by <ids1024>, though maybe it was just image-edited. The script just
generates a triple-tank for that one, using the same effect.

The transformation from green to purple "capacitor" images can be done via `convert -modulate 100,100,0 capacitor.webp capacitor-g.webp` and the like.
