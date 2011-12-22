#!/usr/bin/env bash

cd "$(dirname $0)"
RENDER="../render.py"
RENDER_DIM="../dim.sh"
MKSPR="$(./naevpath.sh)/mkspr"
SHIPPATH=".."
STATIONPATH="../../stations"
BEGIN=$(date +%s)

export PYTHONPATH="$PWD"

# Create output directory if needed
test -d "raw" || mkdir "raw"

usage()
{
   echo -e " Usage: ./render.sh [options]\n"\
   " Options:\n"\
   "  -S: Render models from stations/\n"\
   "  -l \"[layers]\": Renders with extra layers. One render per layer.\n"\
   "  -m \"[models]\": List of models to be rendered.\n"\
   "  -c [0/1]: Enable or disable comm rendering (on by default).\n"\
   "  -e [0/1]: Disable or enable automatic engine glow rendering.\n"\
   "  -r [degrees]: Rotate the model before rendering. Negative is clockwise.\n"\
   "  -R [pixels]: Render at an arbitrary resolution. Default is 512px.\n"\
   "  -d: Enable verbose output from Blender.\n\n"\
   " Note: When rendering multiple models or layers, quotes are necessary."
}

count()
{
   echo $@ | wc -w
}

converttime()
{
   date -d "0 $(expr `date +%s` - $BEGIN) sec" +%T
}

debuglevel()
{
   # Redirects output to /dev/null by default.
   if [ "$DEBUG" == "true" ]; then
      printf '\n'
      $@
   else
      $@ &>/dev/null
   fi
}

renderjobs()
{
   # Computes the number of queued renders (solely for output purposes.)
   if [ -z "$JOBS" ]; then
      JOBS=0
   fi

   if [ -n "$MODELS" ]; then
      for model in $MODELS; do
         if [ -e "$model.blend" ] && [ -z "$STATION" ] && ! $RENDER_DIM S $model >/dev/null; then
            ENGINES=$(enginestate $model)
         fi

         if [ -n "$layers" ]; then
            for layer in $layers; do
               JOBS=$(expr $JOBS + 1)
            done
         elif [ "$ENGINES" == "true" ]; then
            JOBS=$(expr $JOBS + 2)
         else
            JOBS=$(expr $JOBS + 1)
         fi

         if [ -e "$model.blend" ] && [ -z "$COMM" ] && [ "$STATION" != "true" ] && ! $RENDER_DIM S $model >/dev/null; then
            JOBS=$(expr $JOBS + 1)
         fi
      done
   else
      JOBS=$(expr $ARGCOUNT \* 2)
   fi
   echo $JOBS
}

enginestate()
{
   # If engines are disabled (as an argument), don't bother checking dim.sh
   if [ "$ENGINERENDER" == "0" ] ; then
      ENGINES=false
   elif [ "$ENGINERENDER" == "1" ]; then
      ENGINES=true
   else
      ENGINES=`$RENDER_DIM e $1`
   fi
   echo $ENGINES
}

render()
{
   BLEND="$1"
   RENDERPATH=$SHIPPATH
   if ! $RENDER_DIM s $BLEND > /dev/null; then
      echo -e "\E[31m$BLEND not found."; tput sgr0
      return
   fi

   # Check what to run.
   if [ "$STATION" == "true" ]; then
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER"
      SPRITES=
      REND_PARAMS="--spritex 1 --intensity $INTENSITY"
   elif [ "$2" = "comm" ]; then
      INTENSITY=`$RENDER_DIM i $BLEND`
      rotz=-135
      REND_SCRIPT="$RENDER"
      REND_PARAMS="--spritex 1 --intensity $INTENSITY --comm 1"
   else
      SPRITES=`$RENDER_DIM s $BLEND`
      STATION=`$RENDER_DIM S $BLEND`
      INTENSITY=`$RENDER_DIM i $BLEND`
      REND_SCRIPT="$RENDER"
      REND_PARAMS="--spritex $SPRITES --intensity $INTENSITY"
      unset rotz;
   fi

   # Render from the stations/ dir if argument is passed.
   if [ "$STATION" == true  ]; then
      RENDERPATH=$STATIONPATH
      REND_PARAMS="--spritex 1 --intensity $INTENSITY"
   fi

   if [[ ! -e "$BLEND" ]] && [ "$STATION" != "true" ] || [[ ! -e "../stations/$BLEND" ]] &&  [[ "$STATION" == "true" ]]; then
      echo -e "\E[31m$BLEND not found."; tput sgr0
      return
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

   # Outputs different things depending on layers.
   if [ -n "$layer" ] && [ "$layer" != 9 ]; then
      echo -en "\E[32mRendering ${BLEND%.blend}_$layer ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   elif [ "$layer" == 9 ]; then
      echo -en "\E[32mRendering ${BLEND%.blend}_engine ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   else
      echo -en "\E[32mRendering ${BLEND%.blend} ... "; tput sgr0
      echo -n "(Render $COUNT of $JOBS)"
      COUNT=$(expr $COUNT + 1)
      debuglevel blender "$RENDERPATH/$BLEND" -P "$PWD/../$REND_SCRIPT" -- $REND_PARAMS
   fi

   # Post process
   if [ "$2" = "comm" ]; then
      cp "000.png" "../../raw/${BLEND%.blend}_comm.png"
      echo -e " ... Comm done!"
   elif [ -n "$STATION" ]; then
      cp "000.png" "../../raw/${BLEND%.blend}.png"
      echo -e " ... Station done!"
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
   #rm *.png
   cd ..
}

finish()
{
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
      while getopts ":Sc:l:m:e:dghr:R:" opt; do
         case $opt in
            S) STATION="true"
               ;;
            c) if [ "$OPTARG" == 0 ]; then
                  COMM=$OPTARG
               elif [ "$OPTARG" != 1 ]; then
                  echo -e "\E[31mValid input for -c is 0 or 1."; tput sgr0
                  exit 1
               fi
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
            h) usage
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
            elif [ "$STATION" == "true" ]; then
               render "$model.blend"
            elif [ -z "$STATION" ] && $RENDER_DIM S $model || [[ -e "../stations/$model.blend" ]]; then
               $RENDER_DIM S $model
               STATION="true"
               render "$model.blend"
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

            if [ -z "$COMM" ] && [ "$STATION" != "true" ]; then
               render "$model.blend" "comm"
            fi
         done
      else
         echo -n "This will render all models, which may take a while. Type yes to continue: "
      read choice
      case $choice in
         yes)
            for BLEND in *.blend; do
               unset rotz
               render "$BLEND"
               render "$BLEND" "comm"
            done
            finish
            ;;
         *)
            echo "$choice" is not valid, terminating.
            exit 1
            ;;
      esac
      fi
      finish
   else # Falls back to legacy behaviour.
      echo -n "This will render all models, which may take a while. Type \"yes\" to continue: "
      read choice
      case $choice in
         yes)
            for BLEND in *.blend; do
               unset rotz
               render "$BLEND"
               render "$BLEND" "comm"
            done
            finish
            ;;
         *)
            echo "$choice" is not valid, terminating.
            exit 1
            ;;
      esac
   fi

# No parameters, do them all
else
   for BLEND in *.blend; do
      render "$BLEND"
      render "$BLEND" "comm"
   done
fi
cd ..
