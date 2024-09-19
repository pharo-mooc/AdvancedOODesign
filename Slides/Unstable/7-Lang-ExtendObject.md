{ 
"title" : "About extending objects",
"subtitle" : "",
"author" : "S. Ducasse" 
} 
 
# Goal 
- Revisit conditional 
- Think about visibility 
 
# Recall 
- `x isKindOf: Class` or `x class = Class` are against OOP 
- Do not ask, tell 
 
# About class extension 
In Pharo a package can define a method in a class that is not in the extending package. 
- Powerful mechanism. 
- Here STEF 
 
# About isFoo methods 
- Be suspicious about conditional logic 
- An isFoo \(isArray, isPair, ...\) is still a conditional and asking form 
- It does not support a tell \(from Do not ask, Tell\)  
 
# About isFoo methods 
 
``` 
printOn: stream

	stream nextPutAll: self label.
	model isCollection
		ifTrue: [ 
			model
				do: [ :node | node printOn: stream ]
				separatedBy: [ stream << ', ' ] ]
		ifFalse: [ model printOn: stream ] 
``` 
- Why the model cannot be a collection? 
- It can be a collection with a single element or more. 
