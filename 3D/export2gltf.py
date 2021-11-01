import os
import subprocess
import bpy
import shutil

textures_dir = os.path.dirname(bpy.data.filepath) + '/textures'
if os.path.exists(textures_dir):
    shutil.rmtree(textures_dir)

import sys
argv = sys.argv
if "--" in argv:
    argv = argv[argv.index("--") + 1:]  # get all args after "--"
    filename = argv[0]
else:
    filename = bpy.data.filepath
shipname = os.path.splitext(os.path.basename(filename))[0]

shipdir = os.path.abspath(os.path.join('3d', shipname))
os.makedirs(shipdir, exist_ok=True)
gltfpath = os.path.join(shipdir, shipname) + '.gltf'
bpy.ops.file.unpack_all()

# Get rid of stuff
for obj in bpy.data.objects:
    if obj.type!="MESH":
        obj.select_set(True)
    else:
        obj.select_set(False)
bpy.ops.object.delete()

#bpy.context.scene.layers[0] = True
#bpy.context.scene.layers[8] = True

#bpy.data.collections['Collection 1'].hide_viewport = False
#bpy.data.collections['Collection 9'].hide_viewport = True

def remove_dups():
    bpy.ops.object.convert(target='MESH') # Here I've added an option which will
                                    # apply all modifiers by converting object
                                    # to mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles( threshold = 0.001 )
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type = 'FACE')
    bpy.ops.mesh.select_interior_faces()
    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.object.mode_set(mode='OBJECT')


for obj in bpy.data.objects:
    obj.select_set(False)
for obj in bpy.data.collections['Collection 1'].all_objects:
    if obj.type=="MESH":
        obj.select_set(True)
        obj.name = "body"
        obj.data.name = "body"
        bpy.context.view_layer.objects.active = obj
        remove_dups()

#bpy.ops.object.select_by_layer(layers=1)
#bpy.context.scene.objects.active = [i for i in bpy.context.selected_objects if i.type=='MESH'][0]
bpy.ops.object.join()
remove_dups()
#bpy.context.scene.objects.active.name = 'body'
#bpy.context.scene.objects.active.data.name = 'body'

if "Collection 9" in bpy.data.collections.keys():
    for obj in bpy.data.objects:
        obj.select_set(False)
    for obj in bpy.data.collections['Collection 9'].all_objects:
        if obj.type=="MESH":
            obj.select_set(True)
            obj.name = "engine"
            obj.data.name = "engine"
            bpy.context.view_layer.objects.active = obj
            remove_dups()
#bpy.ops.object.select_by_layer(layers=9)
#bpy.context.scene.objects.active = [i for i in bpy.context.selected_objects if i.type=='MESH'][0]
    bpy.ops.object.join()
    remove_dups()
#bpy.context.scene.objects.active.name = 'engine'
#bpy.context.scene.objects.active.data.name = 'engine'

bpy.ops.export_scene.gltf(filepath=gltfpath, export_format='GLTF_SEPARATE', export_lights=False, export_cameras=False )

"""
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

with open(shipname + '.mtl', 'w') as mtlfile:
    mtlfile.write(mtltext)
"""
