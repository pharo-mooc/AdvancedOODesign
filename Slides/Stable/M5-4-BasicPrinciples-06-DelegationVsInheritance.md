{ 
"title" : "Delegation vs. Inheritance", 
"slidesid" : "M5S4", 
"subtitle" : "Basic but worth" 
} 
 
# Goals 
- Delegation-based and inheritance-based designs 
- Compare designs using criteria/hints 
 
# Exercise setup 
Imagine the class `TextEditor` and the definition of several algorithms: 
- `formatWithTeX(t)` to color TeX 
- `formatFastColoring(t)` to fastly color the text 
- `formatSlowButPreciseColoring(t)` to color ... 
- `formatRTF(t)` 
- ... 
How can we create an editor that will format differently different texts? 
# Agenda 
- Two first solutions: 
  - with inheritance 
  - with one class and conditionals 
- Define some criteria to compare solutions 
- A third solution with delegation 
- Evaluation 
 
# With inheritance 
<!columns|width=100 
 
<!column|width=52 
 
 
``` 
Object << #TextEditor
    slots: { #text }

TextEditor >> format
    self subclassResponsability 
``` 
 
``` 
SlowFormatingTextEditor >> format
	 self formatSlowButPreciseColoring: text 
``` 
 
``` 
FastFormatingTextEditor >> format
	 self formatFastColoring: text 
``` 
 
``` 
NullFormatingTextEditor >> format
	^ self "do nothing" 
``` 
 
!> 
 
<!column|width=48 
 
![.](figures/textEditorHierarchy.pdf width=106) 
!> 
 
 
!> 
 
# With one class and conditionals 
![.](figures/textEditorSingle.pdf width=30) 
``` 
TextEditor >> format
	currentSelection = #slow
		ifTrue: [ self formatSlowButPreciseColoring: text]
		ifFalse: [
            currentSelection = #fast
                ifTrue: [self formatFastColoring: text]
			....
        ] 
``` 
 
# With one class, a registry and meta-programming 
 
``` 
Object << #TextEditor
    slots: { #currentSelection. #formatters. #text } 
``` 
 
``` 
TextEditor class >> initialize
	self formatters
		at: #slow put: #slowFormat: ;
		at: #fast put: #fastFormat: ;
		at: #null put: #nullFormat: ;
		at: #tex put: #texFormat: 
``` 
 
``` 
TextEditor >> format
	self perform: (formatters at: currentSelection) with: text 
``` 
 
# How to compare solutions? 
Some criteria: 
- **Addition** 
  - What is the cost to define a new formatting algorithm? 
- **Packaging** 
  - Can I deploy a new formatting algorithm separately from others? 
- **Dynamic switch** 
  - Can I dynamically switch to another formatting algorithm? 
 
# Evaluating inheritance-based solution 
<!columns|width=100 
 
<!column|width=75 
 
**Pros:** 
- Addition: adding a new formatting algorithm is done by subclassing 
- Packaging: formatting algorithms are modularised in separate classes 
**Cons:** 
- Dynamic switch 
  - Have to create the right `TextEditor` at beginning 
  - Difficult to **change** it dynamically \(external references\) and we do not want to reopen the text editor 
- Addition: combinatorial explosion 
 
!> 
 
<!column|width=25 
 
 
!> 
 
 
!> 
 
# Evaluating inheritance-based solution 
<!columns|width=100 
 
<!column|width=55 
 
- Do not want a hierarchy for each text editor features to be multiplied with previous ones \(Single/Multi-Pane, completion, grammatical verification, compilation,....\) 
- API of TextEditor can get large: no clear identification of responsibilities 
 
!> 
 
<!column|width=45 
 
![.](figures/textEditorHierarchyBloated.pdf width=100) 
!> 
 
 
!> 
 
# Evaluating conditionals-based solution 
<!columns|width=100 
 
<!column|width=70 
 
**Pros:** 
- Dynamic switch: we can use a different formatting algorithm dynamically 
**Cons:** 
- Addition: adding a version requires to edit and **recompile** the conditionals 
- Packaging: we cannot package a new algorithm separately 
 
!> 
 
<!column|width=30 
 
 
!> 
 
 
!> 
 
# Solution with delegation 
Imagine a solution using delegation to another object \(a formatter\) 
# Delegating to a formatter 
![.](figures/textEditorStrategy.pdf width=70) 
``` 
myEditor formatter: FastFormatter new.
myEditor format.
myEditor formatter: SlowFormatter new. 
``` 
 
# Evaluating the delegation to a formatter 
**Pros:** 
- Addition: just add a new formatter subclass 
- Packaging: formatting algorithms are well **modularised** in separate classes 
- Dynamic switch: just create a new formatter instance and set it in the editor 
- Uniform API between the Editors and the Formatters \(`format:`\) 
**Cons:** 
- The formatter should access the state of the text \(i.e. the text, positions... contained in the text editor\) 
- The API of the TextEditor should be opened to support it 
BTW, this is a typical example of the **Strategy Design Pattern** ;-\) 
# Conclusion 
Inheritance 
- is about **incremental static** definition 
- can lead to static design 
- helps defining **abstractions** 
Delegation 
- brings runtime **flexibility** and modularity 
but there's no such thing as a free lunch! 
