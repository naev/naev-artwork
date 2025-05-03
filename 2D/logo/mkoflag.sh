#!/usr/bin/bash

VER="$(inkscape --version)"
if [ "$(echo "$VER" | cut "-d " -f1)" == "Inkscape" ];then
   installedver=$(echo "$VER" | cut "-d " -f2)
else
   installedver="$VER"
fi
targetVer="1.0.0"

if [ "$(printf '%s\n' "$targetVer" "$installedver" | sort -V | head -n1)" = "$targetVer" ]; then
   echo 'o'
else
   echo 'e'
fi

