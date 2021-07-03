#!/usr/bin/env python
from functools import reduce
import os
import subprocess
import sys
import tempfile

_, in_path, max_dimension, out_path = sys.argv
w = float(subprocess.check_output(['inkscape', '-W', in_path]))
h = float(subprocess.check_output(['inkscape', '-H', in_path]))
f = float(max_dimension) / max(w, h)
tmp_fd, tmp_path = tempfile.mkstemp('.png')
os.close(tmp_fd)
subprocess.check_call(['inkscape', '--export-area-drawing',
                       '-w', str(round(w*f)),
                       '-h', str(round(h*f)), in_path,
                       '-o', tmp_path])
subprocess.check_call(['convert', '-trim', '+repage', tmp_path, out_path])
