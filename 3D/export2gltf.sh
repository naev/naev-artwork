#!/bin/bash

if [ -z "$1" ]
then
   for i in ships/*.blend
   do
      $0 $i
   done
else
   TMPFILE=`mktemp --suffix '.blend'`
   blender-2.7 $1 -b -P materials_cycles_converter.py -- $TMPFILE
   blender $TMPFILE -b -P export2gltf.py -- $1
   #blender $1 -b -P export2gltf.py
fi
