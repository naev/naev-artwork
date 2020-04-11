#!/bin/sh

# Export all but bottom layer (for the .psd files)
# WIP: it works, but seems to not be quite right on some images

infile=$1
outfile=$2

gimp -n -i -b - <<EOF
(let* ((image (car (gimp-file-load RUN-NONINTERACTIVE "$infile" "$infile")))
       (layers (cadr (gimp-image-get-layers image))))
   (gimp-item-set-visible (vector-ref layers (- (vector-length layers) 1)) 0)
   (let ((layer (car (gimp-image-merge-visible-layers image CLIP-TO-IMAGE))))
      (gimp-file-save RUN-NONINTERACTIVE image layer "$outfile" "$outfile")))
(gimp-quit 0)
EOF
