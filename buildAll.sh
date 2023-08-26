#!/bin/bash

rm -fr __results
mkdir __results

buildSlide() {
    f=$1
	echo $f
	pillar build pdf $f
	echo _result/pdf/${f%.pillar}.pdf
	cp _result/pdf/${f%.pillar}.pdf __results
}

for PILLAR_FILE in $(find Slides/Stable -name '*.pillar')
do
	buildSlide $PILLAR_FILE
done

# for PILLAR_FILE in $(find Slides/Lectures -name '*.pillar')
# do
# 	buildSlide $PILLAR_FILE
# done
