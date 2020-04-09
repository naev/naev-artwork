#!/bin/bash

res=200x150
if [ "$1" == "--hidpi" ]; then
    res=400x300
fi

for i in $(find -name '*.xcf')
do
    mkdir -p out/$(dirname "$i")
    echo "$i -> out/${i%.xcf}.png"
    ./xcf2png.sh $i out/${i%.xcf}.png $res
done
