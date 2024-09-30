#!/bin/bash

rm -fr __results
mkdir __results

buildSlide() {
	f=$(dirname $1)/$(basename $1 .md)
	echo $f
	pillar build pdf $f.md
	echo _result/pdf/${f%.md}.pdf
	cp _result/pdf/${f%.md}.pdf __results
}

for MD_FILE in $(find Slides/Stable -name '*.md')
do
	buildSlide $MD_FILE
done

