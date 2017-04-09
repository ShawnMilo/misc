#!/usr/bin/env bash

# Requires tesseract-ocr and imagemagick

for F in $*
do
    filename=$(basename $F)
    ext=${filename#*.}
    flat=$(mktemp --suffix=.$ext)
    txt=$(mktemp)

    convert -density 300 -depth 8 -type grayscale $F $flat || continue
    tesseract $flat $txt
    cat ${txt}.txt # tesseract appends .txt to whatever you give it
    rm $flat
    rm $txt
done
