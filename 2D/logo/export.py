#!/usr/bin/env python
from functools import reduce
from lxml import etree
import os
import subprocess
import string
import sys
import tempfile

_, in_path, max_dimension, out_path = sys.argv
attributes = etree.parse(open(in_path)).getroot().attrib
w = float(attributes['width' ].rstrip(string.ascii_letters))
h = float(attributes['height'].rstrip(string.ascii_letters))
f = float(max_dimension) / max(w, h)
tmp_fd, tmp_path = tempfile.mkstemp('.png')
os.close(tmp_fd)
subprocess.check_call(['inkscape',
                       '-w', str(round(w*f)),
                       '-h', str(round(h*f)), in_path,
                       '-o', tmp_path])
subprocess.check_call(['convert', '-trim', '+repage', tmp_path, out_path])
