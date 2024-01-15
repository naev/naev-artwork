#!/bin/bash
BLENDER="blender-2.7"

if [ -z "$1" ]
then
    for i in ships/*.blend
    do
        ./tocycles.sh "$i"
    done
else
    $BLENDER "$1" -b -P materials_cycles_converter.py
fi
