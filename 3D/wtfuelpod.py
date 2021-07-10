#!/usr/bin/env python

from PIL import Image
import subprocess

def enlarge(single, out_name):
    double = Image.new('RGBA', single.size)
    double.alpha_composite(single, ((-3*single.width)//128, (0*single.height)//128))
    double.alpha_composite(single, (( 5*single.width)//128, (8*single.height)//128))
    double.save(f'{out_name}.png')
    subprocess.check_call(['cwebp', '-z', '9', f'{out_name}.png', '-o', f'{out_name}.webp'])
    return double

fuel1 = Image.open('../out/outfits/fueltank.webp')
fuel2 = enlarge(fuel1, '../out/outfits/medium_fuel_pod')
fuel3 = enlarge(fuel2, '../out/outfits/large_fuel_pod')
