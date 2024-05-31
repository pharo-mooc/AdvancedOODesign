#!/bin/bash

for PDFFILE in $(find __results -name '*.pdf')
do
	echo PDF: $PDFFILE
	JPEG=__results/$(basename -s .pdf $PDFFILE)
	echo JPEG: $JPEG
	 pdftoppm -jpeg -f 1 -l 1 -scale-to 1000 $PDFFILE $JPEG
done

