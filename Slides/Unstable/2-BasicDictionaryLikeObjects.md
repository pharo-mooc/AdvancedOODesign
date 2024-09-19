{
"title" : "An Object vs. a Class Hierarchy",
"subtitle" : "",
"author" : "S. Ducasse"
}

# Goal
- Remember the Implementing Not Lectures
- Transform Self Type Check Reengineering pattern
- Discussion on Memento

# Example: BibTeX

```
@book{Blac09a,
  author = {Andrew P. Black and St\'ephane Ducasse and Oscar Nierstrasz and Damien Pollet and Damien Cassou and Marcus Denker},
  title = {Pharo by Example},
  publisher = {Square Bracket Associates},
  year = {2009},
  url = {http://books.pharo.org}
}

@inproceedings{Scha03a,
  author = {Nathanael Sch\"arli and St\'ephane Ducasse and Oscar Nierstrasz and Andrew P. Black},
  title = {Traits: Composable Units of Behavior},
  booktitle = {ECOOP},
  pages = {248--274},
  publisher = {Springer Verlag},
  year = {2003}
}

@article{Teso20b,
  author = {Pablo Tesone and St\'ephane Ducasse and Guillermo Polito and Luc Fabresse and Noury Bouraqadi},
  title = {A new modular implementation for Stateful Traits},
  journal = {Science of Computer Programming},
  ...
```

# A single class in Citezen

```
CZScoped << #CZEntry
	slots: { #type . #key . #fields };
	sharedVariables: { #ExtendedFieldKeys . #FieldKeysToRemove };
	sharedPools: { CZFieldPool };
	package: 'Citezen-Model'
```

# Consequences

```
isArticle
	^ self type = #article
```

```
isBook
	^ self type = #book
```
And their senders...
# Another example: CZField

```
CZScoped << #CZField
	slots: { #key . #value };
	package: 'Citezen-Model'
```

# Consequence

```
CZField >> isDoi

	^ key = #doi
```

```
CZField >> visitField: aField

	self outputStream nextPutAll: '<span class="', aField key,'">'.
	(#(#pdf #url #doi) includes: aField key) ifTrue: [ Transcript show: aField; cr ]. 
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
- Not possible to dispatch logic because there is only one class 
- Simple extensions require many changes to the conditional code
- Difficult subclassing without duplicating/adapting the methods containing the conditional code
- Adding a new behavior always results in changes to the same set of methods and always results in adding a new case to the conditional code.
- Remember the Implementing Not Lectures

# Transform self type
![Not implementation](figures/TransformSelfType.png width=80)
# The case of the Memento DP
Sometimes you need to be able to edit a temporary version of an object
- Memento allows one to save and reload the state of an object without revealing implementation details
- To have a generic Memento we can use a kind of dictionary to hold field values of the copied object

# Conclusion
