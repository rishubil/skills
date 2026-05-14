---
title: Functions
source: https://developer.garmin.com/connect-iq/monkey-c/functions/
---

Functions are the meat [<sup>1</sup>](#fntarg_1) of your program. Functions define discrete callable units of code.

Monkey C functions can take arguments, but because Monkey C is a dynamically typed language the argument types is not declared; just its name. Also, it is not necessary to declare the return value of a function, or even if a function returns a value, because all functions return values.

Functions can exist in a class or module, or appear in the global module.

## Variables, Expressions, and Operators

The basic types supported by Monkey C are:

- **Integers** - 32-bit signed integers
- **Floats** - 32-bit floating point numbers
- **Longs** – 64-bit signed integers
- **Doubles** – 64-bit floating point numbers
- **Booleans** - `true` and `false`
- **Chars** - Unicode characters
- **Strings** - strings of characters
- **Objects** – Instantiated objects (defined with the class keyword)
- **Arrays** - Allocated with the syntax `new [X]` where 'X' is an expression computing the size of the array
- **Dictionaries** - Associative arrays, allocated with the syntax `{}`

### Keywords

Here is a list of keywords in the Monkey C programming language. You cannot use any of the following as variables or symbols in your programs. The keywords `native` and `alias` are reserved, even though it is not currently used. `true`, `false`, `null`, `NaN`, `new`, `and`, and `or` might seem like keywords, but they are actually literals and operators; you cannot use them as identifiers in your programs.

| `as` | `const` | `enum` | `has` | `module` | `self` | `using` |
| --- | --- | --- | --- | --- | --- | --- |
| `break` | `continue` | `extends` | `hidden` | `private` | `static` | `var` |
| `case` | `default` | `finally` | `if` | `protected` | `switch` | `while` |
| `catch` | `do` | `for` | `instanceof` | `public` | `throw` |  |
| `class` | `else` | `function` | `me` | `return` | `try` |  |

### Declaring Variables

All local variables must be declared ahead of time using the `var` keyword. In the Monkey C language, all values (including numeric values) are objects.

```java
var n = null;               // Null reference
var x = 5;                  // 32-bit signed integers
var y = 6.0;                // 32-bit floating point
var l = 5l;                 // 64-bit signed integers
var d = 4.0d;               // 64-bit floating point
var bool = true;            // Boolean (true or false)
var c = 'x';                // Unicode character
var str = "Hello";          // String
var arr = new [20 + 30];    // Array of size 50
var dict = { x=>y };        // Dictionary: key is 5, value is 6.0
var z = arr[2] + x;         // Null pointer waiting to happen
```

Monkey C supports the following operators:

| Precedence | Operator | Description |
| --- | --- | --- |
| 1 | `new` | creation |
|  | `!` | logical NOT |
|  | `~` | bitwise NOT |
|  | `( )` | function invocation |
| 2 | `*` | multiplication |
|  | `/` | division |
|  | `%` | modulo |
|  | `&` | bitwise AND |
|  | `<<` | left shift |
|  | `>>` | right shift |
| 3 | `+` | addition |
|  | `-` | subtraction |
|  | `\|` | bitwise OR |
|  | `^` | bitwise XOR |
| 4 | `<` | less than |
|  | `<=` | less than or equals |
|  | `>` | greater than |
|  | `>=` | greater than or equals |
|  | `==` | equals |
|  | `!=` | not equals |
| 5 | `&&` | logical AND |
|  | `and` |  |
| 6 | `\|\|` | logical OR |
|  | `or` |  |
| 7 | `?:` | conditional |

### Symbols

Symbols are lightweight constant identifiers. When the Monkey C compiler finds a new symbol, it will assign it a new unique value. This allows symbols to be used as keys or constants without explicitly declaring a const or enum:

```java
var a = :symbol_1;
var b = :symbol_1;
var c = :symbol_2;
Sys.println( a == b );  // Prints true
Sys.println( a == c );  // Prints false
```

Symbols can be useful when wanting to create keys without having to declare an enum:

```java
var person = { :firstName=>"Bob", :lastName=>"Jones" };
```

### Constants

Constants are named, immutable values declared with the `const` keyword. These are useful for storing unchanging values that may be used repeatedly throughout code. Constants must be declared at the module or class level; they cannot be declared within a function.

Constants support the same types as . It is important to note that with data structures like arrays, `const` functions similar to Java's `final` keyword. For example, a `const` array prevents the array from being replaced by a new instance, but the elements of the array may be modified.

```java
const PI = 3.14;
const EAT_BANANAS = true;
const BANANA_YELLOW = "#FFE135";
```

### Enumerations

Enumerations are explicit or auto-incrementing constant mappings from symbol to integer. Unless explicity set (see the second example), each proceeding symbol is automatically assigned the value of its predecessor plus one, starting with `0`. So, in the following example, the symbol Monday is automatically assigned the value `0`, Tuesday is assigned `1`, and so on. These symbols can be used just like constant variables (which is essentially what they are). Enums must be declared at the module or class level; they cannot be declared within a function.

```java
enum {
    Monday,   // Monday = 0
    Tuesday,  // Tuesday = 1
    Wednesday // Wednesday = 2
    // ...and so on
}
```
```java
enum {
    x = 1337, // x = 1337
    y,        // y = 1338
    z,        // z = 1339
    a = 0,    // a = 0
    b,        // b = 1
    c         // c = 2
}
```

### Calling Methods and Functions

To call a method within your own class or module, simply use the function call syntax:

```typescript
function foo( a ) {
    //Assume foo does something really impressive
}

function bar() {
    foo( "hello" );
}
```

If calling on an instance of an object, precede the call with the object and a '`.`'.

When accessing class members, `public` and `protected` variables should be accessed using either one of the following formats:

```typescript
var x = mMemberVariable;
var y = self.mMemberVariable;
```

Overridden parent member functions should be accessed using the following syntax:

```typescript
class A
{
    function overridableMethod() {
        System.println("I am A!");
    }
}

class B extends A
{
    function overridableMethod() {
        System.println("B wins!");
        A.overridableMethod();
    }
}
```

The syntax of `SuperClass.memberVariable` is not supported in the Monkey C language. Always use `self` to access member variables of super classes.

### If Statements

`if` statements allow branch points in your code:

```java
myInstance.methodToCall( parameter );

if ( a == true ) {
    // Do something
} else if ( b == true ) {
    // Do something else
} else {
    // If all else fails
}

// Monkey C also supports the ternary operator
var result = a ? 1 : 2;
```

The expression inside the `if` statement is required to be an expression; assignments are not allowed. Things that will evaluate to true are:

- `true`
- A non-zero integer
- A non-null object

### Switch Statements

Like `if` statements, `switch` statements also allow branch points in your code. Deciding whether to use `if` statements or a `switch` statement is based on readability and the expression that the statement is testing.

A `switch` statement tests expressions based only on a single object. Like `if` statements, the expression inside the `switch` statement is required to be an expression; assignments are not allowed. You can have any number of `case` statements within a `switch` statement. Each `case` is followed by the object or `instanceof` object to be compared to and a colon:

```typescript
switch ( obj ) {
    case true:
    // Do something
    break;
    case 1:
    // Do something
    break;
    case "B": {
        // Do something
        break;
    }
    // Executed based on the type
    // instead of the value
    case instanceof MyClass:
    // Do something
    break;
    default:
    // If all else fails
    break;
}

// Monkey C also supports fall-through into the next case statement
switch ( obj ) {
    case false:
    // Do something
    // Fall through and execute the code in the next case block
    case 2: {
        // Do something
        break;
    }
    case instanceof MyOtherClass:
    // Do something
    break;
    case "B":
    // Do something
    // Fall through and execute the code in the default block
    default:
    // If all else fails
    break;
}
```

The `instanceof` operator is discussed in more detail later in this guide.

When the object being switched on is either equal to or an instance of the value defined in a `case` statement, the statements following that `case` will execute until a `break` statement is reached. Each `break` statement terminates the enclosing `switch` statement. Without a `break` statement, `case` statements fall through: all statements after the matching `case` label are executed in sequence, regardless of the expression of the subsequent `case` labels, until a `break` statement is encountered. A final `break` statement is not required because control flow will just naturally fall out of the `switch` statement.

A `switch` statement can also have a single optional `default` case, which is not required to appear at the end of the `switch` statement. The `default` case handles all objects that are not explicitly handled by one of the `case` statements.

### Switch Block Variable Scoping

The body of a `switch` statement is known as the "switch block". Variables declared within the switch block will be scoped at the switch block level. Variables defined within curly braces of a case block will be scoped at that code block level. Additionally, due to the nature of fall-through cases, all variables defined at the switch block level must be initialized before being used in any subsequent `case` statements. For instance:

```java
switch ( obj ) {
    case true:
    var aaa = 1; // Scoped at the switch block level
    ...
    case 1:
    var zzz = aaa; // Results in a compiler error because aaa was not initialized in this case block
    ...
    break;
    case "B": {
       var aaa = true; // Scoped at the code block level within the curly braces, no scoping conflict with variable aaa at the swtich block level
       ...
       break;
    }
    case instanceof MyClass:
    var aaa = "Hello!" // Results in a compiler error because aaa has already been defined in the switch block
    ...
    default:
    aaa = 0; // aaa was defined in the first case and initialized at the beginning of the default case, no errors!
    var good = aaa;
    ...
    break;
}
```

### Loops

Monkey C supports `for` loops, `while` loops, and `do/while` loops. `while` and `do/while` loops have a familiar syntax:

```java
// do/while loop
do {
    // Code to do in a loop
}
while( expression );

// while loop
while( expression ) {
    // Code to do in a loop
}
```

Loops must have braces around them because single-line loops are not supported:

```java
// Monkey C does allow for variable declaration in for loops
for( var i = 0; i < array.size(); i++ ) {
    // Code to do in a loop
}
```

Control within loops can be managed by using the `break` and `continue` statements. These should also have familiar behavior:

```java
// This for loop should only print 5, 6, and 7.
for (var i = 0; i < 10; i += 1) {
    if (i < 5) {
        continue;
    }
    System.println(i);
    if (7 == i) {
        break;
    }
}
```

### Returning Values From Functions

All functions return values in Monkey C. You can explicitly set the return value by using the `return` keyword:

```java
return expression;
```

The expression is optional. Functions without a return statement automatically return the last value operated on.

### Instanceof and Has

As a duck-typed language, Monkey C gives the programmer great flexibility, but the trade off is that the compiler cannot perform the type checking like in C, C++ or Java. Monkey C provides two tools to do runtime type checking— `instanceof` and `has`.

The `instanceof` operator offers the ability to check if an object instance inherits from a given class. The second argument is the class name to check against:

```java
var value = 5;
// Check to see if value is a number
if ( value instanceof Toybox.Lang.Number )
{
    System.println( "Value is a number" );
}
```

The `has` operator lets you check if a given object has a symbol, which may be a public method, instance variable, or even a class definition or module. The second argument is the symbol to check for. For example, assume we have magnetometer libraries in `Toybox.Sensor.Magnetometer`, but not all products have a magnetometer. Here is an example of changing your implementation based on those criteria:

```java
var impl;
// Check to see if the Magnetometer module exists in Toybox
if ( Toybox has :Magnetometer )
{
    impl = new ImplementationWithMagnetometer();
}
else
{
    impl = new ImplementationWithoutMagnetometer();
}
```

Monkey C's object-oriented design patterns in conjunction with the `has` and `instanceof` operator enables software that has implementations for many devices in one code base.

## Callbacks

Functions in Monkey C are not first class, meaning you cannot pass them as objects directly for use in other functions. However, using the `method()` function inherited from `Toybox.Lang.Object`, a class instance can create a `Method` object, which provides a way to invoke it as a callback method.

```java
class Foo
{
    function operation(a, b) {
        // The code here is really amazing. Like mind blowing amazing. You wish this method was in your program.
    }
}
function usageSample() {
    // Create a new instance of Foo
    var v = new Foo();
    // Get the callback for the operation method from the instance of Foo.
    var m = v.method(:operation);
    // Invoke v's operation method.
    m.invoke(1,2);
}
```

A ` Method` object will invoke a method on the instance of the object it came from. It keeps a strong reference to the source object.

Unlike classes, Modules do not inherit from Object so do not have access to the `method()` function. However, a new instance of `Method` can be created, which allows module-level functions to be invoked as callbacks in a similar fashion:

```typescript
import Toybox.Lang;

module Foo
{
    function operation() {
        // Do something
    }
}
function moduleSample() {
    var v = new Method(Foo, :operation);
    v.invoke();
}
```

[<sup>1</sup>](#fnsrc_1) Tofu for the vegetarians, BBQ for Kansans…
