{
"title" : "Libraries versus Frameworks",
"subtitle" : "",
"slidesid" : "From the Design Corner"
}


# Outline
- What are libraries?
- What are frameworks?
- Some guidelines to create a new framework

# What are Libraries?
- a _library_ is a set of code entities \(classes and methods\)
- the _client_ of a library sends _requests_ to the library
- the library returns _responses_
- the main code \(dark blue\) is in the client
![.](figures/Library.png width=60)
# What are Frameworks?
- a _framework_ is a set of code entities \(classes and methods\), just like in libraries
- the framework has _abstractions_ \(i.e., holes\) to be implemented
- the _client_ implements the abstractions to parameterize the framework
- the main code \(dark blue\) is in the framework
![.](figures/Framework.png width=70)
# Libraries versus Frameworks
- Library
  - You call it
  - You use callbacks to extend it
- Framework
  - _Hollywood principle_: Don't call me, I will call you

# Libraries versus Frameworks

| Library | Framework |
| --- | --- |
| The client instantiates the classes | The framework instantiates the classes |
| The client invokes library functions | The framework invokes code in the client |
| The client is responsible for the flow | The framework is responsible for the flow |
# Inheritance as Parameterization
- a client parameterizes a framework by overriding operations
- the _template method_ design pattern is often used
![.](figures/FrameworkParameterization.png width=70)
```language=smalltalk
MyGUI new newWindow  --> creates a window of width 25
```

# Framework Design
- Needs at least 3 clients
- "_A Pattern Language for Developing Object-Oriented Frameworks_", by Don Roberts and Ralph Johnson
- Framework design often relies on whitebox abstractions
  - framework are extended by inheritance
  - blackbox abstraction is also possible: usage of composition
