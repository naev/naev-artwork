#!/usr/bin/env bash

RENDER="./render.py"
BLENDER="${BLENDER:-blender}"
# allow for custom path for blender as return by optional blenderpath.sh script
[[ -f "../blenderpath.sh" ]] && BLENDER="$(../blenderpath.sh)blender"

# Create output directory if needed
if [ ! -d "raw" ]; then mkdir "raw"; fi

function render {
   BLEND="$1"
   echo -n "Rendering ${BLEND%.blend} ... "
   $BLENDER -b "$BLEND" -P $RENDER > /dev/null
   mv "000.png"  "raw/${BLEND%.blend}.png"
   echo "done!"
}

# Parameters - only do those
if [ $# -gt 0 ]; then
   for STATION in "$@"; do
      render "$STATION.blend"
   done
# No parametrs, do them all
else
   for BLEND in *.blend; do
      render "$BLEND"
   done
fi
