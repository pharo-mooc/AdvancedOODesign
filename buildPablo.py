#!/usr/bin/env python3

import os
import sys
import argparse

OUTDIR="__results.pablo"

SLIDES= [
    "Slides/Stable/M2-4-Tests-04-XTDD.pillar",
    "Slides/Stable/M2-5-Tests-05-ParametrizedTests.pillar",
    "Slides/Stable/M4-2-BasicPrinciples-04-AboutObjectsVSData.pillar",
    "Slides/Stable/M4-4-BasicPrinciples-05-FatClassesAreBad.pillar",
    "Slides/Stable/M5-2-DesignPattern-11-State.pillar",
    "Slides/Stable/M5-3-DesignPattern-07-Command.pillar",
    "Slides/Stable/M5-5-CaseStudy-01-TurningAProcIntoAnObject.pillar",
    "Slides/Stable/M5-6-Lang-04-BlocksVsObjects.pillar",
    "Slides/Stable/M7-6-DesignPattern-08-Builder.pillar",
    "Slides/Stable/M7-7-Lang-05-AboutBuilder.pillar",
    "Slides/Stable/M8-6-DesignPattern-12-TypeObject.pillar",
    "Slides/Stable/M9-4-CaseStudy-06-LayeredSettingsArchitecture.pillar",
    "Slides/Stable/M10-2-Principles-09-SubtypingVsSubclassing.pillar",
    "Slides/Stable/M10-3-Principles-10-DynamicStaticType.pillar",
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
    parser = argparse.ArgumentParser(description='Compile Pablo Slides')
    # prefixing the argument with -- means it's optional
    parser.add_argument('-s','--slide', help='slide num to compile')
    args = parser.parse_args()

    filesToCompile = SLIDES
    if(args.slide is not None):
        filesToCompile = [ SLIDES[int(args.slide)] ]

    os.system("mkdir -p "+OUTDIR)

    for pillarfile in filesToCompile:
        pdffile = pillarfile.rsplit('.', 1)[0] + '.pdf'
        MyTerm.print(pillarfile,MyTerm.WARNING)
        cmd = "pillar build pdf "+pillarfile+" && cp _result/pdf/"+pdffile+" "+OUTDIR
        MyTerm.print(cmd)
        os.system(cmd)

if __name__ == '__main__':
    main()
