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

You can also automatically generate all the images using the provided Makefile
with:

```sh
make
``
