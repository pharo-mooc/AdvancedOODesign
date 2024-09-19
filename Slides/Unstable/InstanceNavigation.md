{
"title" : "Instance Tree Navigation",
"subtitle" : "",
"author" : "S. Ducasse"
}

# Goal
- How can we navigate an instance tree?
- With optional states that can be skipped

# The case

```
MainPresenter >> model
	^ aModel
```

```
MainPresenter >> initializePresenters
	super initializePresenters.
	widgetOne := self instantiate: WidgetOnePresenter.
```

```
WidgetOnePresenter >> initializePresenters
	super initializePresenters.
	widgetTwo := self instantiate: WidgetTwoPresenter.
```

```
WidgetTwoPresenter >> initializePresenters
	super initializePresenters.
	...
```

# The question
How WidgetTwoPresenter can access model of the main presenter?
```
WidgetTwoPresenter >> action...

	...
	self owner owner model
	
```
- Not good it hardcodes the instance tree structure

# Passing explicitly a model around

```
MainPresenter >> model
	^ aModel
```

```
MainPresenter >> initializePresenters
	super initializePresenters.
	widgetOne := self instantiate: WidgetOnePresenter on: aModel.
```

```
WidgetOnePresenter >> initializePresenters
	super initializePresenters.
	widgetTwo := self instantiate: WidgetTwoPresenter on: aModel.
```

```
WidgetTwoPresenter >> initializePresenters
	super initializePresenters.
	...
```

# Another Possible Solution

```
SpPresenter >> definedModelOrNil
	"Returns the defined model if it is defined or nil.
	By default return nil"
```

```
SpPresenter >> model
	"Assume that there is at least an owner defining a model in the presenter instance tree."
	^ self definedModel
		ifNil: [ self owner model ] 
```
We recurse dynamically in the instance structure
# Possible Application

```
Main >> definedModelOrNil
	^ model
```

```
WidgetTwoPresenter >> action...

	...
	self model
	
```

# Conclusion
- 
