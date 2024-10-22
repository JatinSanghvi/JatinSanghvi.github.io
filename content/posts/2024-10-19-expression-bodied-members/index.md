---
title: C# Expression Body Syntax
summary: C# syntactic sugar series - Part 4.
---

<!-- IDE0021, IDE0022, IDE0025, IDE0027 -->

To support SQL-like LINQ query expressions in C# 3.0, several language features were introduced, including lambda expressions, extension methods, and anonymous types. While the query expressions themselves did not become mainstream, the supporting features gained significant popularity. Building on the success of lambda syntax, C# 6.0 introduced expression-bodied members, which were further enhanced in C# 7.0 and C# 8.0 to support all possible class and struct member types.

Consider the following example of a property definition and its replacement using expression-body syntax:

```cs
// Traditional Syntax.
public string Address
{
    get { return this.address; }
    set { this.address = value; }
}

// Expression-Body Syntax.
public string Address
{
    get => this.address;
    set => this.address = value;
}
```

If the `Address` property above does not have a setter, the property definition can be further simplified to:

```cs
public string Address => this.address;
```

Constructors and methods can also utilize the shorthand syntax provided by expression-bodied members:

```cs
// Traditional Syntax.
public Person(string name) // Constructor.
{
    this.Name = name;
}

public string GetName() // Method.
{
    return this.FirstName + " " + this.LastName;
}

// Expression-Body Syntax.
public Person(string name) => this.Name = name; // Constructor.
public string GetName() => this.FirstName + " " + this.LastName; // Method.
```

While the expression-body syntax can make your code more concise, there are some considerations to keep in mind. Unlike lambda functions, which can have multiple statements as in `num => { int digit = (num / 10) % 10; return digit * digit; }`, the expression-bodied members are limited to single expression only, and using expression-body syntax for single-statement methods and the regular one for multi-statement methods will make your code appear incoherent.

Additionally, developers who embrace the functional programming style often view expressions as statements with no side effects. In the above code examples, the getter-only `Address` property and the `GetName` method do not alter the state of containing class, so it may be reasonable to use the expression-body syntax for them. However, for the same reason, a regular method-body syntax will be more preferable for the single-statement `Person` constructor.
