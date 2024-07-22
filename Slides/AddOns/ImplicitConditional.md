{
	"title":"Implicit conditional @ work"
}


<!slide|title=Quest: Nice reporting error

```
![Example of wrong file reference.](brokenpath/foo.pgr)
```

The file 'brokenpath/foo.pgr' in file Chapter/BrokenExample.md is not found.

!>


<!slide|title=Problem: 

- Q1: How do we know the file of an element?
- Q2: How do we know the file of a document?

!>


<!slide|title=Easy for Q2

```
Microdown >> parseFile: aFile
	^  MicrodownParser parse: aFile contents. 
```

becomes 

```
Microdown >> parseFile: aFile
	| root |
	root := MicrodownParser parse: aFile contents. 
	root fromFile: aFile fullName.
	^ root
```

!>



<!slide|title=In MicRootBlock&tag=nh5p

In a document we store the file if available

```
MicRootBlock >> fromFile: aFile 
	"Store the file from which the document was built"
	
	self propertyAt: #file put: aFile
```

!>


<!slide|title=Q2

How do we get the file from any document element?

!>

<!slide|title=Q2

Without condition, of course

!>

<!slide|title=Just tell

Without condition, of course

!>

<!slide|title=Just tell

```
MicRootBlock >> fromFile
	^ self propertyAt: #file 

```
!>

<!slide|title=Q2 cont

What about any element such as figures, inputfile?

```
MicElementBlock >> fromFile
	...
```
!>

<!slide|title=Just delegate

```
MicElementBlock >> fromFile
	"Let us bubble up to the root to get the file"
	^ self parent fromFile

```
!>

<!slide|title=Stepping back

- No need for asking
- There is an implicit condition: a message!

!>
