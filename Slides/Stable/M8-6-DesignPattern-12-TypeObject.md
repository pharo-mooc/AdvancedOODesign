{ 
"title" : "TypeObject",
"subtitle" : "",
"slidesid" : "M8-6" 
} 
 
 
# Goals

- Individuals and their description 
- Another form of sharing 
- TypeObject 
 
# Analysing a case 

- Imagine that you have a cactus collection and you want to manage them 
- There is a difference between one plant and its kind 
Gymnocalycium mihanovichii \(a south american well known cactus\)![](figures/Gymno.png width=60) 

# An individual vs. its description

- You can several G. Mihanovichii and each one can be different 
- Different flowers, pest attacks, ... 
![](figures/Gymnos.png width=60) 

# Still one description of their kind 
![](figures/succu.png width=60) 

# Video Rental 
- There is a difference between a video description and the actual BlueRay you have in your hand. 
- The description describes all the RamboIII Blueray 
- A given blueray can be scratched and its box broken 
![](figures/rambo3.png width=60) 

# How to implement this? 
- Should we implement all the descriptions on the class level? 
- Should we have a separate class? 
 
# All in class level 
- Putting all the description information at the class level could work 
- Cannot change dynamically 
- Our instance can get big easily 
- Duplicated information in all instances 
- Cannot be shared between different kinds of objects 
 
# TypeObject 

- Introduce a TypeObject whose responsibility is to gather description-specific properties 
- `PlantDescription` vs `Plant` 
- We can share the description instance 
- Information is not repeated in many objects 
![](figures/TypeObject.pdf width=80) 

# TypeObject (II) 
- Define instance-specific properties in typed object class 
- Define instance description specific properties in the `TypeObject` associated with the typed Object 
 
``` 
Plant
	age, size, lastPestAttack, flowerColor 
``` 
 
``` 
PlantDescription
	otherNames, countries, cultivars 
``` 
 
# Dynamic TypeObjects 
- Depending on your domain the typed object and TypeObject relationship can be dynamic 
- The description evolves with the program 
- Changing one description affects all described instances 
 
# Conclusion 
TypeObject: 
- makes explicit the relation to the object description 
- encapsulates state and behaviour that is common to a type of objects 
- is a dynamic way of handling descriptions 
