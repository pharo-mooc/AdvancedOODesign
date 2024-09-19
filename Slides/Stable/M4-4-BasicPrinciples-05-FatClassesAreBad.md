{ 
"title" : "Fat classes are bad", 
"slidesid" : "M4S4", 
"subtitle" : "a.k.a. A large class vs. a class hierarchy" 
} 
 
# Goals 
- Remember the _Implementing Not_ Lectures 
- _Transform Self Type Check_ Object-Oriented Reengineering pattern 
 
# Example: BibTeX 
 
``` 
@inproceedings{Scha03a,
  author = {N. Schaerli and S. Ducasse and O. Nierstrasz and A. P. Black},
  title = {Traits: Composable Units of Behavior},
  booktitle = {ECOOP},
  publisher = {Springer Verlag},
  year = {2003}}

@article{Teso20b,
  author = {P. Tesone and S. Ducasse and G. Polito and L. Fabresse ...},
  title = {A new modular implementation for Stateful Traits},
  journal = {Science of Computer Programming}, ...}

 @book{Duca22a,
    author = {S. Ducasse and G. Rakic and  ...},
    title = {Pharo by Example},
    publisher = {Keepers of the lighthouse},
    url = {http://books.pharo.org}} 
``` 
 
# Example: BibTeX 
- Different entries: inproceedings, book, article, techreport, phd.... 
- Different fields: key, year, institution, booktitle, title... 
 
# A single class in Citezen :( 
 
``` 
CZScoped << #CZEntry
	slots: { #type . #key . #fields };
	sharedVariables: { #ExtendedFieldKeys . #FieldKeysToRemove };
	sharedPools: { CZFieldPool };
	package: 'Citezen-Model' 
``` 
 
# isSomething methods 
 
``` 
isArticle
	^ self type = #article 
``` 
 
``` 
isBook
	^ self type = #book 
``` 
It is always worth to have a look at users of these `isSomething` methods 
# Another example: CZField 
 
``` 
CZScoped << #CZField
	slots: { #key . #value };
	package: 'Citezen-Model' 
``` 
 
``` 
CZField >> isDoi
	^ key = #doi 
``` 
 
# Consequence 
 
``` 
CZField >> visitField: aField
	self outputStream nextPutAll: '<span class="', aField key,'">'.
	aField isPDF
			ifTrue: [outputStream nextPutAll: '<a href="'].
	aField isURL
		ifTrue: [outputStream nextPutAll: '<a href="'].
	aField isDoi
		ifTrue: [outputStream nextPutAll: '<a href="https://doi.org/'].	
	aField dispatchVisitor: self.
	aField isURL
		ifTrue: [outputStream nextPutAll: '">URL</a>'].
	aField isDoi
		ifTrue: [outputStream nextPutAll: '">DOI</a>'].
	aField isPDF
			ifTrue: [outputStream nextPutAll: '">PDF</a>'].
	outputStream nextPutAll: '</span>'. 
``` 
 
# When using a Fat class 
Not having a class hierarchy:  
- **Impossible to dispatch** logic because there is **only one** class  
- Simple extensions require **many changes** to the conditional code 
- Difficult subclassing **without duplicating/adapting** the methods containing the conditional code 
- Adding a new behavior always results in: 
  - changes to the same set of methods and  
  - adding a new case to the conditional code 
- Remember the Implementing Not Lectures 
 
# Two kinds of type checking conditionals 
**Self type checks** 
- check some internal values to invoke self methods 
- not that bad 
**Client type checks** 
- Violate The **do not ask, tell** principle 
- Defeat late binding and inverse the flow of control 
- Unnecessary in a large class 
 
# Transform self type transformation 
![](figures/TransformSelfType.png width=90) 
% ${slide:title=The case of the Memento Design Pattern}$ 
% Sometimes you need to be able to edit a temporary version of an object 
% - Memento allows one to save and reload the state of an object without revealing implementation details 
% - To have a generic Memento we can use a kind of dictionary to hold field values of the copied object.  
# Conclusion 
- Favor dispatch 
- Create classes to encapsulate knowledge 
- Apply the **Do not ask, tell** principle 
- Read _Object-Oriented Reengineering Patterns_ 
