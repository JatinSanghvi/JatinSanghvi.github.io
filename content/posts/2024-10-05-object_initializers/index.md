---
title: C# Object Initializers
summary: C# syntactic sugar series - Part 2.
---

If you've been programming in C# for a while, you're likely familiar with the object initializer syntax that simplifies the process of creating and initializing objects. Consider the following class definition:

```cs
class Person
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```

With this class, you can initialize an object in two ways. The traditional method involves creating an instance and then setting properties individually:

```cs
Person person = new Person();
person.FirstName = "John";
person.LastName = "Doe";
```

However, C# allows for a more concise approach using **object initializers**:

```cs
Person person = new Person
{
    FirstName = "John",
    LastName = "Doe",
};
```

In the example above, initializing the properties `FirstName` and `LastName` is optional. You can instantiate the object with `new Person()` without providing values for these properties, and the compiler will allow it, which is not always desirable. To enforce that a property must be initialized during object creation, you can use the **required modifier** introduced in C# 11:

```cs
public required string FirstName { get; set; }
```
With this definition, attempting to create a `Person` object without setting `FirstName` will result in a compilation error:

```cs
// This will fail.
Person person = new Person { LastName = "Doe" };
```

If you want to ensure that `FirstName` is set during initialization and cannot be changed afterward, you can define the property with the **init accessor**:


```cs
public string FirstName { get; init; }
```

I would recommend this approach as it allows you to create immutable class-objects whose state cannot change after they are constructed.

Immutability is a powerful concept in software design. By defining classes as immutable, you can avoid many common bugs related to state changes, especially in multi-threaded environments. While it may seem restrictive, it often leads to cleaner and more maintainable code. In my experience, I've successfully built sizable server applications and tools with  only immutable classes, and the benefits in terms of reliability and simplicity are significant.

Before the introduction of `init`, a common way to create immutable classes was to use **readonly fields**:

```cs
public readonly string FirstName;
```

This approach necessitates passing the values as constructor arguments, which can result in lengthy constructor signatures when there are many fields to be initialized in the class. Additionally, to avoid modifying the existing method calls with the introduction of new fields, one might resort to creating multiple overloaded constructors with one invoking another. This complicates the code and makes it harder to read and maintain. The init accessor solves majority of these issues. The caller code can now pass the values in any order and does not need to match them with one of the constructor signatures.

In summary, by leveraging object initializers, the required modifier, and the init accessor, you can create robust and maintainable applications. Embracing immutability can lead to cleaner code and fewer issues in concurrent scenarios, making it a best practice worth adopting in your C# programming endeavors.
