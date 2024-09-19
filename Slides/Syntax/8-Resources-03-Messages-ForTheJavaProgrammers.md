{
"title" : "Messages for Java Programmers",
"subtitle" : "",
"slidesid" : "xxx"
}

# Only objects and messages
- code in Pharo **only** manipulates objects: mouse, booleans, arrays, numbers, compressed, strings, windows, scrollbars, canvas, files, trees, compiler, sound, url, socket, fonts, text, collections, stack, shortcut, streams, ...
- messages and assignments are the only way to do something

# Equivalence
In Java
```
    ArrayList<String> strings = new ArrayList<String>();
```
In Pharo
```
strings := OrderedCollection new.
```
- 1 assignment, 1 message sent
- `new` is a message sent to a class
- no static typing
- no generics

# Equivalence
In Java
```language=java
Thread regThread = new Thread(
  new Runnable() {
    @Override
    public void run() {
      this.doSomething();
    }
  });
regThread.start();
```
In Pharo
```
[ self doSomething ] fork
```

# Equivalence
In Java 8
```language=java
new Thread(() -> this.doSomething()).start();
```
In Pharo
```
[ self doSomething ] fork
```

# Three kinds of messages
- Unary

```
5 factorial
Transcript cr
```
- Binary

```
3 + 4
5 -> 10
```
- Keyword-based

```
Transcript show: 'hello world'
2 between: 0 and: 5
```

# Keyword messages for Java developers
In Java
```language=java
    receiver.keyword1keyword2(arg1, arg2)
```
In Pharo
```
    anObject keyword1: arg1 keyword2: arg2
```

# Keyword messages for Java developers
In Java
```
    postman.send(mail,recipient);
```

# Keyword messages for Java developers

```
    postman.send(mail,recipient);
    postman . send ( mail , recipient );
```

# Keyword messages for Java developers

```
    postman.send(mail,recipient);
    postman . send ( mail , recipient );
    postman send mail recipient
```

# Keyword messages for Java developers

```
    postman.send(mail,recipient);
    postman . send ( mail , recipient );
    postman send mail recipient
    postman send mail to recipient
```

# Keyword messages for Java developers

```
    postman.send(mail,recipient);
    postman . send ( mail , recipient );
    postman send mail recipient
    postman send mail to recipient
    postman send: mail to: recipient
```

# Keyword messages for Java developers
In Java
```language=java
    postman.send(mail,recipient);
```
In Pharo
```
    postman send: mail to: recipient
```
- the message
  - is named `send:to:`
  - is sent to `postman`
  - includes two arguments \(`mail` and `recipient`\)

# Conditionals are just messages
- in Java, `if`, `else`, `for`, `while`, `do`, ... are language keywords
- in Pharo, conditional expressions are messages
- booleans are objects

```
fullName isEmpty
   ifTrue: [ 'FirstnameLastname' ]
   ifFalse: [ fullName ]
```

# Loops are just messages

```
4 timesRepeat: [ self doSomething ]
```

```
0 to: 100 do: [ :i | ... ]
```

```
0 to: 100 by: 3 do: [ :i | ... ]
```

```
aCollection do: [ :each | ... ]
```

# Summary
- Three kinds of messages: unary, binary and keywords
- \(\) > unary > binary > keywords
- Conditionals are messages
- Loops too
