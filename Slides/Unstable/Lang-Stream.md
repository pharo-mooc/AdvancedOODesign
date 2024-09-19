{ 
"title" : "Basic about asString and printString",
"subtitle" : "",
"author" : "S. Ducasse" 
} 
 
# Goal 
- Think about intermediary object creation 
- How to avoid spurious objects 
- `asString` and `printString` inside `printOn:` 
 
# printString: setting the stage 
 
``` 
Object >> printString
		"Answer a String whose characters are a description of the receiver. 
		If you want to print without a character limit, use fullPrintString."

		^ self printStringLimitedTo: 50000
		
Object >> printStringLimitedTo: limit
	"Answer a String whose characters are a description of the receiver.
	If you want to print without a character limit, use fullPrintString."

	^self printStringLimitedTo: limit using: [:s | self printOn: s] 
``` 
 
# printString creates its own stream! 
 
``` 
printProtocol: protocol sourceCode: sourceCode

	^ String streamContents: [ :stream |
		stream
			nextPutAll: '"protocol: '; 
			nextPutAll: protocol printString;
			nextPut: $"; cr; cr;
			nextPutAll: sourceCode ]	 
``` 
`protocol printString` 
- Creates a new stream 
- Get its contents to be able to put in the first stream 
 
# Better use print: 
 
``` 
printProtocol: protocol sourceCode: sourceCode

	^ String streamContents: [ :stream |
		stream
			nextPutAll: '"protocol: '; 
			print: protocol;
			nextPut: $"; cr; cr;
			nextPutAll: sourceCode ]	 
``` 
 
``` 
Stream >> print: anObject
	"Have anObject print itself on the receiver."

	anObject printOn: self 
``` 
 
# The case of displayStringOn: 
- When we get a stream, better use it directly 
 
``` 
MessageTally >> displayStringOn: aStream
	self displayIdentifierOn: aStream.
	aStream 
		nextPutAll: ' (';
		nextPutAll: self tally printString;
		nextPutAll: ')' 
``` 
`self tally printString` 
- Creates a new stream 
- Get its contents to be able to put in the first stream 
 
# Better 
 
``` 
MessageTally >> displayStringOn: aStream
	self displayIdentifierOn: aStream.
	aStream 
		nextPutAll: ' (';
		print: self tally;
		nextPutAll: ')' 
``` 
- No creation of intermediary streams 
 
# Conclusion 
- Let the object decide if it wants to join a process but passing a container 
