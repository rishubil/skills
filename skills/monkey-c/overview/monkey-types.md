---
title: Monkey Types
source: https://developer.garmin.com/connect-iq/monkey-c/monkey-types/
---

Monkey Types is the gradual type system for the Monkey C language. The type system is designed to recognize Monkey C's historically duck-typed nature but add the necessary components to type check your applications at compile time.

Monkey Types has the following goals:

1. **Compatibility** - Breaking changes to the Monkey C language would require rework to thousands of Connect IQ apps. Monkey Types extends the Monkey C grammar but avoids breaking changes. Monkey Types is also designed to not rely on additional run time information. Because of this, you can use Monkey Types for apps that run on all Connect IQ compatible devices.
2. **Ease of Use** - The philosophy of Monkey C is to be *the language you didn't know you already knew*. We want the experience of writing Monkey C to be like deja-vu. Likewise, Monkey Types borrows heavily from Kotlin, Swift, and Typescript in its design.
3. **Flexibility** - Monkey Types is a gradual type system. You can leave the type scaffolding off if you choose, or you can strictly type your app.

The Connect IQ type checker is disabled by default and is enabled with the `-l` compiler option. There are four levels of type checking:

| Option | Level | Description |
| --- | --- | --- |
| `-l 0` | Silent | No type checking; keep everything dynamically typed |
| `-l 1` | Gradual | Type check any statement where typing can be inferred, otherwise stay silent |
| `-l 2` | Informative | Type check only what has been typed, warn about ambiguity |
| `-l 3` | Strict | Do not allow compiler ambiguity |

Let's cover the new syntax available for communicating type information to the type system.

## The as Clause

Monkey Types introduces a new keyword `as`. You use `as` to bind a type to a member variable, module variable, function argument, or function return value. Locals are always type inferred at assignment.

Once a type has been bound to a value, the compiler will only allow values of that type to be assigned.

```typescript
using Toybox.Lang;
using Toybox.System;

var globalX as Lang.Number = 0;

function hasANumber() {
    globalX = 2;  // Allowed
    globalX = "2"; // Not allowed
    System.println("globalX = " + globalX);
}
```

In this example we are declaring that global variable `globalX` will only accept values of `Toybox.Lang.Number`. Once that has been declared, the compiler will only allow values of that type to be assigned to `globalX`.

Since Monkey C is a duck-typed language, only allowing a single type to be bound to a variable would be overly restrictive. An `as` clause is allowed to have an `or` clause attached if a variable accepts multiple types.

```typescript
using Toybox.Lang;
using Toybox.System;

var globalX as Lang.Number or Lang.String = 0;

function hasANumber() {
    globalX = 2;  // Allowed
    globalX = "2"; // Allowed
    System.println("globalX = " + globalX);
}
```

## The import Statement

In traditional Monkey C, the `using` statement brings a `module` suffix into the namespace of the file being processed. To access any functions, variables, or class definitions, the module suffix must be referenced.

For adding type information, all that module prefixing is annoying. Monkey Types introduces the `import` statement. When you use `import` it will bring the *module suffix and all classes in the module into the type namespace*. This allows classes in a module to be accessed without the module suffix, making for easier typing. Functions still require the module suffix to be accessed.

```typescript
import Toybox.Lang;
import Toybox.System;

// Import lets you say goodbye to
// module prefixes
var globalX as Number or String = 0;

function hasANumber() {
    globalX = 2;  // Allowed
    globalX = "2"; // Allowed
    // Still require prefixes in code
    System.println("globalX = " + globalX);
}
```

Note `import` does not support using `as` for renaming modules in a source file [<sup>1</sup>](#fntarg_1).

## Named Versus Anonymous Types

As you can see from the above example, the type system can allow for complicated type definitions. There are times where a type pattern is repeated that you just want to refer to it by a name.

A `typedef` statement allows you to create a *named type* in the application namespace. For example, the following would create a poly type named `Numeric` in the global namespace. The function `add` then binds `Numeric` to parameters `a` and `b` and its return value by having the `as` clauses refer to the `Numeric` type declaration.

```typescript
import Toybox.Lang;

typedef Numeric as Number or Float or Long or Double;

function add(a as Numeric, b as Numeric) as Numeric {
    return a + b;
}
```

If you do not wish to name your type declarations, you can always use the `as` clause to build the type declaration in line as an anonymous type.

## Types

Monkey Types allows you to add a layer of type scaffolding to your Monkey C code. The type system allows for a lot more than associating variables with classes.

This section will overview the type declarations you can use.

### Any

Any variable, function argument, or function return value that does not have a type bound to it is of type Any. The Any type can be anything, including nothing. Values of type Any follow the traditional duck type rules of Monkey C.

To bind Any to a value, simply do not add an `as` clause to it's declaration. There is no keyword to bind Any to a value.

### Void

The void type is only for return values, and communicates that a function does not allow return values. It also communicates that a function should not expect a return value by calling this function.

```typescript
import Toybox.Lang;

function doNothing() as Void {
    // Compiler error - this is failing to
    // do nothing.
    return true;
}

function doSomething() as String {
    // Compiler error - cannot assign value
    // from a function that returns nothing
    var x = doNothing();
    // Compiler error - doSomething should
    // return a String
}
```

### Concrete

Concrete types are a single reference to a declared class in the program namespace. This is the most traditional and most familiar use of typing. If a value is bound to a concrete type, it will only accept values of that class or any derived classes.

```typescript
import Toybox.Lang;
import WoolMarket;

class Wool {
    public var bagsFull;

    public function initialize(bags as Number) {
        bagsFull = bags;
    }
}

class Sheep {
    public var wool as Wool;

    public function initialize() {
        wool = new Wool(1);
    }
}

class BlackSheep extends Sheep {
    public function initialize() {
        Sheep.initialize();
        wool = new Wool(3);
    }
}

function processSheep(baa as Sheep) {
    if(baa.wool != null) {
        WoolMarket.sellWool(baa.wool);
    }
}

function example() {
    // Allowed
    processSheep(new Sheep());
    processSheep(new BlackSheep());
    // Not allowed
    processSheep(new Wool());
}
```

Note that concrete types do not implicitly accept `null` as a value. If you want a value to also accept `null` you must make a poly type (see for more information).

### Poly

Poly types allow the concatenation of multiple types into a single type. This allows for the type system to model the duck-type nature of Monkey C. To create a poly type, you simply use the `or` clause when defining your type.

A poly type will accept:

1. A value whose type is bound to one of the types within the poly type
2. A value bound to a poly type whose types are within the definition of the destination type
```typescript
import Toybox.Lang;

typedef Addable as Number or Float or Long or Double or String;
typedef Numeric as Number or Float or Long or Double;

function add(a as Addable, b as Addable) as Addable {
    return a + b;
}

function subtract(a as Numeric, b as Numeric) as Numeric {
    return a - b;
}

function doWork() {
    // Allowed
    var x as Addable = add("1", "2");
    // Not allowed; Addable has String which is
    // not within Numeric
    var y as Numeric = subtract(x, 2);
}
```

### Interface

An interface type requires a class to contain a set of member declarations. The members can be member variables and functions.

```typescript
import Toybox.Lang;

typedef LittleBoys as interface {
    var frogs as Array<Frogs>;
    var snails as Array<Snails>;
    var puppyDogTails as Array<PuppyDogTails>;
};

// Implements LittleBoys interface
class MaleChild {
    var frogs as Array<Frogs>;
    var snails as Array<Snails>;
    var puppyDogTails as Array<PuppyDogTails>;
}
```

Note that the class does not require additional decoration to implement the interface. This allows anonymous interfaces to be defined within function arguments.

```typescript
// Processing
function example(you as interface {
    var frogs as Array<Frogs>;
})
```

### Container

The Monkey C language has two native container types, `Array` and `Dictionary`. While the Monkey Types system does not support generics, it does allow for the developer to type the value type of an `Array` or the key and value type of a `Dictionary`.

```typescript
import Toybox.Lang;

typedef ContainerA as Array<Number>;
typedef ContainerB as Dictionary<String, Number>;
```

Container types only match other container types if both the key and value types are equivalent. An `Array<String>` only matches an `Array<String>` and not an `Array<String or Number>`.

Monkey C does not infer container types at this time, so you will need to declare your containers. If you want to create a new typed array or dictionary you can use the following syntax:

```typescript
class ContainerClass {
    // Array of 10 items that takes only numbers
    var typedArray as Array<Number> = new Array<Number>[10];
    // Initialized array
    var initializedArray as Array<Number> = [1, 2, 3, 4, 5] as Array<Number>;
    // Initialized dictionary
    var initializedDictionary as Dictionary<String, String> = {"this"=>"that"} as Dictionary<String, String>;
}
```

### Tuples

A common pattern in Monkey C is to use arrays as structured groupings. Monkey types allows modeling an array by binding the indexed items to types.

Think of Tuple types like Dictionary types, except the key is implied by the order. In the following example, the array being returned is automatically typed as a Tuple of types `[StartView, StartDelegate]`. This is typed against the allowed return value `[Views, InputDelegates]` and found to match:

```typescript
function getInitialView() as [Views] or [Views, InputDelegates] {
    return [ new StartView(), new StartDelegate() ] ;
}
```

The rules of Tuple type A matching Tuple type B are as follows:

- Tuple A and B must be the same length
- For every index, every type in A must be an instance of B

Arrays created with the `[ value, value...]` syntax will now be typed as a Tuple instead of an `Array<Any>`. You can use Container types if that better matches the pattern you are implementing, but Tuples have a natural compatibility with Container types. Tuples of type `[A, B, C]` shall be instance of `Array<A or B or C>` if the types A, B, and C are in the polytype definition of the container type.

```typescript
function sumArray(x as Array<Numeric>) as Number {
    var result = 0;
    for (var i = 0; i < x.size(); i++) {
        result += x[i];
    }
    return result;
}

function sumThisTuple() as Number{
    // This should pass type checking because the
    // Tuple [Number, Number... ] should be an instanceOf Array<Numeric>
    return sumArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
}
```

Tuple types are also more mutable. As the underlying array changes, they are modified as long as the type system can keep up. The type system will not track changes to the tuple's types when passed as an argument to another method.

```typescript
function foo(x as [Number, Number, Number]) as [Number, Number, Number] {
    x[1] = "Hello"; // Allowed, type is now [Number, String, Number]
    return x; // Error, type mismatch
}
```

### Dictionary

A common pattern in Monkey C is to use an options dictionary as an argument. This allows for extensible APIs. Monkey Types allows modeling an options dictionary by binding key literals to types.

```typescript
import Toybox.Lang;

function doWork(options as {
    :option1 as String,
    :option2 as {
        "name" as String,
        "value" as Number
    }
})
```

If a dictionary is declared inline, the compiler will track the types bound to the values, and then type check to see if all the value types match. It will not require all keys to be provided, and it will not error if additional keys are added.

```typescript
doWork({:option1=>"x", :option3=>true})
```

### Enumerations

Enumerations can now be named types by appending a name to the declaration. Enumeration values will be bound to both their enumeration type as well as their value type.

```typescript
import Toybox.Lang;

enum Dog {
    SPOT = "Spot",
    LUKE = "Luke",
    POCO = "Poco",
    COMMODORE = "Commodore",
    BINGO = "B_I_N_G_O"
}

function getDogName(dog as Dog) as String {
    // Return the dog name
    return dog.toString();
}
```

### Callback

The base object of Monkey C contains the `method` method to create `Method` callback objects [<sup>2</sup>](#fntarg_2). The callback type allows you to type `Method` objects based on what the expected parameters and return values are.

```typescript
import Toybox.Lang;

function doWork(
    x as Method(a as Number) as String
) as String {
    return x.invoke(2);
}
```

### Null

Monkey Types treats Null as its own unique type. More importantly, Monkey Types requires explicit declaration if `null` is an allowed value.

```typescript
function doWork() as Number or Null
```

The `?` can be used with single type declarations to make it a null accepting poly type.

```typescript
function doWork() as Number?
```

## Type Matching and Ambiguity

Because of the duck type nature of Monkey C, ambiguity is inherit to Monkey Types. Ideally, type systems would have very clear rules for if a type does or doesn't match, but Monkey Types has True, False, and Maybe [<sup>3</sup>](#fntarg_3).

Assuming we have the following:

```
var a as A;
var b as B;

a = b; // Is this assigment allowed?
```

You can use the following table

| A↓ B→ | Any | Concrete | Poly | Interface | Container | Dictionary | Enum | Callback | Null |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Any** | True | True | True | True | True | True | True | True | True |
| **Concrete** | Maybe | True if B is or extends A | Maybe if one of the poly types in B matches A, False otherwise | False | Maybe if A is a Dictionary or Array | Maybe if A is a Dictionary, False otherwise | True if enum value type matches A, False otherwise | False | False |
| **Poly** | Maybe | True if B is a type within A, False otherwise | True if all references exist in both A and B. Maybe if there are some types in B not in A. False if no matching types between B and A | True if B is a type within A, False otherwise | True if B is a type within A, False otherwise | True if B is a type within A, False otherwise | True if B is a type within A, False otherwise | True if B is a type within A, False otherwise | True if B is a type within A, False otherwise |
| **Interface** | Maybe | True if B is an object that contains all members of interface A, False otherwise | Maybe if the poly contains a matching type | True if B's interface contains all members in A. | True if classes Array or Dictionary contains all members of interface, False otherwise | True if class Dictionary contains all members of interface, False otherwise | False | False | False |
| **Container** | Maybe | False | Maybe if one of the poly types in B matches A, False otherwise | False | True if container type and key/value types match exactly, False otherwise | False | False | False | False |
| **Dictionary** | Maybe | False | Maybe if one of the poly types in B matches A, False otherwise | False | True if all keys match the key type and values match the value type (if applicable), False otherwise | True if all keys match the key type and values match the value type (if applicable), False otherwise | False | False | False |
| **Enum** | Maybe | True if value type of enum value B matches concrete type A | Maybe if one of the poly types in B matches A, False otherwise | False | False | False | True if enum types match, false otherwise | False | False |
| **Callback** | Maybe | False | Maybe if one of the poly types in B matches A, False otherwise | False | False | False | False | True if function signatures match, False otherwise | False |
| **Null** | Maybe | False | Maybe if one of the poly types in B matches A, False otherwise | False | False | False | False | False | True |

The type checker can run at three different levels based on your level of comfort with ambiguity.

1. **Silent** - Type match failures are marked as errors, but ambiguity is ignored
2. **Warning** - Type match failures are marked as errors, and ambiguity is marked as a warning
3. **Error** - Type match failures and ambiguity are marked as errors

Compiling a code base with ambiguity muted can find obvious type errors, while compiling code when erroring on ambiguity requires adding type scaffolding throughout the code. Monkey Types is designed to allow you to build towards aggressive typing if you choose to, while still adding value if you don't.

## Typing Within Functions

Up until now we have been explicitly adding type scaffolding. While this makes for very readable and explicit code, it can add lots of boilerplate to implementation.

Unlike with class instance variables, the Monkey Types system will infer the type of a local variable by tracking assignments.

```typescript
import Toybox.Lang;
import OldMacDonaldsFarm;

function handleDog(dog as Dog, here as Array, there as Array, everywhere as Array) {
    here.add(dog.woofWoof());
    there.add(dog.woofWoof());
    everywhere.add(dog.woofWoof());
}

function handleCat(cat as Cat, here as Array, there as Array, everywhere as Array) {
    here.add(cat.meowMeow());
    there.add(cat.meowMeow());
    everywhere.add(cat.meowMeow());
}

function eieio() {
    var here = [], there = [], everywhere = [];
    // Animal will be typed as a Dog based
    // on the assignment. No need to declare
    // it's type
    var animal = new OldMacDonaldsFarm.Dog();
    // Allowed, animal is currently assigned a Dog value
    handleDog(animal, here, there, everywhere);
    // Animal will now be typed as a Cat based on
    // the assignment
    animal = new OldMacDonaldsFarm.Cat();
    // Allowed, animal is currently assigned a Cat value
    handleCat(animal, here, there, everywhere);
}
```

The inference will follow through branches. If the type is unclear based on which branch is taken, the type system will make a poly type of the options until the next assignment.

```typescript
import Toybox.Lang;

function process(a as Boolean) as Boolean? {
    var x = null;

    if(a) {
        x = true;
    }
    // At this point, x is now the poly type
    // Boolean or Null
    return x;
}
```

When a value has a known type definition, the type checker will validate if method calls are allowed.

```typescript
import Toybox.Lang;

class A {
    function foo() {};
    function bar() {};
}

function process() {
    var a = new A();
    a.foo(); // Allowed
    a.bar(); // Allowed
    a.fonz(); // Not allowed
}
```

With container types, it is also possible to bind a type to the initialized value. This will put controls on what can be assigned to the container, but allow the local to have any value.

```typescript
import Toybox.Lang;

function example() {
    var a = {} as Dictionary<String, String>;
    a["key"] = "value" // <-- Assignments to a's value must obey type

    a = null; // <-- a is Any and can be assigned to null
}
```

### Return Values and Void

By default functions return Any. If you bind a type to a function return value, the type checker will ensure that you return values of that type.

```typescript
import Toybox.Lang;

function isTrue() as Boolean {
    return "true"; // Not allowed
}
```

If your function does not have a return value, you can use the `Void` type. This will ensure the function doesn't return values and error if a function tries to assign the return value of the function.

### Any and Type Ambiguity

Any function parameter without a bound type will be of type Any. The ambiguity of the parameter will percolate to any member it interacts with in an expression. If you provide all type definitions, type checking can protect them from many kinds of common errors. However, just a little ambiguity can prevent any level of checking. Take this example where a function has a result check but does not have a argument type for `a`.

```typescript
import Toybox.Lang;

function foo(a) as Integer? {
    // a is of type Any, so Monkey Types can't identify what doThis() is being called
    var x = a.doThis();
    // x is of type Any, so we can't know what the result type is
    var y = x + 3;
    // What is Y? What is Why? What is Love?
    return y;
}
```

Because `a` is Any, Monkey Types can't make any determination on any members of it, and by proxy Monkey Types can't make determination on the results of accessing those members.

### Type Casting

The `as` keyword can also be used in an expression to type cast a value to another type. This can be useful if the type is not clear to the type system.

```typescript
import Toybox.WatchUi;

function process(a as View) {
    (a as MyView).specialMyViewMethod();
}
```

Because Monkey Types are purely lexical and exist only at compile time, type casting will not result in runtime changes.

### Runtime Type Checking

One of the goals of Monkey Types was to not add any runtime overhead. This allows Monkey Types to work on all Connect IQ compatible products out of the gate, but it does add a cost when it comes to runtime type checking. Put simply: while at compile time you have access to an expressive type system, at runtime `instanceof` and `has` have the same limits as they had before. For cases involving poly types of concrete types this can work fine.

```typescript
import Toybox.Lang;

function example(x as Number or Float) as Boolean {
    switch(x) {
        case instanceof Number:
            doNumberImpl(x);
            break;
        case instanceof Float:
            doFloatImpl(x);
            break;
    }
}
```

Unfortunately not every scenario can be resolved this way. For example, lets say we had the following scenario:

```typescript
typedef Nimble as interface {
    function isNimble() as Boolean;
};

typedef Quick as interface {
    function isQuick() as Boolean;
};

function handleCandleStick(jack as Nimble or Quick) {
    if(jack instanceof Nimble and jack instanceof Quick) {
        if(jack.isNimble() and jack.isQuick() and jack has :jumpOverCandleStick) {
            jack.jumpOverCandleStick();
        }
    }
}
```

In the case of `handleCandleStick` the interfaces `Nimble` and `Quick` are lexical types and only exist at compile time. This will cause a compiler error because `instanceof` can only be used on concrete classes and not lexical types. In this case we can use `has` to resolve this issue.

```typescript
function handleCandleStick(jack as Nimble or Quick) {
    if(jack has :isNimble and jack has :isQuick and jack has :jumpOverCandleStick) {
        if(jack.isNimble() and jack.isQuick()) {
            jack.jumpOverCandleStick();
        }
    }
}
```

### If-Splitting

In languages like Java, an object's type is assumed to be whatever it was declared to be. This can lead to some very redundant casting or generation of lots of unnecessary locals to communicate to the Compiler that something isn't what it was declared to be.

```java
public boolean foo(SomeInterfaceType x) {
    if(x instanceof SomeConcreteType) {
        // My life will just be easier if I make
        // a new variable, even though it should
        // be possible to assume that x is
        // a SomeConcreteType
        SomeConcreteType y = (SomeConcreteType)x;
        // Do operations on y
    }
}
```

The Monkey C type system will take advantage of if-splitting, where the branch expression causes the types for variables to mutate within the true and false cases.

```typescript
import Toybox.Lang;

public function foo(x as Number?) as Boolean {
    if(x != null) {
        // Within this block assume x is Number and not null
    } else {
        // Within this block assume x is null
    }
}
```

The ==,!=, and `instanceof` operators will mutate the types based on the following rules

| type | \== | != | instanceof | !instanceof |
| --- | --- | --- | --- | --- |
| Any | Ignore | Ignore | Mutate type to `instanceof` type | Ignore |
| Concrete | Ignore | Ignore | Mutate type to `instanceof` type | Ignore |
| Poly | If == is `null`, mutate to Null type | if!= is `null`, mutate to poly type minus `null`. | Mutate type to `instanceof` type | Mutate type to poly type minus type from `instanceof` |
| Interface | Ignore | Ignore | Mutate type to `instanceof` type | Ignore |
| Container | Ignore | Ignore | Ignore | Ignore |
| Dictionary | Ignore | Ignore | Ignore | Ignore |
| Enum | Mutate to enum value type | Ignore | Ignore | Ignore |
| Callback | Ignore | Ignore | Ignore | Ignore |
| Null | Ignore | Ignore | Ignore | Ignore |

Expressions can also be modified using the && and || operators. With the && operator, the mutation will carry through the expression, being further modified as the expression continues.

```typescript
import Toybox.Lang;

typedef Addable as Number or Float or Long or Double or String;

public function foo(x as Addable?) {
    // In the first clause, x is modified to remove the null
    // from the poly type. In the second clause, the new polytype
    // is modified to be a String concrete type.
    if(x != null &&
       x instanceof String) {
        // Within this block assume x is a string
    }
}
```

With || operators, a new poly type is created with the results of both operations

```typescript
import Toybox.Lang;

typedef Addable as Number or Float or Long or Double or String;

public function foo(x as Addable?) {
    if(x instanceof Number ||
       x instanceof Float) {
        // Within this block assume x is a Number or Float
    }
}
```

When if-splitting on member variables, all type mutations will be removed if a function is invoked.

## Typing Modules and Classes

Class member variables are bound to type Any by default. Unlike local variables, member variables are not type inferenced based on assignment. Adding type scaffolding to your member variables and names to your enumerations will allow for stronger type checking. Constants are typed based on assignment.

```typescript
class Example {
    // Member variable
    private var _x as Number = 0;

    // Enum values can be explicitly assigned, or by default will
    // be numerically incremented values.
    enum NamedEnum {
        NAMED_ENUM;
    }

    // Constants assume their type by assignment
    private const _constant = "Constant";
}
```

If you add type scaffolding, you must either initialize the variable or allow it to be `null`. The below example will cause a compiler error:

```typescript
import Toybox.Lang;
import Toybox.System;

// Don't shoot
class Messenger {
    private var _message as String;

    public function shareTheMessage() as Void {
        System.println(_message);
    }
}
```

The reason for the error is that `_message` is declared as a String, but left alone it's initialized as `null`. Module variables either have to be initialized at declaration or allowed to be `null`, while object members can be initialized in the `initialize` function, as well. The following would address the error:

```typescript
import Toybox.Lang;
import Toybox.System;

// Don't shoot
class Messenger {
    private var _message as String;

    public function initialize() {
       // Initialize message
        _message = "";
    }

    public function shareTheMessage() {
        System.println(_message);
    }
}
```

### Types and Inheritance

When extending classes, the type system will use the following rules:

1. If you extend a function from a parent with the same number of arguments but do not add type decoration, the types for the arguments and return value will be transferred verbatim from the parent implementation
2. If you extend a function from a parent with the same number of arguments and add type decoration, you must match the number of arguments and type decoration exactly or the compiler will error

This allows for existing Monkey C code that extends `Toybox` types to take advantage of type checking without having to add any type decoration.

## Application Scope Type Checking

The type checker attempts to validate that any member fetched from a module or class is available in all of the same application scopes as the caller. If the developer is confident their code is application scope safe and the type checker still complains, this check can be disabled for background or glance scopes using the annotations `:typecheck(disableBackgroundCheck)` or `:typecheck(disableGlanceCheck)`, respectively. To disable checks for both background and glance scopes, use the annotation `:typecheck([disableBackgroundCheck, disableGlanceCheck])`.

[<sup>1</sup>](#fnsrc_1) It is understood that this is controversial. First, `as` has a whole new meaning now in the grammar, and using it for module renaming is confusing. Also, renaming modules in Monkey C has made it really difficult to write good shareable example code because everyone renames every module to their own preference. Yes, `Gregorian` is a big word and is annoying to type, but thats what we have auto-complete for.

[<sup>2</sup>](#fnsrc_2) The `method` method that returns `Method` should not be confused with "The Method Method", my upcoming self help book on evaluating self help books.

[<sup>3</sup>](#fnsrc_3) I just met you | and this is crazy | but I'm an Any | so type match? Maybe...
