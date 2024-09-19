{ 
"title" : "Class Methods At Work",
"subtitle" : "",
"slidesid" : "M9S2" 
} 
 
 
# What you will learn 
- In Pharo, class methods are normal virtual methods 
  - methods are looked up dynamically 
- Most class methods create new instances 
  - but they can be used for other things 
 
# Case study: parsing a string 
<!columns|width=100 
 
<!column|width=60 
 
Imagine we want to parse the following string: 
``` 
!Section Title
- list item
-- subitem

Any text here 
``` 
and create the corresponding objects. 
!> 
 
<!column|width=40 
 
 
!> 
 
 
!> 
 
# A possible design 
<!columns|width=100 
 
<!column|width=70 
 
![](figures/items.pdf width=85)Each `DocumentItem` subclass knows 
- if it can parse a line \(`canParse:`\) 
- how to create an instance of itself \(`newFromLine:`\) 
 
!> 
 
<!column|width=30 
 
 
!> 
 
 
!> 
 
# Parsing lines 
<!columns|width=100 
 
<!column|width=70 
 
![](figures/items.pdf width=60) 
``` 
Parser >> documentClasses
	^ DocumentItem allSubclasses
			sorted: [ :class1 :class2 |
                class1 priority < class2 priority ]

Parser >> parse: line
	self documentClasses
		detect: [ :subclass |
			(subclass canParse: line)
			    ifTrue: [ ^ subclass newFromLine: line ] ] 
``` 
 
!> 
 
<!column|width=30 
 
 
!> 
 
 
!> 
 
# The Pharo command-line interface (CLI) 
<!columns|width=100 
 
<!column|width=60 
 
 
```language=bash 
$ pharo Pharo.image eval "10 factorial"
3628800 
``` 
- it uses the same approach 
- each subclass of `CommandLineHandler` processes one type of command 
- the correct subclass is selected by sending messages to the class 
 
!> 
 
<!column|width=40 
 
 
!> 
 
 
!> 
 
# The command-line handler 
 
``` 
CommandLineHandler class >> handlersFor: arguments
    ^ self allHandlers
        select: [ :handlerClass |
            handlerClass isResponsibleFor: arguments ]

CommandLineHandler class >> allHandlers
    ^ self allSubclasses
        reject: [ :handler | handler isAbstract ]

CommandLineHandler class >> isResponsibleFor: arguments
    ^ arguments includesSubCommand: self commandName

EvaluateCommandLineHandler class >> commandName
    ^ 'eval' 
``` 
 
# Evaluation 
**Pros**: 
- Modular design 
- Extensible 
**Cons**: 
- Checking all subclasses all the times is **costly** 
- Do you need such a dynamic behavior? 
  - For the command line, each application may define its own commands 
 
# Conclusion 
- Classes are objects and can be sent messages 
- Method lookup is exactly the same as for all objects: 
  - go to the class of the receiver 
  - follow inheritance chain 
- Pharo makes it easy to iterate over subclasses 
  - it enables modular and extensible design 
  - but this is **costly** 
- Related to the lecture on _Registration_ 
