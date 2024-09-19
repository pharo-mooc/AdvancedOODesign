{ 
"title" : "Distributing Responsibility", 
"subtitle" : "" 
} 
 
# Building map from specification 
 
``` 
| importer game |
importer := SkBoardImporter new. 
game := importer buildMapFor: 
'######
#@$ . #
#######'. 
``` 
 
# Building map from specification 
 
``` 
SkBoardImporter >> buildMapFor: aString

	self buildEmptyFor: aString.
	lines doWithIndex: [ :aLine :lineNumber |
		aLine doWithIndex: [ :aChar :columnNumber |
			| new | 
			new := (self classFor: aChar) new.
			game initializeElement: new atLine: lineNumber column: columnNumber ] ].
	game finalize.
	^ game 
``` 
 
# Building map from specification 
 
``` 
SkBoard >> finalize
	"A player and boxes should have a previous location set as ground."

	player previousBackground: (SkGround new position: player position; yourself).
	map do: [ :each | ( each isKindOf: SkBox )
		ifTrue: [ each previousBackground: (SkGround new position: each position; yourself)] ].
	self identifyPlayerAndBoxes 
``` 
 
``` 
SkBoard >> identifyPlayerAndBoxes

	player := map detect: [ :each | each  isPlayer ].
	boxes := OrderedCollection new.
	map do: [ :each | each isBox ifTrue: [ boxes add: each ] ] 
``` 
 
# Analysis 
- Responsibilities are concentred in Board 
- Forced to check to identify element 
 
# Preparing holding boxes 
 
``` 
SkBoard >> initialize
	super initialize.
	boxes := OrderedCollection new. 
	
SkBoard >> addBox: aBox
	boxes add: aBox	 
``` 
 
# Introducting a hook 
 
``` 
SKBoard >> initializeElement: anElement 
	atLine: lineNumber 
	column: columnNumber
	
	anElement setBoard: self.
	anElement position: columnNumber @ lineNumber.
	self atRow: lineNumber atColumn: columnNumber put: anElement.
	anElement postCreationAction 
``` 
 
# Specialization of hook 
 
``` 
SKElement >> postCreationAction
	self 
``` 
 
``` 
SKPlayer >> postCreationAction 
	board setPlayer: self.
	self previousBackground: self newGround 
``` 
 
``` 
SkBox >> postCreationAction 
	board addBox: self.
	self previousBackground: self newGround 
``` 
 
``` 
SKMovable >> newGround
	^ (SkGround new position: self position; yourself) 
``` 
 
#  Removing useless methods 
- No need for `finalize` 
- No need for `identifyPlayer` 
 
# Conclusion 
- No need to check and query 
- No need  
