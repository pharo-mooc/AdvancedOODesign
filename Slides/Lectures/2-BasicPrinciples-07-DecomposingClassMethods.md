{ 
"title" : "About class methods",
"subtitle" : "",
"author" : "S. Ducasse" 
} 
 
 
# Studying a simple example 
 
# Building a board 
 
``` 
Board >> buildMapWidth: x height: y
	map := Array2D 
				rows: y 
				columns: x 
				tabulate: [ :row :column |
					self initializeElement: self groundClass new atLine: row column: column ] 
``` 
 
# Placing the back pointer  
 
``` 
Board >> initializeElement: anElement atLine: lineNumber column: columnNumber

	anElement setBoard: self.
	anElement basicPosition: columnNumber @ lineNumber.
	self atRow: lineNumber atColumn: columnNumber put: anElement.
	anElement postCreationAction. 
``` 
 `self atRow: lineNumber atColumn: columnNumber put: anElement.` cannot work because the board map 
 is not finished to be created. 
# Class creation 
 
``` 
Array2D class >> rows: rowNumber columns: columnNumber tabulate: aTwoArgumentBlock
	"Answer a new Matrix of the given dimensions where
	 result at: i at: j is aTwoArgumentBlock value: i value: j"
	|a i|
	a := Array new: rowNumber*columnNumber.
	i := 0.
	1 to: rowNumber do: [:row |
		1 to: columnNumber do: [:column |
			a at: (i := i + 1) put: (aTwoArgumentBlock value: row value: column)]].
	^ self rows: rowNumber columns: columnNumber contents: a 
``` 
- It feels like too much is done on the class side. 
 
# New instance behavior 
 
``` 
Array2D >> rowsColumnsDo: aTwoArgumentBlock
	"Set the value at row,colum as the value of aTwoArgumentBlock with row and column as inputs."

	| i |
	i := 0.
	1 to: numberOfRows do: [:row |
		1 to: numberOfColumns do: [:column |
			contents at: (i := i + 1) put: (aTwoArgumentBlock value: row value: column)]]. 
``` 
 
# Revisiting class  
 
``` 
Array2D class >> rows: rowNumber columns: columnNumber tabulate: aTwoArgumentBlock
	"Answer a new array2d of the given dimensions where
	 result at: i at: j is aTwoArgumentBlock value: i value: j"

	| newArray |
	newArray := self rows: rowNumber columns: columnNumber.
	newArray rowsColumnsDo: aTwoArgumentBlock.
	^ newArray 
``` 
 
# Now this is possible 
 
``` 
Board >> buildMapWidth: x height: y

	map := Array2D rows: y columns: x.
	map rowsColumnsDo: [ :row :column |
		self initializeElement: self groundClass new atLine: row column: column ] 
``` 
