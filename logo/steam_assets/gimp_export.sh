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
    exit 1
fi

# Start gimp with script-fu convert-xcf-png
{
cat <<EOF
(define (convert-xcf-png ${XCFFILE} ${OUTPUTDIR})
    (let* (
            (image (car (gimp-xcf-load RUN-NONINTERACTIVE ${XCFFILE} ${XCFFILE} )))
            (drawable (car (gimp-image-merge-visible-layers image CLIP-TO-IMAGE)))
            )
        (begin (display "Exporting ")(display ${XCFFILE})(display " -> ")(display ${OUTPUTDIR})(newline))
        (file-png-save2 RUN-NONINTERACTIVE image drawable ${OUTPUTDIR} ${OUTPUTDIR} 0 9 0 0 0 0 0 0 0)
        (gimp-image-delete image)
    )
)

(gimp-message-set-handler 1) ; Messages to standard output
EOF

echo "(convert-xcf-png \"${XCFFILE}\" \"${OUTPUTDIR}\")"

echo "(gimp-quit 0)"

} | ${GIMPEXEC} -i -b -
