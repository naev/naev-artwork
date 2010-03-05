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
   # Redirects output to /dev/null by default.
   if [ "$DEBUG" == "true" ]; then
      printf '\n'
      $@
   else
      $@ &>/dev/null
   fi
}

function renderjobs {
   # Computes the number of queued renders (solely for output purposes.)
   if [ -z "$JOBS" ]; then
      JOBS=0
   fi
   if [ -n "$MODELS" ]; then
      for model in $MODELS; do
         ENGINES=$(enginestate $model)
         if [ -n "$layers" ]; then
            for layer in $layers; do
               JOBS=$(expr $JOBS + 1)
            done
         elif [ "$ENGINES" == "true" ]; then
            JOBS=$(expr $JOBS + 2)
         else
            JOBS=$(expr $JOBS + 1)
         fi
      done
   else
      JOBS=$(expr $ARGCOUNT \* 2)
   fi
   echo $JOBS
}

function enginestate {
   # If engines are disabled (as an argument), don't bother checking dim.sh
   if [ "$ENGINERENDER" == "0" ]; then
      ENGINES=false
   elif [ "$ENGINERENDER" == "1" ]; then
      ENGINES=true
   else
      ENGINES=`$RENDER_DIM e $1`
   fi
   echo $ENGINES
}

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
      #STATION=`$RENDER_DIM S $BLEND`
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER"
      REND_PARAMS="--spritex $SPRITES --intensity $INTENSITY"
   fi

   # Iterate over arguments and build the options list passed to render.py
   for arg in rotz resolution layer; do
      if [ -n "${!arg}" ]; then
         REND_PARAMS="$REND_PARAMS --$arg ${!arg}"
      fi
   done

   # Render
   test -d ".render" || mkdir ".render"
   cd .render
   if [ -z "$COUNT" ]; then
      COUNT=1
   fi

   # Render from the stations/ dir if argument is passed.
   if [ "$STATION" == true  ]; then
      RENDERPATH=$STATIONPATH
   fi

   # Outputs different things depending on layers.
   if [ -n "$layer" ] && [ "$layer" != 9 ]; then
      echo -en "\E[32mRendering ${BLEND%.blend}_$layer ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   elif [ "$layer" == 9 ]; then
      echo Uhh
      echo -en "\E[32mRendering ${BLEND%.blend}_engine ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   else
      echo Test $layer $ENGINES
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
      if [ -n "$layer" ] && [ "$layer" != 9 ]; then
         cp "sprite.png"  "../../raw/${BLEND%.blend}_$layer.png"
      elif [ "$layer" == 9 ] && [ "$ENGINES" == "true" ]; then
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

function finish {
   # Runs at the end, showing duration.
   if [ -n "$JOBS" ]; then
      echo -e "\E[31m- - - - - - - -"; tput sgr0
      echo -e "Render Finished: \t`date +%T`\nElapsed Time: \t\t$(converttime)"
   fi
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
      while getopts ":Sl:m:e:dghr:R:" opt; do
         case $opt in
            S) STATION="true"
               ;;
            l) layers=$OPTARG 
               ;;
            m) MODELS=$OPTARG
               ;;
            e) if [ "$OPTARG" != 1 ] && [ "$OPTARG" != 0 ]; then
                  echo -e "\E[31mValid input for -e is 0 or 1."; tput sgr0
                  exit 1
               else
                  ENGINERENDER=$OPTARG
               fi
               ;;
            d) DEBUG=true
               ;;
            g) echo -e "\E[33mNAEV Render Script (Getopts Mode)"; tput sgr0
               ;;
            h) echo -e " Usage: ./render.sh [options]\n"\
               " Options:\n"\
               "  -S: Render models from stations/\n"\
               "  -l \"[layers]\": Renders with extra layers. One render per layer.\n"\
               "  -m \"[models]\": List of models to be rendered.\n"\
               "  -e [0/1]: Disable or enable automatic engine glow rendering.\n"\
               "  -r [degrees]: Rotate the model before rendering. Negative is clockwise.\n"\
               "  -R [pixels]: Render at an arbitrary resolution. Default is 512px.\n"\
               "  -d: Enable verbose output from Blender.\n\n"\
               " Note: When rendering multiple models or layers, quotes are necessary."
               exit 1
               ;;
            r) rotz=$OPTARG
               ;;
            R) resolution=$OPTARG
               ;;
            \?) echo -e "\E[31mUnknown option: -$OPTARG\nRun with -h for usage information."; tput sgr0
               exit 1
               ;;
            :) echo -e "\E[31mOption -$OPTARG requires an argument."; tput sgr0
               exit 1
               ;;
         esac
      done

      if [ -n "$MODELS" ]; then
         JOBS=$(renderjobs)
         for model in $MODELS; do
            ENGINES=$(enginestate $model)
            if [ -n "$layers" ]; then
               # Multiple layers can be specified, so they must be iterated over.
               for layer in $layers; do
                  render "$model.blend"
               done
            elif [ "$ENGINES" == "true" ]; then
               # Engine meshes are on their own layer, but layer is not set by Getopts.
               render "$model.blend"
               layer=9
               render "$model.blend"
               unset layer
            else
               # Simply renders model with no special layers.
               render $model.blend
            fi
         done
      fi
      finish
   else # Falls back to legacy behaviour.
      for SHIPNAME in "$@"; do
         ARGCOUNT="`count $@`"
         JOBS=$(renderjobs)
         render "$SHIPNAME.blend"
         render "$SHIPNAME.blend" "comm"
         finish
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
