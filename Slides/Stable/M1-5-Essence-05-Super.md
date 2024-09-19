{ 
"title" : "About super",
"subtitle" : "",
"slidesid" : "M1S5" 
} 
 
# Goals 
- Sending a message 
- Method lookup 
- `super` semantics and the differences with `self` 
 
# Define what super is! 
<!columns|width=100 
 
<!column|width=50 
 
![](figures/LookupWithSuperInSuperclassMethodThreeClasses.pdf width=85) 
!> 
 
<!column|width=50 
 
Take 5 min and write the definition of `super` 
- your definition should have two points: 
  - what does `super` represent? 
  - how is a method looked up when a message is sent to `super`? 
 
!> 
 
 
!> 
 
# Challenge yourself with super! 
<!columns|width=100 
 
<!column|width=80 
 
![](figures/LookupWithSuperInSuperclassMethodThreeClasses.pdf width=85) 
!> 
 
<!column|width=30 
 
 
``` 
> aA bar
...
> aB bar
...
> aC bar
... 
``` 
 
!> 
 
 
!> 
 
# Challenge yourself with super! 
<!columns|width=100 
 
<!column|width=80 
 
![](figures/LookupWithSuperInSuperclassMethodThreeClasses.pdf width=85) 
!> 
 
<!column|width=30 
 
 
``` 
> aA bar
10
> aB bar
20
> aC bar
100 
``` 
 
!> 
 
 
!> 
 
# super changes where the lookup starts 
<!columns|width=100 
 
<!column|width=54 
 
![](figures/LookupWithSuperInSuperclassMethodThreeClasses.pdf width=100) 
!> 
 
<!column|width=46 
 
Evaluation of `aC bar`1. `aC`'s class is `C` 
1. no method `bar` in C 
1. look up in `B` - `bar` is found 
1. method `bar` is executed 
1. `bar` is sent to `super` 
1. `super` is `aC` but lookup starts in `A` 
1. `bar` is found in `A` and executed 
1. `foo` is sent to `aC` 
1. `foo` is found in `C` 
 
!> 
 
 
!> 
 
# super changes where the lookup starts 
- `super` refers to the **receiver** of the message \(just like `self`\) 
- The method lookup starts .......................................... \(Take 1 min to fill the dots\) 
 
# super in two sentences 
- `super` refers to the receiver of the message \(just like `self`\) 
- The method lookup starts in the superclass of **the class containing the `super` expression** 
 
# self is dynamic 
<!columns|width=100 
 
<!column|width=45 
 
![](figures/LookupWithSelfInSuperclassMethod.pdf width=90) 
!> 
 
<!column|width=55 
 
- At compilation time, we **don't** know  
- to which object `self` points to 
- to which `foo` method `bar` refers to 
Imagine that we load a new subclass `C` of `B` and do `C new bar`, `self` will be pointing to such instance 
!> 
 
 
!> 
 
# super is static 
<!columns|width=100 
 
<!column|width=50 
 
![](figures/superIsStatic.pdf width=65aA) 
!> 
 
<!column|width=50 
 
- At **compilation-time**, we know that `B>>foo` refers to `A>>foo` 
- we should look above the class containing the **method** using `super` 
 
!> 
 
 
!> 
 
# Even some books got it wrong 
- **Wrong** definition: _`super` looks for the method in the superclass of the **receiver**'s class_ 
- With this definition, this example would loop forever: 
![](figures/LookupWithWrongDefinition.pdf width=50)In reality it **does not** loop, the definition is wrong 
# What you should know 
- `self` always represents the receiver 
- `super` always represents the receiver 
- `super` changes the lookup: 
  - a super send starts the lookup in the class above it 
- self sends act as a hook: code of subclasses may be invoked \(see Lectures for more\) 
