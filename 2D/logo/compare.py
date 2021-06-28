#!/usr/bin/env python
import os
import subprocess

subprocess.check_call(['make'])
roots = ['../../../naev/dat/gfx/logo/', '../../out/logo/']
fns = [os.path.join(mid, name) for top in roots for (mid, _, names) in os.walk(top) for name in names]
fns.sort(key = lambda s: s[::-1])
subprocess.check_call([
    'feh',
    '--draw-filename', '--draw-tinted',
    '--fullscreen',
    '--image-bg', 'checks',
    '--zoom', '1600',
] + fns)
