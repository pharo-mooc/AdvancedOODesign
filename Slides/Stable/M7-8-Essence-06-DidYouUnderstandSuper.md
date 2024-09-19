{ 
"title" : "Did You Really Understand Super?",
"subtitle" : "",
"slidesid" : "M7-8" 
} 
 
# What you will learn 
Revisit 
- `super` 
- Message lookup 
- Class methods 
 
# A little puzzle 
 
``` 
Die class >> new

  | inst |
  inst := super new.
  inst initialize.
  ^ inst 
``` 
We execute the following expression: `Die new` 
# Questions 
 
``` 
Die class >> new

  | inst |
  inst := super new.
  inst initialize.
  ^ inst 
``` 
- What is `inst`? 
- What is `super`? 
- What is `super new`? 
 
# Hint: super is Not... 
 
``` 
Die class >> new

  | inst |
  inst := super new.
  inst initialize.
  ^ inst 
``` 
- No, `super` is not the superclass 
- No, `inst` is not an instance of the superclass 
 
# Hint 2: super is the message receiver 
 
``` 
Die class >> new

  | inst |
  inst := super new.
  inst initialize.
  ^ inst 
``` 
- The message is `Die new` 
- So the receiver is the class `Die` 
 
# Sending a message: Lookup + execute on receiver 
![](figures/InheritanceDiagram-sendingMessage.png width=40) 
# Remember: Method lookup 
![](figures/LookupEssenceWithGeneric.png width=55) 
# Solution 
 
```language=smalltalk 
Die class >> new

  | inst |
  inst := super new.
  inst initialize.
  ^ inst 
``` 
- `super` is the receiver: the class `Die` 
- Look for `new` in the superclass of the class `Die class` \(Pay attention not `Die`\) 
- Once found we apply to the receiver: `Die` 
- We get an instance of the class `Die` and send it initialize and return it 
 
# Solution 
![](figures/Workstation-Dice-MetaclassesWithInheritanceWithLookup.png width=80) 
# Summary 
- Sending a message is looking up the method and applying it on the receiver 
- Now you should really understand `super` :\) 
- `super` is the receiver of the message and the method lookup starts in the superclass of the class  containing the expression 
 
# Challenge yourself 
Imagine we have: 
``` 
A >> foo
   ^ super class == self class 
``` 
What is the result of `A new foo` and why?