---
title: Coding Conventions
source: https://developer.garmin.com/connect-iq/monkey-c/coding-conventions/
---

Here are guidelines for Monkey C code:

## Naming

- Modules and Classes are camel-cased with the first letter in upper case.
- Functions are camel-cased with the first letter always being lower case.
- Private class member variables are camel cased with the first character being an underscore (\_) and then the first letter lower case.
- Public class member variables are camel cased with the first letter lower case.
- Module variables should be camel cased with a lower cased first letter
- Enums must have a common prefix, e.g. *COLOR\_RED*, *COLOR\_BLUE*.
- In POMO (Plain Old Monkey C Objects) it is okay to have all public members.

## Source

- Put one class per Monkey C source file.
- Monkey C code should use spaces aligned four spaces per indent level. The Monkey C editor will automatically convert spaces to tabs and remove trailing white space.
- When defining modules, classes, functions, and enums, put the opening brace on the same line as the definition and the closing brace aligned with the first character as the definition.

## Definitions

- Avoid pure global variables when possible.
- Because modules are not purely lexical and have runtime memory cost, putting class definitions into the global module is acceptable.
- Avoid having public static members in class definitions; instead move those definitions into the parent module.
- In the first line of your class initialize function, always call the superclass initialize.

## Sample

Here is a sample:

```c++
class SampleName extends Toybox.Application.AppBase
{
    public var publicVar;
    private var _privateVar;

    function initialize() {
        AppBase.initialize();
    }
    // onStart() is called on application start up
    function onStart(state) {
    }

    // onStop() is called when your application is exiting
    function onStop(state) {
    }

    // Return the initial view of your application here
    function getInitialView(){
        return [new SampleNameView(), new SampleNameDelegate()];
    }
 }
```
