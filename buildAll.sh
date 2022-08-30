mkdir __results

for OUTPUT in $(find Slides/Stable -name '*.pillar')
do
	x=$OUTPUT
	echo $x
	pillar build pdf $OUTPUT
	echo _result/pdf/${x%.pillar}.pdf
	cp _result/pdf/${x%.pillar}.pdf __results
done


for OUTPUT in $(find Slides/Lectures -name '*.pillar')
do
	x=$OUTPUT
	echo $x
	pillar build pdf $OUTPUT
	echo _result/pdf/${x%.pillar}.pdf
	cp _result/pdf/${x%.pillar}.pdf __results
done
