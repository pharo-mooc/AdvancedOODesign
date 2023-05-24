#!/usr/bin/env python3

import os
import sys
import argparse

OUTDIR="__results.pablo"

SLIDES= [
    "Slides/Stable/M10-2-Principles-09-SubtypingVsSubclassing.pillar",
     "Slides/Stable/M10-3-Principles-10-DynamicStaticType.pillar",
    "Slides/Stable/M5-2-DesignPattern-11-State.pillar",
     "Slides/Stable/M5-5-CaseStudy-01-TurningAProcIntoAnObject.pillar",
     "Slides/Stable/M5-6-Lang-04-BlocksVsObjects.pillar",
     "Slides/Stable/M7-1-Principles-01-LazyInitialization.pillar",
     "Slides/Stable/M7-2-Principles-07-ClassHookVsInstanceHook.pillar",
     "Slides/Stable/M7-6-DesignPattern-08-Builder.pillar",
     "Slides/Stable/M7-7-Lang-05-AboutBuilder.pillar",
     "Slides/Stable/M7-8-Essence-06-DidYouUnderstandSuper.pillar",
     "Slides/Stable/M8-3-Lang-03-SharedPools.pillar",
     "Slides/Stable/M8-5-DesignPattern-10-Flyweigth.pillar",
     "Slides/Stable/M8-6-DesignPattern-12-TypeObject.pillar",
     "Slides/Stable/M9-1-Principles-04-LawOfDemeter.pillar",
     "Slides/Stable/M9-4-CaseStudy-06-LayeredSettingsArchitecture.pillar",
     "Slides/Stable/M5-3-DesignPattern-07-Command-Application.pillar",
	"Slides/Stable/M5-3-DesignPattern-07-Command-Definition.pillar" 
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
