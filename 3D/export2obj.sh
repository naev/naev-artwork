#!/bin/bash

if [ -z "$1" ]
then
    for i in ships/*.blend
    do
        ./export2obj.sh $i
    done
else
    blender-2.7 $1 -b -P export2obj.py
fi
