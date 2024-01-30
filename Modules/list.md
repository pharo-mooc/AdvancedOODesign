- Checked [Stef] 0-AboutTheMooc.pillar

## Module 1: Understanding messages
This first module revisits elementary concepts around self, super and the power of dispatching to dedicated objects.
The case study shows how to go from a monolithic design with one kind of formats to the handling of optional different formats in the Pillar ddocument compilation chain.

- Checked [Stef] 1-Essence-01-NotExample.pillar
+ [Luc] 2-Essence-02-Dispatch.pillar
+ [Luc] 3-Essence-03-Inheritance-Basic.pillar
- Redone [Stef] 4-Essence-04-Self.pillar
- [Guille] 5-Essence-05-Super.pillar
- Checked Should redo Slide 4 - this is not a document this is the class PRDOcument [Stef] 6-CaseStudy-07-Pillar-ReifyAndDispatch.pillar

## Module 2: Test-driven Design
This module covers an important aspect: testing applications and how to take advantage of test driven design. It shows in particular the power of eXtreme Test Driven Design and how writing tests first and coding in the debugger is empowering the designer.

- [Guille] 1-Tests-01-101.pillar
- [Guille] 2-Tests-02-Why.pillar
+ [Luc] 3-Tests-03-TDD.pillar
- [Pablo] 4-Tests-04-XTDD.pillar
- [Pablo] 5-Tests-05-ParametrizedTests.pillar

## Module 3: Hooks: support for evolution
In this module we will start to look at design pattern. In parallel we will discuss a key point of object-oriented design that is how to design abstraction that extensible using hooks. The case study will be about going from monolithic to parametrized objects.

- Checked [Stef] 1-DesignPattern-01-IntroDesignPattern.pillar
+ [Luc] 2-Essence-07-SelfSendsArePlansForReuse.pillar (template methods)
+ [Luc] 3-DesignPattern-02-HookAndTemplate.pillar (Copy PostCopy)
- [Stef] 4-Lang-01-Stream.pillar
- [Stef] 5-BasicPrinciples-02-FromGlobalToParameter.pillar

## Module 4: Objects: state + behavior
In this module we will focus on basic principle showing for example the difference between data and objects. We will start also to present
some design patterns such as Singleton and Decorator

+ [Luc] 1-BasicPrinciples-01-MethodIsReuse.pillar
- [Pablo] 2-BasicPrinciples-04-AboutObjectsVSData.pillar
- Checked okish [Stef] 3-BasicPrinciples-03-AboutGlobalVariable.pillar
- [Pablo] 4-BasicPrinciples-05-FatClassesAreBad.pillar
- [Guille] 5-DesignPattern-06-Singleton.pillar
- [Guille] 6-DesignPattern-09-Decorator.pillar

## Module 5: Elementary design patterns [Files Renamed]

In this module we will present some important and simple design patterns such as composite or state. We will then propose to compare use versus inheritance a way to understand the forces in presence.

- [Luc] 1-DesignPattern-03-Composite.pillar
- [Pablo] 2-DesignPattern-11-State.pillar
- [Pablo] 3-DesignPattern-07-Command.pillar
+ [Luc] 4-BasicPrinciples-06-DelegationVsInheritance.pillar
- [Pablo] 5-CaseStudy-01-TurningAProcIntoAnObject.pillar
- [Pablo] 6-Lang-04-BlocksVsObjects.pillar
- [Guille] 7-Principles-01-AvoidIsNil.pillar
- Checked [Stef] 8-CaseStudy-02-AboutFluidAPI.pillar

## Module 6: Double dispatch [Files Renamed]

This module prensents the double dispatch mechanism and the Visitor design pattern which is based on it.

- [Stef] 1-DoubleDispatch-01-StoneExercise.pillar
- [Guille] 2-DoubleDispatch-04-NoSymmetrical.pillar
- checked can we remove the slide 20 / remove glitch on slide 26  [Stef] 3-DoubleDispatch-03-Dice.pillar
- [Luc] 4-DesignPattern-04-Visitor.pillar
- [Luc] 5-DesignPattern-05-VisitorDiscussions.pillar
- checked [Stef] 6-DoubleDispatch-05-StoneExercise-AboutResult.pillar
- [Stef] M6-7-DoubleDispatch-AddingNumbers.pillar

## Module 7: Object Creation [Files Renamed]

This module focuses on patterns to create and initialize objects.

- [Pablo] 1-Principles-01-LazyInitialization
- [Guille] 2-Principles-07-ClassHookVsInstanceHook.pillar
+ [Luc] 3-Principles-06-selfVSClassDispatch.pillar
- checked [Stef] 4-CaseStudy-03-UsingAnAccumulator-FormValidation.pillar
- checked [Stef] 5-CaseStudy-04-PowerOfDelegationClassDefinitionPrinter.pillar
- [Pablo] 6-DesignPattern-08-Builder.pillar
- [Pablo] 7-Lang-05-AboutBuilder.pillar
- [Guille] 8-Essence-06-DidYouUnderstandSuper.pillar

#Module 8: Sharing Objects [Files Renamed]

This module presents different techniques and design patterns to share objects.

- [Stef] 1-Lang-02-SharedVariables.pillar
- [Stef] 2-Principles-08-Sharing.pillar
Ici UP - Checked [Stef] 3-Lang-03-SharedPools.pillar
- [Luc] 4-Essence-08-AboutMagicNumbers
- [Guille] 5-DesignPattern-10-Flyweigth.pillar
- [Pablo] 6-DesignPattern-12-TypeObject.pillar
 - [ Stef ] 8-7-Sharing-Alternate.pillar

## Module 9: Inversion of control [Files Renamed]

In this module, we present the law of demeter and different techniques to achieve Inversion of control.

- [Guille] 1-Principles-04-LawOfDemeter.pillar
- [Luc] 2-Principles-02-AboutClassMethodsAndRegistration.pillar
- [Luc] 3-Principles-03-AboutRegistration.pillar
- [Pablo] 4-CaseStudy-06-LayeredSettingsArchitecture.pillar
- [Guille] 5-CaseStudy-05-Sokoban-Analysis.pillar
- [Stef] 6-ClassVsObject.pillar

## Module 10: About types [Files Renamed]

This modules focuses on typing and their relation with object-oriented design.

- [Luc] 1-Principles-12-DualInterfaces.pillar
- [Pablo] 2-Principles-09-SubtypingVsSubclassing.pillar
- [Pablo] 3-Principles-10-DynamicStaticType.pillar
- [Luc] 4-Principles-11-PolymorphismSupportEvolution.pillar
- [Guille] 5-Principles-05-AboutDefensiveProgramming.pillar



## Todo


Lectures
	- revisit TypeObject -
	- Parcours?
	- Quizzes
	- Nombres de videos + nombres de slides

- Badges

Katas
	- main exercise
	- satellites
	- Ketches of "katas" + hints


Pour les katas see Booklet-TDDKatas/notes

git@github.com:SquareBracketAssociates/Booklet-TDDKatas.git




