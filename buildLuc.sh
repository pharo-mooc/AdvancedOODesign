#!/bin/env bash

mkdir -p __results.luc

SLIDES=(Slides/Stable/M1-2-Essence-02-Dispatch.pillar\
 Slides/Stable/M1-3-Essence-03-Inheritance-Basic.pillar\
 Slides/Stable/M2-3-Tests-03-TDD.pillar\
 Slides/Stable/M3-2-Essence-07-SelfSendsArePlansForReuse.pillar\
 Slides/Stable/M3-3-DesignPattern-02-HookAndTemplate.pillar\
 Slides/Stable/M4-1-BasicPrinciples-01-MethodIsReuse.pillar\
 Slides/Stable/M5-4-BasicPrinciples-06-UseVsInheritance.pillar\
 Slides/Stable/M6-4-DesignPattern-04-Visitor.pillar\
 Slides/Stable/M6-5-DesignPattern-05-VisitorDiscussions.pillar\
 Slides/Stable/M7-3-Principles-06-selfVSClassDispatch.pillar\
 Slides/Stable/M8-4-Essence-08-AboutMagicNumbers.pillar\
 Slides/Stable/M9-2-Principles-02-AboutClassMethodsAndRegistration.pillar\
 Slides/Stable/M9-3-Principles-03-AboutRegistration.pillar\
 Slides/Stable/M10-1-Principles-12-DualInterfaces.pillar\
 Slides/Stable/M10-4-Principles-11-PolymorphismSupportEvolution.pillar)

# for OUTPUT in $(find Slides/Stable -name '*.pillar')
for OUTPUT in ${SLIDES[*]}
do
	echo $OUTPUT
    x=$OUTPUT
	pillar build pdf $OUTPUT
	echo _result/pdf/${x%.pillar}.pdf
	cp _result/pdf/${x%.pillar}.pdf __results.luc
done


# for OUTPUT in $(find Slides/Lectures -name '*.pillar')
# do
# 	x=$OUTPUT
# 	echo $x
# 	pillar build pdf $OUTPUT
# 	echo _result/pdf/${x%.pillar}.pdf
# 	cp _result/pdf/${x%.pillar}.pdf __results
# done
