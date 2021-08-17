#!/bin/bash
BLENDER="${BLENDER:-blender}"

if [ -z "$1" ]
then
    for i in ships/*.blend
    do
        ./export2obj.sh $i
    done
else
    $BLENDER $1 -b -P export2obj.py
fi
