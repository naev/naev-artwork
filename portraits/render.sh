#!/bin/bash

for i in $(find -name '*.xcf')
do
    mkdir -p out/$(dirname "$i")
    echo "$i -> out/${i%.xcf}.png"
    ./xcf2png.sh $i out/${i%.xcf}.png
done
