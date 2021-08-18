#!/usr/bin/env bash

function getintensity {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ dirge ]]; then INTENSITY=0.8;
   else INTENSITY=1.0
   fi
}

function getsprites {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ hawking ]]; then SPRITES=12;
   elif [[ "$SHIP" = arx ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ mule ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ pacifier ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ goddard ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ kestrel ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ vigilance ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ kahan ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ archimedes ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ watson ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ quicksilver ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ peacemaker ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ taciturnity ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ apprehension ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ certitude ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ divinity ]]; then SPRITES=12;
   elif [[ "$SHIP" = zalek_sting ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ rhino ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ phalanx ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ diablo ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ hephaestus ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ mephisto ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ preacher ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ nyx ]]; then SPRITES=10;
   elif [[ "$SHIP" =~ ira ]]; then SPRITES=12;
   elif [[ "$SHIP" =~ dogma ]]; then SPRITES=12;
   else
      SPRITES=8
   fi
}

function getsize {
   SHIP=`basename "${1%.png}"`

   if [[ "$SHIP" =~ dirge ]]; then SIZE=40;
   elif [[ "$SHIP" =~ gawain ]]; then SIZE=56; # Upsized from 48, engine.
   elif [[ "$SHIP" =~ hawking ]]; then SIZE=139; # Downsized from 150, engine.
   elif [[ "$SHIP" = hyena ]]; then SIZE=44; # Upsized from 40, engine.
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
   elif [[ "$SHIP" =~ virtuosity ]]; then SIZE=70;
   elif [[ "$SHIP" =~ taciturnity ]]; then SIZE=80;
   elif [[ "$SHIP" =~ apprehension ]]; then SIZE=90;
   elif [[ "$SHIP" =~ certitude ]]; then SIZE=120;
   elif [[ "$SHIP" = drone ]]; then SIZE=70;
   elif [[ "$SHIP" = drone_hyena ]]; then SIZE=70;
   elif [[ "$SHIP" = zalek_drone_bomber ]]; then SIZE=48;
   elif [[ "$SHIP" = zalek_drone_heavy ]]; then SIZE=45;
   elif [[ "$SHIP" = zalek_drone_light ]]; then SIZE=40;
   elif [[ "$SHIP" = zalek_drone_scout ]]; then SIZE=38;
   elif [[ "$SHIP" = shaman ]]; then SIZE=68;
   elif [[ "$SHIP" =~ shark ]]; then SIZE=54;
   elif [[ "$SHIP" = zalek_sting ]]; then SIZE=95;
   elif [[ "$SHIP" = arx ]]; then SIZE=124;
   elif [[ "$SHIP" = divinity ]]; then SIZE=140;
   elif [[ "$SHIP" = fidelity ]]; then SIZE=60;
   elif [[ "$SHIP" = hyena ]]; then SIZE=44;
   elif [[ "$SHIP" =~ rhino ]]; then SIZE=100;
   elif [[ "$SHIP" =~ phalanx ]]; then SIZE=95;
   elif [[ "$SHIP" =~ diablo ]]; then SIZE=170; # near 2048. Increase?
   elif [[ "$SHIP" =~ hephaestus ]]; then SIZE=170; # near 2048. Increase?
   elif [[ "$SHIP" =~ mephisto ]]; then SIZE=156;
   elif [[ "$SHIP" =~ reaver ]]; then SIZE=68;
   elif [[ "$SHIP" =~ preacher ]]; then SIZE=70;
   elif [[ "$SHIP" =~ nyx ]]; then SIZE=96;
   elif [[ "$SHIP" =~ marauder ]]; then SIZE=66;
   elif [[ "$SHIP" =~ ira ]]; then SIZE=112;
   elif [[ "$SHIP" =~ dogma ]]; then SIZE=128;
   #elif [[ "$SHIP" =~ viper ]]; then SIZE=60; # NOT IN GAME!!
   # Derelicts
   #elif [[ "$SHIP" == derelict_goddard ]]; then SIZE=125;
   #elif [[ "$SHIP" =~ derelict_koala ]]; then SIZE=46;
   #elif [[ "$SHIP" =~ derelict_llama ]]; then SIZE=47;
   #elif [[ "$SHIP" =~ derelict_mule ]]; then SIZE=96;
   #elif [[ "$SHIP" =~ derelict_phalanx ]]; then SIZE=95;
   #elif [[ "$SHIP" =~ derelict_shark ]]; then SIZE=54;
   #elif [[ "$SHIP" =~ derelict_vendetta ]]; then SIZE=46;
   #elif [[ "$SHIP" =~ debris01 ]]; then SIZE=30;
   #elif [[ "$SHIP" =~ debris02 ]]; then SIZE=30;
   else
      exit 1
   fi
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
