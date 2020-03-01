#!/bin/sh

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 INFILE OUTFiLE"
else
    xcf2png "$1" > "$2"
    convert -crop 1680x1260+120+180 +repage "$2" "$2"
    composite "$2" background.png "$2"
    convert -scale 200x150 -sharpen 0.25x0 "$2" "$2"
fi

# EOF #
