import os
import subprocess
import bpy
import shutil

textures_dir = os.path.dirname(bpy.data.filepath) + '/textures'
if os.path.exists(textures_dir):
    shutil.rmtree(textures_dir)

shipname = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
shipdir = os.path.abspath(os.path.join('3d', shipname))
os.makedirs(shipdir, exist_ok=True)
objpath = os.path.join(shipdir, shipname) + '.obj'
gltfpath = os.path.join(shipdir, shipname) + '.gltf'
bpy.ops.file.unpack_all()

bpy.context.scene.layers[0] = True
bpy.context.scene.layers[8] = True

bpy.ops.object.select_by_layer(layers=1)
bpy.context.scene.objects.active = [i for i in bpy.context.selected_objects if i.type=='MESH'][0]
bpy.ops.object.join()
bpy.context.scene.objects.active.name = 'body'
bpy.context.scene.objects.active.data.name = 'body'

bpy.ops.object.select_by_layer(layers=9)
bpy.context.scene.objects.active = [i for i in bpy.context.selected_objects if i.type=='MESH'][0]
bpy.ops.object.join()
bpy.context.scene.objects.active.name = 'engine'
bpy.context.scene.objects.active.data.name = 'engine'

bpy.ops.export_scene.obj(filepath=objpath, use_triangles=True, path_mode='COPY')

os.chdir(shipdir)
with open(shipname + '.mtl') as mtlfile:
    mtltext = mtlfile.read()

for i in os.listdir():
    name, ext = os.path.splitext(i)
    if ext not in ('.obj', '.mtl', '.png'):
        oldname, ext, i = i, '.png', f'{name}.png'
        print(f'Converting {oldname} to {i}...')
        subprocess.call(['convert', oldname, i])
        os.unlink(oldname)
        mtltext = mtltext.replace(oldname, i)
    """
    if ext == '.png':
        oldname, ext, i = i, '.webp', f'{name}.webp'
        print(f'Converting {oldname} to {i}...')
        subprocess.call(['cwebp', '-lossless', '-z', '9', oldname, '-o', i])
        os.unlink(oldname)
        mtltext = mtltext.replace(oldname, i)
    """

with open(shipname + '.mtl', 'w') as mtlfile:
    mtlfile.write(mtltext)

"""
bpy.ops.export_scene.gltf(filepath=gltfpath, export_format='GLTF_SEPARATE', export_lights=False, export_cameras=False )
"""
