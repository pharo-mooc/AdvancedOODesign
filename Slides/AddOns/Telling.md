{
	"title":"Tell as an alternative to ask"
}


<!slide|title=File metadata 

- Should be the first element of the main file
- Attach to the document to play well within Pillar compilation chain

!>


<!slide|title=Studying the parser

```
MicrodownParser >> parse: aStreamOrString
	"returns the root node of aStreamOrText"

	| inStream line |
	current := root := self newRootBlock
		setParser: self;
		yourself.
	....
	whileFalse: [ 
		self handleLine: line ].
	...
	root hasMetaDataElement 
		ifTrue: [ root properties: root metaDataElement body ].
	^ root
```
!>



