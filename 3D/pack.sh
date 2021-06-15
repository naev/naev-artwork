#!/usr/bin/env bash

PACK="./pack.py"
BLENDER="${BLENDER:-blender}"

function pack {
   BLEND=$1
   echo -n "Packing ${BLEND%.blend} ... "
   "$BLENDER" "$BLEND" -P $PACK > /dev/null
   echo "done!"
}

if [ $# -gt 0 ]; then
   for FILE in "$@"; do
      pack "$FILE"
   done
else
   for BLEND in ships/*.blend; do
      pack $BLEND
   done
fi
