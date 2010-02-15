#!/usr/bin/env bash

RENDER="../render.py"
RENDER_COMM="../render_comm.py"
RENDER_DIM="../dim.sh"
MKSPR="$(./naevpath.sh)/mkspr"
SHIPPATH=".."
STATIONPATH="../../stations"
BEGIN=$(date +%s)

export PYTHONPATH="$PWD"

# Create output directory if needed
test -d "raw" || mkdir "raw"

function count {
   echo $@ | wc -w
}
function converttime {
   date -d "0 $(expr `date +%s` - $BEGIN) sec" +%T
}

function debuglevel {
   if [ "$DEBUG" == "true" ]; then
      printf '\n'
      $@
   else
      $@ &>/dev/null
   fi
}

function renderjobs {
   if [ -z "$JOBS" ]; then
      JOBS=0
   fi
   if [ -n "$MODELS" ]; then
      for model in $MODELS; do
         if [ -n "$LAYERS" ]; then
            for layer in $LAYERS; do               
               JOBS=$(expr $JOBS + 1)
            done
         elif [ "$ENGINES" == "true" ] && [ "$FIRSTRUN" != "false" ]; then
            JOBS=$(expr $JOBS + 1 + `count $MODELS`)
            FIRSTRUN=false
         else
            JOBS=$(expr $JOBS + 1)
         fi
      done
   else
      JOBS=$(expr $ARGCOUNT \* 2)
   fi
   echo $JOBS
}

function render {
   BLEND="$1"
   RENDERPATH=$SHIPPATH
   RENDERED=1
   
   # Check what to run.
   if [ "$2" = "comm" ]; then
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER_COMM"
      REND_PARAMS="--intensity $INTENSITY"
   else
      SPRITES=`$RENDER_DIM s $BLEND`
      #STATION=`$RENDER_DIM S $BLEND`
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER"
      REND_PARAMS="--spritex $SPRITES --intensity $INTENSITY"
   fi

   # Render
   test -d ".render" || mkdir ".render"
   cd .render
   if [ -z "$COUNT" ]; then
      COUNT=1
   fi
   if [ "$STATION" == true  ]; then
      RENDERPATH=$STATIONPATH
   fi
   if [ -n "$LAYER" ] && [ "$LAYER" != 9 ]; then
      echo -en "\E[32mRendering ${BLEND%.blend}_$LAYER ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS --layers $LAYER
   elif [ "$LAYER" == 9 ] && [ "$ENGINES" == "true" ]; then
      echo -en "\E[32mRendering ${BLEND%.blend}_engine ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS --layers $LAYER
   else
      echo -en "\E[32mRendering ${BLEND%.blend} ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   fi

   # Post process
   if [ "$2" = "comm" ]; then
      cp "comm.png" "../../raw/${BLEND%.blend}_comm.png"
      echo -e " ... Comm done!"
   else
      # Make sprite
      $MKSPR $SPRITES
      if [ -n "$LAYER" ] && [ "$LAYER" != 9 ]; then
         cp "sprite.png"  "../../raw/${BLEND%.blend}_$LAYER.png"
      elif [ "$LAYER" == 9 ] && [ "$ENGINES" == "true" ]; then
         cp "sprite.png"  "../../raw/${BLEND%.blend}_engine.png"
      else
         cp "sprite.png"  "../../raw/${BLEND%.blend}.png"
      fi
      echo " ... Done!"
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
      while getopts ":Sl:m:e:dgh" opt; do
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
            e)
               if [ "$OPTARG" != 1 ] && [ "$OPTARG" != 0 ]; then
                  echo -e "\E[31mValid input for -e is 0 or 1."; tput sgr0
                  exit 1
               else
                  ENGINERENDER=$OPTARG
               fi
               ;;
            d)
               DEBUG=true
               ;;
            g)
               echo -e "\E[33mNAEV Render Script (Getopts Mode)"; tput sgr0
               ;;
            h)
               echo "Usage: ./render.sh [options]
   Options:
      -S: Render models from stations/
      -l \"[layers]\": Renders with extra layers. One render per layer.
      -m \"[models]\": List of models to be rendered.
      -e [0/1]: Disable or enable automatic engine glow rendering.
      -d: Enable verbose output from Blender.

      Note: When rendering multiple models or layers, quotes are necessary."
               ;;
            \?)
               echo -e "\E[31mUnknown option: -$OPTARG\nRun with -h for usage information."; tput sgr0
               exit 1
               ;;
            :)
               echo -e "\E[31mOption -$OPTARG requires an argument."; tput sgr0
               exit 1
               ;;
         esac
      done
      
      if [ "$ENGINERENDER" == "0" ]; then
         ENGINES=false
         NOCONTINUE=true
      else
         ENGINES=`$RENDER_DIM e $BLEND`
      fi

      if [ -n "$MODELS" ]; then
         JOBS=$(renderjobs)
         for model in $MODELS; do
            ENGINES=`$RENDER_DIM e $model.blend`
            if [ -n "$LAYERS" ]; then
               for layer in $LAYERS; do
                  LAYER=$layer
                  render "$model.blend"
               done
            elif [ "$ENGINES" == "true" ]; then
               render "$model.blend"
               if [ "$NOCONTINUE" != "true" ]; then
                  LAYER=9
                  render "$model.blend"
                  unset LAYER
               fi
            else
               render $model.blend
            fi
         done
      fi
   else
      for SHIPNAME in "$@"; do
         ARGCOUNT="`count $@`"
         JOBS=$(renderjobs)
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

if [ -n "$RENDERED" ]; then
   echo -e "\E[31m- - - - - - - -"; tput sgr0
   echo -e "Render Finished: \t`date +%T`\nElapsed Time: \t\t$(converttime)"
fi
