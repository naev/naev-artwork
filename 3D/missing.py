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
    if et.find('GFX') == None:
        print('No GFX tag in \'' + i + '\'')
        continue
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

# Similarly to outfits.
missing = set()
for i in os.listdir(DAT + 'gfx/planet/space'):
    if i.endswith('.png'):
        if not os.path.exists('stations/' + i.replace('.png', '.blend')):
            if not os.path.exists('../2D/planet/space/' + i.replace('.png', '.psd')):
                missing.add(i)
print_missing("Planets Space", missing)

missing = set()
for i in os.listdir(DAT + 'gfx/logo'):
    if not i.endswith('_small.png'):
        continue
    faction = i.replace('_small.png', '')
    if not os.path.exists('../2D/logo/' + faction + '.svg'):
        missing.add(faction)
print_missing("Faction Logos", missing)
