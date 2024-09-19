{ 
"title" : "About Types and Lookup",
"slidesid" : "",
"subtitle" : "",
"author" : "S. Ducasse" 
} 
 
# Remember: Static vs. Dynamic Types 
 
``` 
A a = new B(); 
``` 
- The static type of variable `a` is `A`  i.e., the statically declared class to which it belongs. 
  - The static type never changes. 
- The dynamic type of `a` is `B`  i.e., the class of the object currently bound to a. 
  - The dynamic type may change throughout the program. 
 
# Two simple classes 
 
``` 
public class Machine {
    public void accept(){System.out.println("accept");}}
public class Robot extends Machine {
    public void accept(){System.out.println("accept");}
    public void agree(){System.out.println("agree");}} 
``` 
 
# Valid and invalid 
 
``` 
Robot r = new Robot();
r.accept();
r.agree(); 
``` 
 
``` 
Machine m = r;
m.accept(); 
``` 
 
``` 
m.agree(); >>> BREAK!
((Machine)r).agree(); >>> BREAK! 
``` 
- A typechecker rejects programs that would execute without problems to make sure that it can find execution that would fail. 
 
# What you should know 
- Static types are used to identify at compile time which methods to lookup 
- Lookup will look for such method at runtime   
