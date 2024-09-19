{ 
"title" : "About Symbols as Blocks", 
"author" : "S. Ducasse", 
"subtitle" : "" 
} 
 
# Goal 
- Think about communication 
- Reflect on usage 
 
# Symbols as Blocks are handy for scripting 
 
``` 
#(1 2 3 4) select: #even 
``` 
Super nice, fast and handy. 
# Symbols as Blocks have real drawbacks 
- They are SLOW 
- They are making debugging less nice 
- They do not communicate well intention 
 
# Symbols as Blocks are SLOW 
- 10% is 10% of slowdown is a LOT 
- We should not put the burden on VM optimiser 
- We should ease the optimiser to focus on the real hotspot 
- Same for refactorings 
- Let us stop to be lame 
 
# Symbols as Blocks are not tools friendly 
Now all the rules should also take that into account that a symbol could also be a block.  
- Can we use the little static analysis we can do to ease tooling? Else why not removing temp declaration? 
- What is we have a block and a key symbol with the same  
 
``` 
	at: #name put: 33
	
	authors collect: #name 
``` 
So? 
# Symbols as Blocks slow my debugging 
When I debug I cannot grab fast an element of the list or the method by putting a self halt.  
``` 
self xzw do: #kkk 
``` 
vs. 
``` 
self zzz do: [:each | self halt. each kkk] 
``` 
 
# Examples 
- How do you know that you can pass a block or not 
 
``` 
	... port: #in  
``` 
 
# Examples 
 
``` 
centered
	self withWindowDo: #centered 
``` 
So just reading the reader has no idea which kind of object it can pass. 
# Give me more information not less 
 
``` 
rule := ReRuleManager visibleRuleClasses collect: [:clas | clas new]. 
``` 
vs. 
``` 
rule := ReRuleManager visibleRuleClasses collect: #new. 
``` 
With `new` we can expect the receiver to be a class 
``` 
model emergingEntity collect: #outgoing. 
``` 
vs. 
``` 
model emergingEntity collect: [ :fmclass | fmclass outgoing ]. 
``` 
 
# Give me more information not less 
 
``` 
(self port: #out) collect: #selector 
``` 
	vs.  
``` 
(self port: #out) collect: [ :aPragma | aPragma selector ] 
``` 
 
# About inverse 
When I pass a block I know that I can pass a symbol  but when I pass a symbol I do not know if I can pass a block 
``` 
deactivate
	activeTranscript := Transcript.
	SystemProgressMorph disable.
	self trigger: #aboutToLeaveWorld.
	WorldMorph extraWorldList do: [:world | world trigger: #aboutToLeaveWorld ]. 
``` 
Can I pass a block to `trigger:`? 
# Conclusion 
- Symbols as blocks are cool for scripting 
- Avoid them in application code 
