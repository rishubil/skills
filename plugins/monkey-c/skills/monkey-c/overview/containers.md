---
title: Containers
source: https://developer.garmin.com/connect-iq/monkey-c/containers/
---

Monkey C has two container types built into the language: Arrays and Dictionaries.

## Arrays

Arrays in Monkey C, like variables, are typeless, it is not necessary to declare a data type. There are two forms for creating a new array. To create an empty array of a fixed `size`, use this:

```typescript
// Create a typeless array
var untypedArray = new [size];
// Create a typed array
var typedArray = new Array<Number>[size];
```

To pre-initialize an array, this syntax can be used:

```typescript
// New array. Will be typed as a Tuple
// [Number, Number, Number, Number, Number]
var untypedArray = [1, 2, 3, 4, 5];
// New typed array
var typedArray = [1, 2, 3, 4, 5] as Array<Number>;
```

Elements are expressions, so multidimensional arrays can be created using this syntax:

```typescript
var array = [ [1,2], [3,4] ];
```

Monkey C does not have a direct way of creating an empty two-dimensional array, one may be initialized with this syntax:

```typescript
// Shout out to all the Java programmers in the house
var array = new [first_dimension_size];

// Initialize the sub-arrays
for( var i = 0; i < first_dimension_size; i += 1 ) {
    array[i] = new [second_dimension_size];
}
```

## Dictionaries

Dictionaries, or associative arrays, are a built-in data structure in Monkey C:

```java
var dict = { "a" => 1, "b" => 2 };  // Creates a dictionary
System.println( dict["a"] );        // Prints "1"
System.println( dict["b"] );        // Prints "2"
System.println( dict["c"] );        // Prints "null"
```

To initialize an empty dictionary, use the following syntax:

```typescript
var x = {};                         // Empty dictionary
```

A type suffix can be added when creating new [Lang.Dictionary](../api-docs/Toybox/Lang/Dictionary.md) objects:

```typescript
var x = {} as Dictionary<Symbol, String>;
// Valid
x[:option] = "value";
// Invalid
x["option"] = "value";
```

By default, objects hash on their reference value. Classes should override the `hashCode()` method in `Toybox.Lang.Object` to change the hashing function for their type:

```java
class Person
{
    // Return a number as the hash code. Remember that the hash code must be
    // the same for two objects that are equal.
    // @return Hash code value
    function hashCode() {
        // Using the unique person id for the hash code
        return mPersonId;
    }
}
```

Dictionaries automatically resize and rehash as the contents grow or shrink. This makes them extremely flexible, but it comes at a cost. Insertion and removal of the contents can cause performance problems if there is accidental or excessive resizing and rehashing. Also, because hash tables require extra space for allocation, they are not as space-efficient as either objects or arrays.
