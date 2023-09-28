## Objectifs pédagogiques EN et FR

Mooc
- Get to know and understand the key mechanisms and the essence of OOD

Module 1: Understanding messages
- Completely rethink what it means to send a message
- Explain that sending a message is making a choice based on classes
- Distinguish between static and dynamic approaches to inheritance
- Understand what is to send a message and how lookup works
- Understand deeply what super is 
- Apply the mechanics of a transformation that makes implicit behavior explicit

Module 2: Test-driven design
- Understand the structure and benefits of a test and specify a proper automated test
- Identify the benefits and characteristics of a good test suite
- Identify the benefits and apply a Test Driven Development workflow
- Specify and apply the Xtrem Test Driven Development method with Pharo tools
- Create a parameterized test and reuse it with specific values

Module 3: Hooks: support for evolution
- Get exposed to design patterns
- Use hooks to extend code
- Analyze hook and template methods
- Use a stream and avoid creating spurious objects
- Move from a monolithic global design to one that can be parameterized

Module 4: Object state & behavior
- Rethink object API
- Distinguish between an object and a data structure
- Identify the different syntactic forms of global variables
- Identify the disadvantages of fat classes and replace them with class hierarchies and delegation
- Implement the Singleton pattern, with its advantages and disadvantages
- Apply the Decorator design pattern and identify when to use it

Module 5: Elementary design pattern
- Understand the Composite design pattern and identify when to use it
- Use the State design pattern to design objects with many states, complex transitions between states and operations that depend on each state
- Understand the Command design pattern and identify when to use it
- Use a design pattern in the real world
- Compare inheritance-based and delegation-based designs
- Identify the benefits of using objects to represent complex algos
- Recognize when it is preferable to use objects rather than lexical closures
- Identify the use of NullObject design pattern and the benefit of object state initialization
- Manage methods with a large number of arguments and design fluid APIs

Module 6: Double dispatch
- Use the power of sending messages to get a more modular design
- Apply Double dispatch to non-symmetrical domains
- Identify the double dispatch mechanisms and use them with a simple example
- Apply the Visitor design pattern and identify when to use it
- Use and implement the possible variations of the Visitor design pattern 
- Question the return of values, numbers vs. symbols
- Use the double dispatch mechanisms in more complex cases

Module 7: Object creation
- Identify the benefit of delaying the initialization of an object until it is needed
- Analyze the impact of the granularity of hooks
- Use a mechanism for specifying extensible class names by default to avoid hardcoding them
- Use the delegation of actions and accumulator concepts
- Use of behavior delegation to avoid programming complex conditions
- Use the Builder design pattern to create complex object graphs
- Identify and use different API design alternatives for Builder Patterns
- Explain the relation between super and lookup when sending a message

Module 8: Sharing objects
- Use a shared variable and analyze its impact on the instances of a hierarchy
- Mix resource sharing with instance-specific information to extend the spectrum of object sharing
- Group and share constants between multiple classes
- Customize hooks to define and reuse magic literals to avoid hardcoding them in the code
- Identify the implementation compromises for the Flyweight pattern
- Represent attributes that are common to a type of objects in a more flexible way
- Share objects while allowing properties to be modified

Module 9: Inversion of control
- Reduce the impact of change in complex systems by following Demeter's Law
- Use class methods to create extensible designs
- Use an explicit registration mechanism and explain its benefits
- Identify a monolithic architecture and propose different solutions to transform it into a more modular one
- Analyze an existing design and remodel it to make it modular using message dispatch
- Understand object programming as opposed to a design approach that focuses more on classes than on objects

Module 10: About types
- Disprove the common misconception that instance variables must be private
- Explain the difference between Subclasses and Subtypes
- Describe the relationship between sending a message associated with the selection of lookup methods and static types
- Explain the need for interfaces in statistically-typed languages and their uselessness in dynamically-typed languages
- Explain the pros and cons of using defensive checks in programming




Mooc
- Get to know the key mechanisms and the essence of OOD

Module 1: Understanding messages
- Repenser complètement ce qu'est un envoi de message
- Envoyer un message c'est faire un choix basé sur les classes
- Distinguer les 2 approches de l'héritage, statique et dynamique / Comprendre la création de sous-classes
- Comprendre l'envoi d'un message et comprendre le fonctionnement de la recherche de méthodes
- Comprendre et utiliser super pour effectuer une bonne recherche de méthode
- Comprendre la mécanique d'une transformation qui rend explicite un comportement implicite

Module 2: Test-driven design
- Comprendre la structure et les bénéfices d'un test / Spécifier un bon test automatique
- Comprendre les bénéfices d'une bonne suite de tests
- Comprendre et appliquer le workflow du TDD
- Connaitre la technique de Xtrem test driven development et l'utiliser avec les outils de Pharo 
- Utiliser les parametrized tests et amplifier leurs usages avec différentes valeurs

Module 3: Hooks: support for evolution
- Identifier un design pattern et les différentes formes existantes
- Prévoir des hooks permettant l'extension du code
- Analyser des exemples de hook et template
- Qu'est-ce qu'une stream ?
- Passer d'un design global monolithique à un design paramétrable

Module 4: Object state & behavior
- Enrichir l'API des objets
- Comprendre la difference entre un objet et une structure de données et l'importance d'implémenter des opérations dans un objet
- Identifier les différentes formes syntaxiques des global variables
- Identifier le problème des larges classes / remplacer les larges classes par les hiérarchies de classes et la délégation
- Apprendre à implémenter le pattern Singleton avec ses avantages et ses inconvénients 
- Appliquer le Design Pattern Decorator et comprendre quand l'utiliser

Module 5: Elementary design pattern
- Comprendre le design pattern Composite pour savoir à quoi il sert et quand l'utiliser
- Utiliser le State design pour la conception d'objets avec plusieurs états, des transitions complexes entre les états et des opérations qui dépendent de chaque état
- Comprendre et utiliser le Command design pattern 
- Utiliser un design pattern dans le monde réel
- Comparer des conceptions basées sur l'héritage de celles basées sur la délégation
- Comprendre les bénéfices d'utiliser les objets pour représenter des algos complexes
- Reconnaitre les situations où il est préférable d'utiliser des objets plutôt que des fermetures
- Concevoir de façon modulaire en modélisant l'absence d'objets
- Gérer des méthodes avec un grand nombre d'arguments et concevoir des API

Module 6: Double dispatch
- Avoir une conception plus modulaire / utiliser et comprendre la puissance de l'envoi de messages
- Comprendre que le Double dispatch peut s'appliquer à des domaines non symétriques
- Comprendre les mécanismes du double dispatch et l'utiliser via un exemple simple
- Comprendre le design pattern Visitor et savoir l'utiliser
- Utiliser et comprendre les variations possibles sur l'implémentation du design pattern VIsitor
- Réfléchir à ce qui est un retour de valeur
- Approfondir les mécanismes du double dispatch et l'utiliser via un second exemple

Module 7: Object creation
- Retarder l'initialisation des objets
- Analyser et comprendre du l'impact du choix des granularités des hooks
- Ne pas hardcoder les noms de classe et fournir un mécanisme de spécification de nom de classe extensible par défaut 
- Explorer différents designs et explorer le concept d'accumulator
- Utiliser la delegation pour éviter la programmation de conditions complexes
- Utiliser le Pattern Builder pour la création de graphes complexes d'objets
- Comprendre les différentes alternatives pour la conception d'API pour le Builder Pattern
- Utiliser super et la recherche de méthode avec un exemple concret et 2 casse-têtes

Module 8: Sharing objects
- Comprendre les variables partagées
- Elargir son spectre de partage d'objet avec la possibilité de mixer le partage avec des infos spécifiques à l'instance
- Grouper des constantes ensemble et à les partager
- Prendre conscience de ne pas coder en dure  des constantes dans le code
- Identifier les compromis d'implementation du pattern Flyweight
- Comprendre comment représenter de manière plus flexible les attributs communs entre objets
- Découvrir une autre conception du partage d'objet tout en permettant les particularités

Module 9: Inversion of control
- Diminuer l'impact du changement dans des systèmes complexes en suivant la loi de Demeter 
- Utiliser des méthodes de classe pour faire des conceptions extensibles
- Comprendre l'avantage d'un mécanisme de registration explicite
- Comprendre l'exemple d'une application monolithique et voir les différentes solutions pour mieux la modulariser
- Etudier une conception existante et la remodeliser pour la rendre modulaire en utilisant la liaison tardive
- Comprendre la programmation objet par opposition à une façon de développer qui se concentre trop sur les classes et pas assez sur les objets

Module 10: About types
- Démonter l'idée reçue que les variables d'instances doivent être privées
- Comprendre la différence entre Subclasses et Subtypes
- Comprendre les relations entre l'envoi d'un message associé à la sélection de méthodes lookup et les types statiques
- Comprendre le concept d'interface dans les langages statistiquement typé et son inutilité dans les langages dynamiquement typés
- Comprendre les avantages et inconvénients de faire des checks défensifs dans le code

:::

## Plan du cours

Module 1: Understanding messages
1. Essence of Dispatch - Taking Pharo Booleans as Example
2. Essence of Dispatch - Let the receiver decide
3. Inheritance Basics
4. Inheritance and Lookup: Self - Understand lookup once for all
5. About super
6. Reification and delegation - A case study: Microdown in Pillar
7. **Quiz**

Module 2: Test-driven design
1. Test 101 - The minimum you should know
2. Tests - Why testing is Important?
3. Test-Driven Development
4. Xtreme Test Driven Development - Getting a productivity boost
5. Parametrized Tests - Getting more tests out of test cases
6. **Quiz**

Module 3: Hooks: support for evolution
1. An introduction to design patterns
2. Message Sends are Plans for Reuse
3. Hooks and Template - One of the cornerstone of OOP
4. Using well asString and printString - A Pharo code idiom
5. Global To Parameter - Basic but important
6. **Quiz**

Module 4: Object state & behavior
1. Methods: the elementary unit of reuse - Obvious but important
2. Objects vs. Data - An API perspective studying the class Point
3. About global variables
4. Fat classes are bad - a.k.a. a large class vs. a class hierarchy
5. Singleton - A highly misunderstood pattern
6. Decorator Design Pattern- A composable alternative to subclassing
7. **Quiz**

Module 5: Elementary design pattern
1. Composite - A nice and common design pattern
2. About state Design Pattern
3. Command Design Pattern — Actions as objects  Command Design Pattern — A glimpse at Commander
4. Delegation vs. Inheritance - Basic but worth
5. Turning Procedures to Objects
6. Blocks vs. Objects - Rethinking common abstractions
7. Avoid Null Checks
8. About Fluid APIs - The case of the class definition
9. **Quiz**

Module 6: Double dispatch
1. A double dispatch starter - Stone Paper Scissors
2. Double dispatch
3. a Die + a DieHandle - Practicing dispatch more
4. Visitor - Modular and extensible first class actions
5. Some discussions on Visitor
6. Stone Paper Scissors - The case of results
7. Double Dispatch - Adding numbers as a kata
8. **Quiz**

Module 7: Object creation
1. About Null Check - The case of lazy initialization
2. Customization degree of hooks - Class vs. instance hooks
3. DieHandle new vs. self class new - When classes are first class citizen
4. Delegation of actions and accumulator - Form validation as an example
5. Behavior delegation at work - The case of the class printer
6. Builder Design Pattern - Encapsulating object creation
7. Builder API variations
8. Did You Really Understand Super?
9. **Quiz**

Module 8: Sharing objects
1. Shared variables - A Pharo code idiom
2. Sharing with instance specific possibilities
3. Shared Pools - Static sharing between hierarchies
4. About magic literals
5. Flyweigth
6. TypeObject
7. A variation on sharing
8. **Quiz**

Module 9: Inversion of control
1. About coupling and encapsulation
2. Class Methods at Work
3. About Registration - When class method-based registration is too much
4. Application settings - From a monolithic to a modular architecture
5. Learning from a Sokoban implementation
6. Class vs. Object-Oriented Programming
7. **Quiz**

Module 10: About types
1. The two interfaces - In presence of delta programming
2. Subclassing vs. Subtyping
3. About type and method lookup
4. Polymorphic objects - Support for software evolution
5. About defensive programming
6. **Quiz**

