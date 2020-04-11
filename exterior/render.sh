#!/bin/bash

res=400x400
if [ "$1" == "--hidpi" ]; then
    res=800x800
fi

mkdir -p out
for i in *.png *.jpg
do
    echo "$i -> out/$i"
    convert -scale $res "$i" "out/$i"
done
