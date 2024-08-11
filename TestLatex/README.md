This folder is to test Latex and not Pillar. 

### First checking that everything is working 


#### Generate the latex file and folder 

```
pillar build pdf TestLatex/AAA.pillar
```

This creates a new _result folder with all the files and the correct pdf



###  Producing the PDF 

```
latexmk _result/pdf/TestLatex/AAA.tex -pdflatex=lualatex  -pdf -ps- -f -interaction=nonstopmode -outdir=_resultLua
```

This is working. 


### Not working attempts

Now let us try to just focus on the PDF generation from the tex file

```
lualatex _result/pdf/TestLatex/AAA.tex -pdf -ps- -f -output-dir=luaResult
```

The previous expression succeeds in the advanced Mooc directory
Clean the repo since 

```
-output-dir=
-output-directory=
```
never worked! passing relative or absolute paths

```
rm AAA.*
```

### To copy the behavior of Pillar 

in Pillar we got this

```
postWriteTransform: aFile

	| relativePath outputFileReference |
	self halt.
	relativePath := file file asAbsolute relativeTo: project baseDirectory asAbsolute.
	outputFileReference := outputDirectory resolve: relativePath parent.
	self
		executeCommand: 'latexmk'
		arguments: {
			'-pdflatex=lualatex' . 
			'-pdf' .
			'-ps-' .
			'-f' .
			'-interaction=nonstopmode' .
			'-outdir=', (self toCommandPath: outputFileReference fullName).
			self toCommandPath: (PRLaTeXWriter toLatexPath: (aFile relativeTo: outputDirectory) pillarPrintString) }
		workingDirectory: outputDirectory fullName
```


### Checking that everything works if we copy the _support file

Now we copy the _support folder and the latex one to check

from the directory of advanced mooc

```
rm -rf /tmp/testing
mkdir /tmp/testing
cp -r _result /tmp/testing/_result
cd /tmp/testing/
```

- I do not get why this crap of latex does not find the figures of the support since they are copied.


- So the beamer file contains references that latex cannot resolve so edit the files and remove the last 
slides from the generated tex file. -> This does not work either. 

- added icon-pharo.png in figure -> this does not work either

- Let us look at the Pillar invocation.

The pillar invocation is in abosolute paths 

```
latexmk /tmp/testing/_result/pdf/TestLatex/AAA.tex -pdflatex=lualatex  -pdf -ps- -f -interaction=nonstopmode -outdir=/tmp/testing/_resultLua
```

This does not change.

### So working in this repo

Making lualatex in another repo is a hell and I could not find a way to make it work. 
So I did the following: 
- I introduced two little commands to switch configurations toMDConf.sh and toPillarConf.sh
- Note that the converter from pillar slide to microdown slides in the released version of pillar is not correct since it does not emit a cr befor a code block so I pasted a correct version of AAA.md to be able to continue to work on the #=0 problem.

```
toMDConf.sh
/Users/ducasse/Documents/Pharo/vms/120-x64/Pharo.app/Contents/MacOS/Pharo /Users/ducasse/Documents/Pharo/images/p12-PillarAgain1/p12-PillarAgain1.image  clap build pdf TestLatex/AAA.md
```

### Found the problem

In the configuration of advanced mooc we do not specify the template so it uses the in _support and this one was edited by luc. 

```
{
  "title":"My First Presentation - The main title",
  "subtitle": "and a cool sub",
  "author": "Joe Rabbit",
  "complement" : "Rabbit Corp 4.0",
  "date": "March 2020",
  "latexWriter" : #micBeamer
}
```
In the archetype the configuration uses: 

```
{
  "title":"My First Presentation - The main title",
  "subtitle": "and a cool sub",
  "author": "Joe Rabbit",
  "complement" : "Rabbit Corp 4.0",
  "date": "March 2020",
  "latexWriter" : #micBeamer,
  "template" : "slides.pharobeamer.template"
}
```

And this template has certainly a problem in the beamer template listing and it breaks when used.

Ok now it works! so this means that the #a=0 is a problem with the template in the archetype!
