#!/bin/bash
# gimp export script

# Renders xcf project to a png
# Pass in -f <xcfFile> -o <outputDir> 

set -e

while getopts d:f:o: OPTION "$@"; do
    case $OPTION in
    d)
        set -x
        ;;
    f)
        XCFFILE=${OPTARG}
        ;;
    o)
        OUTPUTDIR=${OPTARG}
        ;;
    esac
done

if [[ -z "$XCFFILE" ]]; then
    echo "usage: `basename $0` [-d] -f <xcfFile> -o <outputDir>"
    exit 1
elif [[ -z "$OUTPUTDIR" ]]; then
    echo "usage: `basename $0` [-d] -f <xcfFile> -o <outputDir>"
    exit 1
fi

if [[ ! -z $(command -v gimp) ]]; then
    GIMPEXEC=gimp
else
    echo "You're missing the gimp package for your distro."
fi

# Start gimp with python-fu batch-interpreter
${GIMPEXEC} -i --batch-interpreter=python-fu-eval -b - << EOF
import gimpfu

def convert(filename):
    img = pdb.gimp_file_load(filename, filename)
    new_name = filename.rsplit(".",1)[0] + ".png"
    layer = pdb.gimp_image_merge_visible_layers(img, 1)

    pdb.gimp_file_save(img, layer, new_name, new_name)
    pdb.gimp_image_delete(img)

convert('${XCFFILE}')

pdb.gimp_quit(1)
EOF

mv *.png ${OUTPUTDIR}
