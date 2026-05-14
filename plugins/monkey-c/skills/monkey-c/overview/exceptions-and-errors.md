---
title: Exceptions and Errors
source: https://developer.garmin.com/connect-iq/monkey-c/exceptions-and-errors/
---

Monkey C supports structured exception handling for non-fatal errors from which there can be recovery. The syntax should be familiar for Java and Javascript developers:

```java
try {
    // Code to execute
}
catch( ex instanceof AnExceptionClass ) {
    // Code to handle the throw of AnExceptionClass
}
catch( ex ) {
    // Code to catch all execeptions
}
finally {
    // Code to execute when
}
```

You can use the `throw` keyword to throw an exception.

## Creating an Exception

If you are creating your own exception, follow these rules:

- Extend `Toybox.Lang.Exception`
- Initialize the superclass in the initializer
- Assign a string message to the `mMessage` member variable

For example, an app specific exception can be defined as follows:

```typescript
class AppSpecificException extends Lang.Exception {
    //! Constructor
    //! @param msg Message explaining cause
    function initialize(msg) {
        Exception.initialize();
        self.mMessage = msg;
    }
}
```

## Errors

Because Monkey C uses dynamic typing, there are many errors for which the compiler cannot check. If the error is of high enough severity, it will raise an fatal API error and cause your app to terminate at runtime. These errors cannot be caught.

Array Out Of Bounds

```
An attempt is being made to reference an array outside of its allocated bounds
```

Circular Dependency

There is a loop in the dependency graph of a module or object that prevents a module or object from being constructed

Communications Error

An error has occurred in [Bluetooth low energy](https://en.wikipedia.org/wiki/Bluetooth_low_energy) communications

File Not Found

The app file could not be found, which is usually caused when trying to load a resource from the app file

Illegal Frame

The return address on the stack is corrupted

Initializer Error

An error occurred in an initializer

Invalid Value

An argument passed to a function or method is invalid

Null Reference

A value is being requested from a null value

Out of Memory

Indicates no more system memory is available for allocation

Permission Required

An attempt was made to use a restricted API without permission

Stack Underflow

The stack pointer went past the bottom of the stack memory limit

Stack Overflow

The stack pointer went past the top of the stack memory limit

Symbol Not Found

An attempt was made to access a variable or method that does not exist in the specified object or method

System Error

A generic error used by the Toybox APIs for fatal errors

Too Many Arguments

Too many arguments used by a method, which are currently limited to 10 arguments

Too Many Timers

Too many `Timer::Timer` objects for the target device were started

Unexpected Type

Indicates an operation being done on a variable that is unsupported by the type; for example, trying to perform a bitwise OR on two string

Unhandled Exception

An `Exception` was thrown but was not caught by an exception handler

Watchdog Tripped

A Monkey C function has executed for too long; watchdogs prevent a Monkey C program from hanging the system via an infinite loop
