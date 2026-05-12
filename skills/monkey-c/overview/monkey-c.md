---
title: Hello Monkey C!
source: https://developer.garmin.com/connect-iq/monkey-c/
copyright: "(c) Garmin Ltd. or its subsidiaries"
license: "All rights reserved (no open license granted) — see ../NOTICE.md"
---

![](https://developer.garmin.com/connect-iq/resources/programmers-guide/smart-monkey.png)

There is no better way to learn Monkey C than by jumping right in. Let's take a look at the application object of a watch face.

```java
using Toybox.Application as App;
using Toybox.System;

class MyProjectApp extends App.AppBase {

    // onStart() is called on application start up
    function onStart(state) {
    }

    // onStop() is called when your application is exiting
    function onStop(state) {
    }

    // Return the initial view of your application here
    function getInitialView() {
        return [ new MyProjectView() ];
    }
}
```

If this looks familiar and non-threatening, that's the point. Monkey C is intended to be the language you didn't know you already knew.

At the top is a using statement, which is analogous to C++'s `using` statement, or an `import` in Java™, Ruby, or Python™. `using` statements lexically bring modules into our name space. After a `using` clause, we can refer to a module by its shortened name (in this case `System`). `Toybox` is the root module for Monkey C system modules; all the cool toys are kept in there.

To print out values to the debug console, use:

```typescript
System.println( "Hello Monkey C!" );
```

`System` refers to the `Toybox.System` module we imported with the `using` statement. Unlike Java namespaces, modules in Monkey C are static objects that can contain functions, classes, and variables. The `println()` function should be familiar to Java programmers—it prints a string and automatically adds a new line. The `System` module has a number of useful functions:

- `print` and `println` send output to the console
- `getTimer` returns the current millisecond timer. The value is a 32 bit integer representing the number of milliseconds the system has been running. The value can be used for timing but is allowed to roll over.
- `getSystemStats` provides statistics from the runtime system
- `exit` will terminate your application
- `error` will exit your application while logging an error message

## Differences From Other Languages

As Italian and Spanish derive from Latin, Monkey C derives heavily from other popular languages. C, Java™, JavaScript, Python™, Lua, Ruby, and PHP all influenced the design for Monkey C. If you are familiar with any of those languages, Monkey C should be easy to pick up.

### Java

Like Java, Monkey C compiles into byte code that is interpreted by a virtual machine. Also like Java, all objects are allocated on the heap, and the virtual machine cleans up memory (Java through garbage collection, Monkey C through reference counting). Unlike Java, Monkey C does not have primitive types—integers, floats, and chars are objects. This means primitives can have methods just like other objects.

While Java is a statically typed language, Monkey C is [*duck typed*](https://en.wikipedia.org/wiki/Duck_typing). In Java, the developer must declare the types for all parameters of a function, and declare the return value type. The Java compiler checks these at compile time to ensure type safety. Duck typing is the concept of "if it walks like a duck, and quacks like a duck, then it must be a duck" [<sup>1</sup>](#fntarg_1). For example:

```typescript
function add( a, b ) {
    return a + b;
}

function thisFunctionUsesAdd() {
    var a = add( 1, 3 ); // Return  4
    var b = add( "Hello ", "World" ); // Returns "Hello World"
}
```

The Monkey C compiler does not verify type safety, and instead causes a runtime error if a function mishandles a method.

Monkey C modules serve a similar purpose as Java packages, but unlike packages, modules can contain variables and functions. It is common for static methods to exist in the module as opposed to a particular class.

### Lua/JavaScript

The main difference between JavaScript or Lua and Monkey C is that functions in Monkey C are not first class. In JavaScript, a function can be passed to handle a callback:

```javascript
function wakeMeUpBeforeYouGoGo() {
    // Handle completion
}

// Do a long running thing, and pass callback to call when done.
doLongRunningTask( wakeMeUpBeforeYouGoGo );
```

In Lua, to create an object, you bind functions to a hash table:

```lua
function doSomethingFunction( me ) {
    // Do something here
}

// Constructor for MyObject
function newMyObject() {
    local result = {};
    result["doSomething"] = doSomethingFunction;
}
```

Neither of these techniques works in Monkey C, because functions are bound to the object they are created in.

To create a callback in Monkey C, create a *Method object*. Method objects are a combination of the function and the object instance or module they originate from.

### Ruby, Python, and PHP

Objects in Ruby and Python are hash tables, and have many of the properties of hash tables. Functions and variables can be added to objects at run time.

Monkey C objects are compiled and cannot be modified at runtime. All variables have to be declared before they can be used, either in the local function, the class instance, or in the parent module.

When importing a module, all classes inside the module have to be referenced through their parent module. You import modules, not classes, into your namespace.

[<sup>1</sup>](#fnsrc_1) This is different than Monkey Typing, where a thousand monkeys over infinite time write the works of Shakespeare.
