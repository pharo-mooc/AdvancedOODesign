{ 
"title" : "Essence of Dispatch", 
"slidesid" : "M1S2", 
"subtitle" : "Let the receiver decide" 
} 
 
# Remember: Implementing not in two methods 
![Not implementation](figures/BooleanHiearchyAndInstancesWithNotMethodsLookup.pdf width=70) 
# What is the point? 
- You will probably never implement `Booleans` in the future 
- So, is it **really** useful? 
- What are the lessons to learn? 
- What are the properties of the solution? 
 
# Imagine having more than two classes 
<!columns|width=100 
 
<!column|width=45 
 
 
``` 
MicAbstractBlock 

		MicAbstractAnnotatedBlock 

			    MicAnnotatedBlock 

		MicContinuousMarkedBlock 

			    MicCommentBlock 

			    MicQuoteBlock 

			    MicTableBlock 

		MicListBlock 

			    MicOrderedListBlock 

			    MicUnorderedListBlock 

		MicParagraphBlock 

			    MacParagraphBlock 

			    MacRawParagraphBlock 

		MicRootBlock 

		MicSectionBlock 
``` 
 
!> 
 
<!column|width=55 
 
 
``` 
	    MicSingleLineBlock 

	        	MicAnchorBlock 

	        	MicHeaderBlock 

	        	MicHorizontalLineBlock 

	    MicStartStopMarkupBlock 

	    	    MicEnvironmentBlock 

	    	    ... 

	    	    MicMetaDataBlock 

	    	    MicSameStartStopMarkupBlock 

	    	    	    MicCodeBlock 

	    	    	    MicMathBlock 

	    	    	    	    MicMathBlockExtensionForTest 

	    	    	    	    MicMultilineComment 
``` 
Imagine a method that has one condition for each of these cases! 
!> 
 
 
!> 
 
# A message send is an open conditional 
Sending a message 
- selects the **right** method to execute based on the class of the receiver 
- can be seen as a condition **without explicit ifs** 
- is a dynamic choice 
 
# Select the right method 
<!columns|width=100 
 
<!column|width=40 
 
 
``` 
aCollection := {a . bb . c}. 

... 

aCollection do: [ :e | 

    e operation] 
``` 
 
!> 
 
<!column|width=50 
 
![](figures/Design-FatVsDispatchNoFat2.pdf width=95) 
!> 
 
 
!> 
 
# But dynamically: new objects can be chosen 
<!columns|width=100 
 
<!column|width=40 
 
 
``` 
aCollection := {a . bb . c . aa}. 

... 

aCollection do: [ :e | 

    e operation] 
``` 
 
!> 
 
<!column|width=50 
 
![](figures/Design-FatVsDispatchNoFatDyn.pdf width=95) 
!> 
 
 
!> 
 
# Sending a message is making a choice 
- Message sending is a **choice** operator 
- Each time you send a message, the execution engine **selects the right method** depending on the class of the receiver 
- So, the next question is: 
  - **How do we express choices**? 
 
# How do we express choices? 
- Could we have the same solution for `not` with a **single** `Boolean` class? 
- No! We would have conditionals in the `not` and `or` methods! 
![](figures/Design-FatVsDispatchBoolean.pdf width=75) 
# Classes play case distinct choices 
- To activate the choice operator we must have **choices** 
- A **class** represents a choice \(a case\) 
 
# One class vs. a hierarchy 
![](figures/Design-FatVsDispatch.pdf width=75) 
# Class hierarchy supports dynamic dispatch 
- More **modular** 
- No need to introduce **complex** conditions 
- A hierarchy provides a way to **specialize** behavior 
- No need to **recompile existing** methods 
- You only focus on one class at a time 
![](figures/Design-FatVsDispatch.pdf width=50) 
# Message dispatch supports modularity 
![](figures/Design-FatVsDispatchWithPackages.pdf width=65)We can package different classes into different packages \(better modularity\) 
# Limit impact of changes 
![](figures/Design-FatVsDispatchWithPackages2.pdf width=65) 
- If a client receives instances of `D` \(in addition to classes of first package\), its code does not have to change 
- Method `operation` of `D` instances will be executed naturally 
 
# Message send is powerful 
- Message sends are supporting **choices** 
- The execution engine acts as a conditional switch: Use it! 
- Classes act as "cases/choices" 
- But with messages, the case statement is **extensible**: 
  - adding new classes without breaking client code 
 
# Let the receiver decide 
- Sending a message lets the receiver decide 
- Client does not have to decide 
- Client code is more declarative: **give orders** 
- Different receivers may be substituted dynamically 
 
# Summary: a cornerstone of OOP 
- Avoid conditionals \(see AntiIfCampaign\) 
- Use objects and messages whenever you can 
- Let the receiver decide: **Do not ask, tell** 
- Class hierarchy supports for dynamic dispatch 
