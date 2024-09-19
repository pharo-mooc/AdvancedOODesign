{ 
"title" : "About inheritance vs. object-based configuration",
"subtitle" : "",
"author" : "S. Ducasse" 
} 
 
# Example 
 
``` 
NewTestRunner << #NewCommandLineRunner,
	slots: { #reporter }; 
 	#package: #'TestRunner-Core-Extensions' 
``` 
 
``` 
NewCommandLineRunner class >> with: aReporterClass [

 	^ self new reporter: aReporterClass new

NewCommandLineRunner >> defaultReporterClass [

	 ^ StdReporter 
``` 
 
# Limits 
- Only define a new defaultReporterClass by subclassing \`NewCommandLineRunner\` 
- Difficult if we cannot/do not want to change the clients of \`NewCommandLineRunner\` 
 
# Solution: variable and setter 
 
``` 
NewTestRunner << #NewCommandLineRunner,
	slots: { #reporter . #defaultClassReporter}; 
 	#package: #'TestRunner-Core-Extensions' 
``` 
  
``` 
NewCommandLineRunner >> defaultReporterClass: aClass

	defaultReporterClass := aClass 
``` 
- Each instance of NewCommandLineRunner has its own \`defaultReporterClass\` 
 
# Initialization 
 
``` 
NewCommandLineRunner >> initialize

	super initialize.
	self defaultReporterClass: aClass 
``` 
 
# Class Granularity 
 
``` 
NewTestRunner << #NewCommandLineRunner,
	slots: { #reporter }; 
	sharedVariables: { #DefaultReporterClass };
 	#package: #'TestRunner-Core-Extensions' 
``` 
 
``` 
NewCommandLineRunner class >> defaultReporterClass: aClass

	DefaultReporterClass := aClass 
``` 
- All instances of all subclasses of NewCommandLineRunner will share the same default class 
  
# class side Initialization 
 
``` 
NewCommandLineRunner class >> initialize

 	self defaultReporterClass: aClass 
``` 
