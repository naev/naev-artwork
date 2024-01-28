#!/bin/bash

if [ -z "$1" ]
then
   for i in ships/*.blend
   do
      $0 "$i"
   done
else
   TMPFILE=$(mktemp --suffix '.blend')
   # First step, we have to upgrade old models to cycles
   blender-2.7 "$1" -b -P materials_cycles_converter.py -- "$TMPFILE"
   # Second step we export the model
   blender "$TMPFILE" -b -P export2gltf.py -- "$1"
   #gltf-transform optimize --compress false --texture-compress false $IN $OUT
fi
