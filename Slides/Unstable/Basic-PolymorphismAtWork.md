{
"title" : "Polymorphism at work",
"subtitle" : "",
"author" : "foobar"
}


# Goal
- Changing your view 
- Multiple classes/objects can collaborate to achieve a behavior

# A little exercise
How to implement `flatten`?
```
testBasic 

	self assert: #((1 2) (3) 4) flatten equals: #(1 2 3 4).
	self assert: #(((1 2) 5) (3) 4) flatten equals: #(1 2 5 3 4).
```

# With a little requirement

```
testBasicEliminatingNil

	self assert: #((1 nil 2) nil (3) 4) flatten equals: #(1 2 3 4).
	self assert: #(((1 nil 2)) nil (3) 4) flatten equals: #(1 2 3 4).
	self assert: #(nil) flatten equals: #()
```

# A possible first "solution"
For an alternative `flattenArray:` message: `Object new flattenArray:  #((1 nil 2) nil (3) 4)`
```
Object >> flattenArray: aCollection
	^ (OrderedCollection
		streamContents: [ :stream | self flatten: aCollection into: stream ]) asArray
```

```
Object >> flatten: anObject into: result
	^ anObject isCollection
		ifTrue: [ anObject do: [ :item | self flatten: item into: result ] ]
		ifFalse: [ anObject ifNotNil: [ result nextPut: anObject ] ]
```

# Analysis
- `isCollection` is a disguised typecheck.
- For normal objects we always do two tests: `isCollection` and `ifNotNil:` 
- Can we express the same without all these tests?

# A much nicer solution

```
Collection >> flatten
	^ (OrderedCollection 
		streamContents: [ :stream | self flattenInto: stream ]) asArray
```

```
Object >> flattenInto: result
	result nextPut: self
```

```
Collection >> flattenInto: result
	self do: [ :item | item flattenInto: result ]
```
	
To handle nil
```
UndefinedObject >> flattenInto: result
	^ self
```

# Remember
- Sending a message is making a choice.
- We have three version of `flattenInto:`.
- Late binding at execution pick the right one. 
