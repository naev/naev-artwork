#!/usr/bin/env python

import os
from xml.etree import ElementTree
import subprocess

DAT = subprocess.check_output('./naevpath.sh').decode().strip('\n') + '/dat/'

def print_missing(name, items):
    if len(items) == 0:
        print("No Missing " + name)
    else:
        print(name)
        for i in items:
            print('* ' + i)
    print()

missing = set()
for i in os.listdir(DAT + 'ships'):
    if not i.endswith('.xml'):
        continue
    et = ElementTree.parse(DAT + 'ships/' + i)
    gfx = et.find('GFX').text
    if not os.path.exists('ships/' + gfx + '.blend'):
        missing.add(gfx)
print_missing("Ships", missing)

# Most are not really missing since they may not be based on 3D sources.
# But it would be good to have the 2D sources as well.
missing = set()
for i in os.listdir(DAT + 'outfits'):
    for j in os.listdir(DAT + 'outfits/' + i):
        et = ElementTree.parse(DAT + 'outfits/' + i + '/' + j)
        gfx = et.find('general').find('gfx_store').text
        if not os.path.exists('outfits/' + gfx + '.blend'):
            missing.add(gfx)
print_missing("Outfits", missing)

missing = set()
for i in os.listdir(DAT + 'gfx/logo'):
    if not i.endswith('_small.png'):
        continue
    faction = i.replace('_small.png', '')
    if not os.path.exists('../logos/' + faction + '.svg'):
        missing.add(faction)
print_missing("Faction Logos", missing)
