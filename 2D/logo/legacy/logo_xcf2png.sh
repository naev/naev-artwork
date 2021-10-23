#!/bin/sh

set -e

if [ $# -ne 3 ]; then
    echo "Usage: $0 INFILE MAX_DIMENSION OUTFILE"
else
    xcf2png "$1" > "$3"
    convert +repage -scale "$2"x"$2" -sharpen 1x0 "$3" "$3"
fi

# EOF #
