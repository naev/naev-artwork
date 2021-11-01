#!/bin/bash
BLENDER="${BLENDER:-blender}"

if [ -z "$1" ]
then
    for i in ships/*-cycles.blend
    do
        $0 $i
    done
else
    $BLENDER $1 -b -P export2gltf.py
fi
