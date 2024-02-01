#!/bin/bash

if [ -z "$1" ]
then
   for i in ships/*.blend
   do
      $0 "$i"
   done
else
   BNAME="$(basename "$1")"
   TMPFILE=$(mktemp --suffix '.blend')
   # First step, we have to upgrade old models to cycles
   blender-2.7 "$1" -b -P materials_cycles_converter.py -- "$TMPFILE" || TMPFILE="$1"

   # Second step we export the model
   blender "$TMPFILE" -b -P export2gltf.py -- "$1" || exit 1
fi
