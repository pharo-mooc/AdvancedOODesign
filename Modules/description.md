Advanced Object-Oriented Design Mooc with Pharo

Authors
	Stéphane Ducasse - http://stephane.ducasse.free.fr
	Luc Fabresse - IMT Nord Europe
	Guillermo Polito -
	Pablo Tesone -

That you are either a beginner or an expert in object-oriented programming and design
you will not develop the same way after following this unique lecture.

This mooc will immerge you in advanced object-oriented design. It is built on more than 60 years
of expert teaching object-oriented design.

This mooc invites you to a journey around 10 modules (with over 60 videos) covering the following topics
	- Understanding messages
    - Test-driven Design
    - Hooks: support for evolution
    - Objects: state and behavior
    - Elementary design patterns
    - Double dispatch
    - Object Creation
    - Sharing Objects
    - Inversion of control
    - About types
	- It also illustrates the topics on concrete case studies taken from Pharo.

This lectures uses Pharo as a pedagogical vehicule but all the concepts you will learn
are applicable to other object-oriented languages. We use Pharo because it is a pure object-oriented programming language. It offers a unique developing experience in constant interaction with live objects. Pharo is elegant, fun to use and very powerful. It is very easy to learn and enables to understand advanced concept in a natural way. When programming in Pharo, you are immersed in a world of live objects. You have immediate feedback at any moment of your development on objects representing web applications, code itself, graphics, network. More…

If you like the Pharo mooc http://mooc.pharo.org, you will just love "Advanced Object-Oriented Design".
It will bring you to the next level.

The learners will be proposed several design exercises ranging from little interpreters to games and quizes.



# =============================

Tests: Les tests sont essentiels pour permettre d’identifier les probrlemes de non regressions en cas de changements.
De plus avec Test Driven Design ils permettent une conception plus claire et efficace. Ils permettent aussi
a la programmation agile de donner tout son potentiel dans une boucle vertueuse (test, developpement, refactorings)
Acquis: Test, XTDD, TDD

Essence: Cette partie presente les aspects essentiels de la POO : a savoir que l'envoi de messages selectionne la bonne methode
Cette section revient sur les concepts importants de self/this et super. Elle presente aussi que les envoie de messages a self sont de la planification pour la reutilisation par les souclasses. Elle montre que definir de petites methodes est un point essentiel pour la reutilisation future du code car le code des souclasses peuvent etre conceptuellemment injecte dans celui des superclasses.
Acquis: points essentiels!, Hook and Template Design Pattern, modularité

Basic Principles: cette partie revient des concepts elementaires de la programmation objet tels que la notion meme d'objets, la comparaison
de l'heritage et la delegation, la simple reutilisation de méthodes.
Acquis: object vs data, inheritage vs delegation, grosses classes sont mauvaises, Stragegie design pattern

Double dispatch: Alors qu'envoyer un message est faire un choix comme vu dans la section Essence, nous abordons ici sa generalisation
c'est dire comment en utilisant deux messages on peut choisir une methode basée sur le receveur et son argument.
Ce point est central car il montre comment on peut eviter l'utilisation de condition statiques et monolithiques pour dfefinir des systemes modulaire. Il est aussi a la base du Design Pattern Visitor.
Acquis: Double Dispatch

Principles: Cette section aborde des principes plus généraux comme l'utilisation de tests sur nul, la loi de demeter qui limite de couplage, et
la comparaison entre subclassing and subtyping.
Acquis: Law of Demeter, couplage, modularite, subclassing, subtyping, ...

Case study: Cette section présente des cas réels d'utilisation des principes presentes avant dans le cours.
Elle presente aussi des points avancés comme une analyse des APIs de classes qui montrent immédiatement des problèmes de conception, ou une architecture en forme de couche et de descriptions.
Acquis: Points avancés.

Design Patterns: Cette aprtie presente quelques Design Patterns comme le Hook and Template Method, le Composite et le Visitor qui sont centraux
a des nimbreux traitements.

Langage: Cette partie montre quelques idiomes de programmation sur l'utilisation des flots, les variables partagees, la comparaison  entre fermetures lexicales et objets et des discussions autour de l'API de Builder Design pattern a base de fermeture. lexicales.