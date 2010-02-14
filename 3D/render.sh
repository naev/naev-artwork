#!/usr/bin/env bash

RENDER="../render.py"
RENDER_COMM="../render_comm.py"
RENDER_DIM="../dim.sh"
MKSPR="$(./naevpath.sh)/mkspr"
SHIPPATH=".."
STATIONPATH="../../stations"

export PYTHONPATH="$PWD"

# Create output directory if needed
test -d "raw" || mkdir "raw"

function render {
   BLEND="$1"
   RENDERPATH=$SHIPPATH
   
   # Check what to run.
   if [ "$2" = "comm" ]; then
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER_COMM"
      REND_PARAMS="--intensity $INTENSITY"
   else
      SPRITES=`$RENDER_DIM s $BLEND`
      ENGINES=`$RENDER_DIM e $BLEND`
      #STATION=`$RENDER_DIM S $BLEND`
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER"
      REND_PARAMS="--spritex $SPRITES --intensity $INTENSITY"
   fi

   # Render
   test -d ".render" || mkdir ".render"
   cd .render

   if [ "$STATION" == true  ]; then
      RENDERPATH=$STATIONPATH
   fi

   if [ -z $LAYER ]; then
      echo -en "\E[32mRendering ${BLEND%.blend} ...\E[37m"
      blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   else
      echo -en "\E[32mRendering ${BLEND%.blend}_$LAYER ... \E[37m"
      blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS --layers $LAYER
   fi

   # Post process
   if [ "$2" = "comm" ]; then
      cp "comm.png" "../../raw/${BLEND%.blend}_comm.png"
      echo -e "Comm done!\n"
   else
      # Make sprite
      $MKSPR $SPRITES
      if [ -z $LAYER ]; then
         cp "sprite.png"  "../../raw/${BLEND%.blend}.png"
      else
         cp "sprite.png"  "../../raw/${BLEND%.blend}_$LAYER.png"
      fi
      echo -e "Done!\n"

      # Make engine sprite if applicable
      if [ "$ENGINES" == "true" ]; then
         echo -n "Rendering ${BLEND%.blend}_engine ... "
         blender "../$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS --engine true
         $MKSPR $SPRITES
         cp "sprite.png"  "../../raw/${BLEND%.blend}_engine.png"
         echo -e "Done!\n"
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
   elif [ "$1" = "-g" ]; then
      while getopts ":Sl:m:gh" opt; do
         case $opt in
            S)
               STATION="true"
               ;;
            l)
               LAYERS=$OPTARG
               ;;
            m)
               MODELS=$OPTARG
               ;;
            g)
               echo -e "\E[33mNAEV Render Script (Getopts Mode)\E[37m"
               ;;
            h)
               echo "Usage: ./render.sh [options]
   Options:
      -S: Render models from stations/
      -l \"[layers]\": Renders with extra layers. One render per layer.
      -m \"[models]\": List of models to be rendered.

      Note: When rendering multiple models or layers, quotes are necessary."
               ;;
            \?)
               echo -e "Unknown option: -$OPTARG\nRun with -h for usage information." 
               exit 1
               ;;
            :)
               echo "Option -$OPTARG requires an argument." 
               exit 1
               ;;
         esac
      done
      if [ -n "$MODELS" ]; then
         for model in $MODELS; do
            if [ -n "$LAYERS" ]; then
               for layer in $LAYERS; do
                  LAYER=$layer
                  render $model.blend
               done
            else
               render $model.blend
            fi
         done
      fi
   else
      for SHIPNAME in "$@"; do
         render "$SHIPNAME.blend"
         render "$SHIPNAME.blend" "comm"
      done
   fi

# No parameters, do them all
else
   for BLEND in *.blend; do
      render "$BLEND"
      render "$BLEND" "comm"
   done
fi
cd ..
