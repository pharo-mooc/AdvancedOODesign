#!/usr/bin/env python3

import os
import sys
import argparse

OUTDIR="__results.luc"

SLIDES= [
    "Slides/Stable/M1-2-Essence-02-Dispatch.pillar",
    "Slides/Stable/M1-3-Essence-03-Inheritance-Basic.pillar",
    "Slides/Stable/M2-3-Tests-03-TDD.pillar",
    "Slides/Stable/M3-2-Essence-07-SelfSendsArePlansForReuse.pillar",
    "Slides/Stable/M3-3-DesignPattern-02-HookAndTemplate.pillar",
    "Slides/Stable/M4-1-BasicPrinciples-01-MethodIsReuse.pillar",
    "Slides/Stable/M5-1-DesignPattern-03-Composite.pillar",
    "Slides/Stable/M5-4-BasicPrinciples-06-DelegationVsInheritance.pillar",
    "Slides/Stable/M6-4-DesignPattern-04-Visitor.pillar",
    "Slides/Stable/M6-5-DesignPattern-05-VisitorDiscussions.pillar",
    "Slides/Stable/M7-3-Principles-06-selfVSClassDispatch.pillar",
    "Slides/Stable/M8-4-Essence-08-AboutMagicNumbers.pillar",
    "Slides/Stable/M9-2-Principles-02-AboutClassMethodsAndRegistration.pillar",
    "Slides/Stable/M9-3-Principles-03-AboutRegistration.pillar",
    "Slides/Stable/M10-1-Principles-12-DualInterfaces.pillar",
    "Slides/Stable/M10-4-Principles-11-PolymorphismSupportEvolution.pillar ",
]

class MyTerm:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def bash(command):
        self.print(command)
        p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
        return p.stdout.read()

    @classmethod
    def print(cls,str,color=OKBLUE):
        print(color + str + MyTerm.ENDC)



def main():
    parser = argparse.ArgumentParser(description='Compile Luc Slides')
    # prefixing the argument with -- means it's optional
    parser.add_argument('-s','--slide', help='slide num to compile')
    args = parser.parse_args()

    filesToCompile = SLIDES
    if(args.slide is not None):
        filesToCompile = [ SLIDES[int(args.slide)] ]
    else:
        os.system(f"rm -fr {OUTDIR} && mkdir -p {OUTDIR}")

    for pillarfile in filesToCompile:
        pdffile = pillarfile.rsplit('.', 1)[0] + '.pdf'
        MyTerm.print(pillarfile,MyTerm.WARNING)
        cmd = f"pillar build pdf {pillarfile} && cp _result/pdf/{pdffile} {OUTDIR}"
        MyTerm.print(cmd)
        os.system(cmd)

if __name__ == '__main__':
    main()
