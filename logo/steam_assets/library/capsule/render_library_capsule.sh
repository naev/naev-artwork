#!/bin/sh
# mlt export script
# uses ffmpeg and mlt to export kdenlive videoproject to apng
# ffmpeg generates a static version in addition

set -e

while getopts d:f:o: OPTION "$@"; do
    case $OPTION in
    d)
        set -x
        ;;
    f)
        MLTFILE=${OPTARG}
        ;;
    o)
        OUTPUTDIR=${OPTARG}
        ;;
    esac
done

if [[ -z "$MLTFILE" ]]; then
    echo "usage: `basename $0` [-d] -f <mltFile> -o <outputDir>"
    exit 1
elif [[ -z "$OUTPUTDIR" ]]; then
    echo "usage: `basename $0` [-d] -f mltFile> -o <outputDir>"
    exit 1
fi

if [[ ! -z $(command -v ffmpeg) ]]; then
    FFMPEGEXEC=ffmpeg
else
    echo "You're missing the ffmpeg package for your distro."
    exit 1
fi

if [[ ! -z $(command -v mlt-melt) ]]; then
    MLTEXEC=mlt-melt
elif [[ ! -z $(command -v melt) ]]; then
    MLTEXEC=melt
else
    echo "You're missing the mlt-melt package for your distro."
    exit 1
fi

${MLTEXEC} ${MLTFILE}
${FFMPEGEXEC} -i naev_library_animated.png -frames:v 1 naev_library_static.png

mv *.png ${OUTPUTDIR}/
