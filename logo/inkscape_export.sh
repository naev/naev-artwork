#!/bin/bash
# inkscape export script

# Renders svg to a png (takes into account the various syntax that inkscape uses..)
# Pass in -f <svgFile> -o <outputDir> 

set -e

while getopts d:f:o: OPTION "$@"; do
    case $OPTION in
    d)
        set -x
        ;;
    f)
        SVGFILE=${OPTARG}
        ;;
    o)
        OUTPUTDIR=${OPTARG}
        ;;
    esac
done

if [[ -z "$SVGFILE" ]]; then
    echo "usage: `basename $0` [-d] -f <xcfFile> -o <outputDir>"
    exit 1
elif [[ -z "$OUTPUTDIR" ]]; then
    echo "usage: `basename $0` [-d] -f <xcfFile> -o <outputDir>"
    exit 1
fi

if ! [ -x "$(command -v inkscape)" ]; then
    echo "You don't have Inkscape installed!, install it for your distro."
else
    installedver="$(inkscape --version)"
    targetVer="1.0.0"
    if [ "$(printf '%s\n' "$targetVer" "$installedver" | sort -V | head -n1)" = "$targetVer" ]; then 
        inkscape "${SVGFILE}" --export-filename "${OUTPUTDIR}"
    else
        inkscape -z "${SVGFILE}" -e "${OUTPUTDIR}"
    fi
fi
