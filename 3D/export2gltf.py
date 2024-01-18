import os
import subprocess
import bpy
import shutil

OUTPATH = "gltf"

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

shipdir = os.path.abspath(os.path.join(OUTPATH, shipname))
os.makedirs(shipdir, exist_ok=True)
gltfpath = os.path.join(shipdir, shipname) + '.gltf'
bpy.ops.file.unpack_all()

# Modernize some stuff
scn = bpy.context.scene
scn.render.engine = 'CYCLES'
scn.cycles.feature_set = 'SUPPORTED'
scn.render.use_bake_multires = False
scn.cycles.bake_type = 'NORMAL'
scn.render.bake.use_selected_to_active = False

# Get rid of stuff
for obj in bpy.data.objects:
    if obj.type!="MESH":
        obj.select_set(True)
    else:
        obj.select_set(False)
bpy.ops.object.delete()

for mat in bpy.data.materials:
     mat.use_backface_culling = True

def remove_dups():
    bpy.ops.object.convert(target='MESH') # Here I've added an option which will
                                    # apply all modifiers by converting object
                                    # to mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles( threshold = 0.001 )
    bpy.ops.mesh.tris_convert_to_quads()
    bpy.ops.mesh.normals_make_consistent()
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type = 'FACE')
    bpy.ops.mesh.select_interior_faces()
    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.object.mode_set(mode='OBJECT')

# Unselect all
for obj in bpy.data.objects:
    obj.select_set(False)

# Collection 1 should contain the main ship (old format)
for obj in bpy.data.collections['Collection 1'].all_objects:
    if obj.type!="MESH":
        continue

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    remove_dups()

    # Bake ambient occlusion
    size = 512
    samples = 128
    scn = bpy.context.scene
    scn.cycles.adaptive_threshold = 0.005
    scn.cycles.samples = samples
    scn.cycles.adaptive_min_samples = int(samples / 2)
    #bpy.ops.object.bake( 'INVOKE_DEFAULT', type='AO', width=size, height=size, save_mode="EXTERNAL", use_automatic_name=True, use_split_materials=True, pass_filter={'COLOR'}, cage_extrusion=1, max_ray_distance=0 )
bpy.ops.object.join()
remove_dups()

# Rename object
obj = bpy.context.active_object
obj.name = "body"
obj.data.name = "body"

# Collection 9 should contain the engine
if "Collection 9" in bpy.data.collections.keys():
    # Deselect all first
    for obj in bpy.data.objects:
        obj.select_set(False)
    for obj in bpy.data.collections['Collection 9'].all_objects:
        if obj.type!="MESH":
            continue
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        remove_dups()
    bpy.ops.object.join()
    remove_dups()

    # Rename object
    obj = bpy.context.active_object
    obj.name = "engine"
    obj.data.name = "engine"

# Finally export the entire scene
bpy.ops.export_scene.gltf( filepath=gltfpath, export_format='GLTF_SEPARATE', export_lights=False, export_cameras=False, export_normals=True )

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
