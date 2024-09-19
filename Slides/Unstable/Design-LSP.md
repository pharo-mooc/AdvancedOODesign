{ 
"title" : "About Liskov Substitution Principle ",
"subtitle" : "",
"slidesid" : "From the Design Corner" 
} 
 
# Goal 
- Pay attention there are different notions of subtyping 
- Liskov subtyping is about **behavioral** subtyping 
- Behavioral subtyping looks not really compatible with OOP incremental definition 
- LSP is a theorical thought without practical impact for OOP 
- I would like to thank the author of the original lecture I got inspired from 
 
# Liskov Substitution Principle (LSP) 
_ 'if for each object o1 of type S there is another object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2, then S is a subtype of T._'Barbara Liskov, "Data Abstraction and Hierarchy," SIGPLAN Notices, 23,5 \(May 1988\) 
# A Simple Bag 
A Bag as an object that accepts two messages: `add:` and `count:` 
``` 
aBag add: $X 
``` 
puts an element x into the Bag, and 
``` 
aBag occurrenceOf: $X 
``` 
gives the count of occurrences of x in the receiver 
# A Simple Set 
A Set as an object that accepts two messages: `add:` and `count:` 
``` 
aSet add: $X 
``` 
puts an element x into the Set, and 
``` 
aSet occurrenceOf: $X 
``` 
gives the count of occurrences of x in the receiver 
# A Bag method 
 
``` 
Bag >> add2
	self add: 5.
	self add: 5.
	^ self count: 5 
``` 
This method is: given a Bag, adds two elements into it and returns 
``` 
	2 + (orig-bag count:  5) 
``` 
 
# A Set cannot be a subtype of a Bag 
You can send `add2` to a Set object as well.  
- Just as a Bag, a Set object accepts messages `add:` and `count:`.  
- However applying `add2` to a Set object will break the method's post-condition 
Passing a set object where a bag was expected changes behavior of some program. According to the Liskov Substitution Principle \(LSP\), a Set is not substitutable for a Bag -- a Set cannot be a subtype of a Bag. 
# A Set method 
 
``` 
Set >> plusOne
	self add: 5.
	^ self count: 5 
``` 
The behavior of this method is: given a Set, adds an element into it and returns 1. 
# A Bag cannot be a subtype of a Set 
- If you send a bag the message `plusOne` the method may return a number greater than 1.  
- Break plusOne contract, which promised always to return 1. 
- Bag cannot be a subtype of a Set 
 
#  About LSP and OOP 
- LSP when considered from an OOP point of view is undecidable 
- LSP is about the same behavior  
- but most of the time when you define subclass to change behavior 
 
#  About LSP and OOP 
- OOP is built on the idea of defining behavior in terms of incremental definition.  
- By definition a subclass often exhibits a slightly different behavior than its superclass. 
- Therefore LSP looks useless in such context. 
 
# Watchout! 
 
# Conclusion 
- Behavioral subtyping is a too 'strong' version of subtyping 
- It is not really useful from a OOP design point of view 
- Just ignore this idea of unchanged behavior 
