#!/bin/bash

%rm -fr __results
%mkdir __results

./toMDConf.sh

buildSlide() {
	f=$(dirname $1)/$(basename $1 .pillar)
	echo $f
	pillar convertAlternateSlide ${f%}.pillar
	pillar build pdf ${f%}.md
	echo _result/pdf/${f%}.pdf
	cp _result/pdf/${f%}.pdf __results
}

for PILLAR_FILE in $(find Slides/Lectures -name '*.pillar')
do
	buildSlide $PILLAR_FILE
done