{
"title" : "Class and Method Definitions",
"subtitle" : "",
"slidesid" : "W1S06"
}

# Class and Method Definitions in Pharo
- classes and methods are defined within tools
- there is no dedicated syntax

# Class Definition in Pharo
![](figures/PointClass.png width=98)
# Class Definition is a Message

```
Object subclass: #Point
  instanceVariableNames: 'x y'
  classVariableNames: ''
  package: 'Graphics'
```
We send the message `subclass:inst....` to the superclass to create the class
# Method Definition in Pharo
![](figures/FactorialInBrowser.png width=98)
# Method Definition in Pharo

```
factorial
  "Answer the factorial of the receiver."
  self = 0 ifTrue: [ ^ 1 ].
  self > 0 ifTrue: [ ^ self * (self - 1) factorial ].
  self error: 'Not valid for negative integers'
```
In which class is `factorial` defined?
# Presentation Convention
In this lecture, a method will be displayed as
```
Integer >> factorial
  "Answer the factorial of the receiver."
  self = 0 ifTrue: [ ^ 1 ].
  self > 0 ifTrue: [ ^ self * (self - 1) factorial ].
  self error: 'Not valid for negative integers'
```
- **Integer >>** is not part of the syntax
  - it tells you the method's class

# Presentation Convention
![](figures/FactorialInBrowser.png width=80)In Pharo, the method belongs to the selected class
# Remember Messages

```
Integer >> factorial
  "Answer the factorial of the receiver."

  self = 0 ifTrue: [ ^ 1 ].
  self > 0 ifTrue: [ ^ self * (self - 1) factorial ].
  self error: 'Not valid for negative integers'
```
- `factorial` is the method name
- `=`, `>`, `*` and `-` are binary messages
- `factorial` is an unary message
- `ifTrue:` and `error:` are keyword messages
- the caret `^` is for returning a value

# A Method Returns self by Default

```
Game >> initializePlayers
  self players
    at: 'tileAction'
    put: ( MITileAction director: self )
```
is equivalent to
```
Game >> initializePlayers
  self players
    at: 'tileAction'
    put: ( MITileAction director: self ).
  ^ self       "<-- optional"
```

# Class Methods
<!columns|width=100

<!column|width=60

![](figures/Point-xy-class-method.png width=90)
!>

<!column|width=40

- press the button `class` to define a class method
- in lectures, we add `class`

!>


!>

```
Point class >> x: xInteger y: yInteger 
  "Answer an instance of me with coordinates xInteger and yInteger."

  ^ self basicNew setX: xInteger setY: yInteger
```

# What You Should Know
- A class is defined by sending a message to its superclass 
- Classes are defined inside packages
- Methods are public
- By default a method returns the receiver, `self`
- Class methods are just methods of the class side

%  Local Variables:
%  compile-command: "cd ../.. && ./compile.sh --to=Beamer Slides/Week1/C019-W1S06-ClassAndMethodDefinition.pillar"
%  End: