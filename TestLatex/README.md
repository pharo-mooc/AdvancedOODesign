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

This is working


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

I do not get why this crap of latex does not find the figures of the support since they are copied.

