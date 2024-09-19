{ 
"title" : "Pharo in a Nutshell", 
"slidesid" : "Summer", 
"subtitle" : "" 
} 
 
 
# Outline 
- Pharo? 
- Model 
- Pharo Syntax 
- Vision 
 
# Pharo? 
![ ](figures/pharo.png width=100) 
# Pharo 
- System: Pure object language + full IDE 
- Powerful, elegant and fun to program 
- Living system under your fingers 
- Works on Mac OSX, Linux, iOS, Android, Windows, Pi - 100% MIT 
- Great community / industrial consortium 
 
# Elegant 
- Full syntax on a postcard 
- Simple and powerful objet model 
 
# A Pharo program 
Mainly objects, messages, and lexical closures 
# Full syntax on half a postcard 
![ ](figures/pharo-fullpostcard.png width=80) 
# Zoom on postcard 
![ ](figures/pharo-postcard.png width=50) 
# Temporary declaration, assignment, separator and return 
Temporary variable declaration, assignment, separator, and return 
``` 

| a |

a := 40 + 2.

^ a 
``` 
 
# Lexical closures: Blocks 
- closure definition  
 
``` 
[:x | x + 5] 
``` 
- closure execution  
 
``` 
> [:x | x + 5] value: 37
42 
``` 
 
# Messages 
- Unary messages 
 
``` 
Date today
9 squared 
``` 
- “Operators” Binary  
 
``` 
4 + 3
'Black ', 'Chocolate ', 'is good' 
``` 
- Keywords messages 
 
``` 
2 between: 0 and: 10
2.betweenAnd(0, 10) 
``` 
 
# Control flow operators are messages 
 
``` 
Weather today isRaining 
   ifTrue: [ self takeUmbrella]
   ifFalse: [ self takeSunglasses] 
``` 
- Yes we send messages to Boolean objects 
- \`ifTrue:ifFalse:\` is a method defined on Boolean objects 
 
# Can define your own DSL 
Just add methods to exiting classes 
``` 
False >> siVrai: aBlock1 faux: aBlock2
	^ aBlock2 value  
``` 
 
# Iterators all the way 
 
``` 
> #( 1 -2 -3 4 -5) collect: [:each | each abs]
#( 1 2 3 4 5) 
``` 
Yes we send messages to collection to do loops 
# You can define your own iterator 
 
``` 
#(1 2 3) 
	do: [:each | stream print: each ]
	separatedBy: [ stream << ', ']

1, 2, 3 
``` 
 
# Class definition 
 
``` 
Object << #Point
	slots: { #x . #y };
	package: ‘Kernel' 
``` 
 
# Class definition (old) 
 
``` 
Object subclass: #Point
	instanceVariableNames: 'x y'
	classVariablesNames: ''
	package: ‘Kernel' 
``` 
 
# Method definition 
 
``` 
<= aPoint 
	"Answer whether the receiver is neither below nor to the right of aPoint."
	^ x <= aPoint x and: [y <= aPoint y] 
``` 
	 
- Dynamically typed 
- Everything is an instance of a class 
- All methods are public virtual \(can be packaged outside their class\) 
- All attributes are protected 
- Single inheritance 
- Stateful traits 
- Closures everywhere 
 
# More advanced 
- Classes are objects 
- Instance variables are first class with a meta object protocol 
- Stack can be reified on demand 
- AST can be fully annotated and transformed on the fly during execution 
- Exceptions are manipulable 
 
# Reflective 
![ ](figures/pharo-reflective.png width=95) 
# As modeling language 
- Focus on intrinsic complexity 
- Eliminate accidental complexity 
 
# Enabler 
- Learn  
- Adapt 
- Modify/Model 
 
# Usually 
A language is a black box 
# Introspective 
![ ](figures/pharo-introspective.png width=95) 
# Immersive 
![ ](figures/pharo-immersive.png width=95) 
# Each time the code is compiled the 3D changes 
![ ](figures/pharo-immersive2.png width=95) 
# Immersion all the way down 
We can do the same with web app, sockets, networks, sensors, living programing…. 
# Pharo's goals 
![ ](figures/pharo-immersive2.png width=95)