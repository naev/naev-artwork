#!/usr/bin/env bash


RENDER_DIM="$PWD/dim.sh"


function process {
   RAWFILE=$1
   BASE=`basename $RAWFILE`
   OUTFILE="final/${BASE%.png}.webp"
   FILENAME="${BASE%.png}"
   if [[ -f "$OUTFILE" ]]; then
      return
   fi

   # Get size.
   if [[ "$RAWFILE" =~ .*_comm\.png ]]; then
      SIZE=1024
      TRIM="-trim +repage -bordercolor none -border 64"
   else
      W=`$RENDER_DIM w "${FILENAME%_engine}"`
      S=`$RENDER_DIM s "${FILENAME%_engine}"`
      SIZE=$(($W*$S))
      TRIM=""
   fi

   if [ $SIZE -gt 2048 ]; then
      echo "WARNING: Size is greater then 2048, that's baaad mmkay?"
   fi

   # Actually process.
   echo -n "Finishing ${BASE} [${SIZE}x${SIZE}] ... "
   #convert -resize $SIZE -sharpen 1 "$RAWFILE" "final/${BASE}" > /dev/null
   #optipng "final/${BASE}" > /dev/null
   # Resize using LAB colorspace and sharpen once. Afterwards convert into lossless best quality webp
   TMPFILE=`mktemp --suffix .png`
   convert $TRIM -colorspace LAB -resize $SIZE -sharpen 1 -colorspace sRGB "$RAWFILE" "$TMPFILE" &> /dev/null
   cwebp -lossless -z 9 "$TMPFILE" -o "$OUTFILE" &> /dev/null
   echo "Done!"
}

if [ ! -d "final" ];then mkdir "final"; fi

for RAWFILE in raw/*.png; do
   process $RAWFILE
done
