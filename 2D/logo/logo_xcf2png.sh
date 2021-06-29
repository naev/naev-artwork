#!/bin/sh

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 INFILE OUTFiLE"
else
    xcf2png "$1" > "$2"
    convert +repage -scale 96x96 -sharpen 1x0 "$2" "$2"
    composite "$2" logos/background.png "$2"
fi

# EOF #
