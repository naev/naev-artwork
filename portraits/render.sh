#!/bin/bash

for i in *.xcf
do
    echo "$i -> $i.png"
    ./xcf2png.sh $i $i.png
done
