This folder is to test Latex and not Pillar. 
So first 

```
pillar build pdf TestLatex/AAA.pillar
```

This creates a new _result folder with all the files and the correct pdf


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


Trying 

```
latexmk _result/pdf/TestLatex/AAA.tex -pdflatex=lualatex  -pdf -ps- -f -interaction=nonstopmode -outdir=_resultLua
```



Now in Pillar we got this

```
postWriteTransform: aFile	| relativePath outputFileReference |	self halt.	relativePath := file file asAbsolute relativeTo: project baseDirectory asAbsolute.	outputFileReference := outputDirectory resolve: relativePath parent.	self		executeCommand: 'latexmk'		arguments: {			'-pdflatex=lualatex' . 			'-pdf' .			'-ps-' .			'-f' .			'-interaction=nonstopmode' .			'-outdir=', (self toCommandPath: outputFileReference fullName).			self toCommandPath: (PRLaTeXWriter toLatexPath: (aFile relativeTo: outputDirectory) pillarPrintString) }		workingDirectory: outputDirectory fullName
```