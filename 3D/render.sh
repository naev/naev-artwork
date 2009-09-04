#!/usr/bin/env bash

RENDER="../render.py"
RENDER_COMM="../render_comm.py"
RENDER_DIM="../dim.sh"
MKSPR="$(./naevpath.sh)/mkspr"

export PYTHONPATH="$PWD"

# Create output directory if needed
test -d "raw" || mkdir "raw"

function render {
   BLEND="$1"
   echo $BLEND

   # Check what to run.
   if [ "$2" = "comm" ]; then
      REND_SCRIPT="$RENDER_COMM"
      REND_PARAMS=""
   else
      SPRITES=`$RENDER_DIM s $BLEND`
      ENGINES=`$RENDER_DIM e $BLEND`
      REND_SCRIPT="$RENDER"
      REND_PARAMS="--spritex $SPRITES"
   fi

   # Render
   echo -n "Rendering ${BLEND%.blend} ... "
   test -d ".render" || mkdir ".render"
   cd .render
   echo "$PWD/../$REND_SCRIPT"
   blender "../$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS

   # Post process
   if [ "$2" = "comm" ]; then
      cp "comm.png" "../../raw/${BLEND%.blend}_comm.png"
      echo "comm done!"
   else
      # Make sprite
      $MKSPR $SPRITES
      cp "sprite.png"  "../../raw/${BLEND%.blend}.png"
      echo "done!"

      # Make engine sprite if applicable
      if [ "$ENGINES" == "true" ]; then
         echo -n "Rendering ${BLEND%.blend}_engine ... "
         blender "../$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS --engine true
         $MKSPR $SPRITES
         cp "sprite.png"  "../../raw/${BLEND%.blend}_engine.png"
         echo "done!"
      fi
   fi

   # Clean up
   rm *.png
   cd ..
}

cd ships
# Parameters - only do those
if [ $# -gt 0 ]; then
   if [ "$1" = "comm" ]; then
      echo "Rendering comms"
      for BLEND in *.blend; do
         render "$BLEND" "comm"
      done
   else
      for SHIPNAME in "$@"; do
         render "$SHIPNAME.blend"
         render "$SHIPNAME.blend" "comm"
      done
   fi
# No parametrs, do them all
else
   for BLEND in *.blend; do
      render "$BLEND"
      render "$BLEND" "comm"
   done
fi
cd ..
