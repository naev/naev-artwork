#!/usr/bin/env bash

function getintensity {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ dirge ]]; then INTENSITY=0.8;
   else INTENSITY=1.0
   fi
}

function getsprites {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ dirge ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ gawain ]]; then SPRITES=6;
   elif [[ "$SHIP" =~ hawking ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ hyena ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ koala ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ lancelot ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ llama ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ mule ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ pacifier ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ seaxbane ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ admonisher ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ schroedinger ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ goddard ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ vendetta ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ ancestor ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ kestrel ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ vigilance ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ kahan ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ archimedes ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ watson ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ quicksilver ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ derivative ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ peacemaker ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ perspicacity ]]; then SPRITES=8;
   elif [[ "$SHIP" =~ scintillation ]]; then SPRITES=8;
   elif [[ -e "$SHIP" ]]; then
      SPRITES=1
   else
      exit 1
   fi
}

function getsize {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ dirge ]]; then SIZE=40;
   elif [[ "$SHIP" =~ gawain ]]; then SIZE=56; # Upsized from 48, engine.
   elif [[ "$SHIP" =~ hawking ]]; then SIZE=139; # Downsized from 150, engine.
   elif [[ "$SHIP" =~ hyena ]]; then SIZE=44; # Upsized from 40, engine.
   elif [[ "$SHIP" =~ koala ]]; then SIZE=46; # Upsized from 46, engine 
   elif [[ "$SHIP" =~ lancelot ]]; then SIZE=56; # Downsized from 60, engine 
   elif [[ "$SHIP" =~ llama ]]; then SIZE=47; # Upsized from 44, engine.
   elif [[ "$SHIP" =~ mule ]]; then SIZE=96; # Upsized from 90, engine.
   elif [[ "$SHIP" =~ pacifier ]]; then SIZE=77; # Upsized from 74, engine.
   elif [[ "$SHIP" =~ seaxbane ]]; then SIZE=70;
   elif [[ "$SHIP" =~ admonisher ]]; then SIZE=68; # Downsized from 70, engine.
   elif [[ "$SHIP" =~ schroedinger ]]; then SIZE=47; # Downsized from 50, engine.
   elif [[ "$SHIP" =~ goddard ]]; then SIZE=125; # Downsized from 120, .blend enlarged 4%
   elif [[ "$SHIP" =~ vendetta ]]; then SIZE=49; # Downsized from 53, engine -- Made 8% larger
   elif [[ "$SHIP" =~ ancestor ]]; then SIZE=65; # Downsized from  70, engine.
   elif [[ "$SHIP" =~ kestrel ]]; then SIZE=125; # Upsized from 100, engine.
   elif [[ "$SHIP" =~ vigilance ]]; then SIZE=95;
   elif [[ "$SHIP" =~ kahan ]]; then SIZE=100;
   elif [[ "$SHIP" =~ archimedes ]]; then SIZE=130;
   elif [[ "$SHIP" =~ watson ]]; then SIZE=130;
   elif [[ "$SHIP" =~ quicksilver ]]; then SIZE=70;
   elif [[ "$SHIP" =~ derivative ]]; then SIZE=45;
   elif [[ "$SHIP" =~ peacemaker ]]; then SIZE=110;
   elif [[ "$SHIP" =~ perspicacity ]]; then SIZE=50;
   elif [[ "$SHIP" =~ scintillation ]]; then SIZE=70;
   fi
}

function hasengine {
   SHIP=`basename "${1%.png}"`

   ENGINE="true"
}

function isstation {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ outpost ]]; then STATION="true";
   elif [[ "$SHIP" =~ fighter_base ]]; then STATION="true";
   elif [[ "$SHIP" =~ fighterbase ]]; then STATION="true";
   elif [[ "$SHIP" =~ shipyard ]]; then STATION="true";
   elif [[ "$SHIP" =~ research ]]; then STATION="true";
   #elif [[ "$SHIP" =~ darkshed ]]; then STATION="true";
   else
      STATION="false";
      exit 1;
   fi
}

if [ "$1" == "s" ]; then
   getsprites $2
   echo $SPRITES
elif [ "$1" == "w" ]; then
   getsize $2
   echo $SIZE
elif [ "$1" == "e" ]; then
   hasengine $2
   echo $ENGINE
elif [ "$1" == "S" ]; then
   isstation $2
   echo $STATION
elif [ "$1" == "i" ]; then
   getintensity $2
   echo $INTENSITY
else
   echo "Unknown parameter $1!"
   exit 1
fi
