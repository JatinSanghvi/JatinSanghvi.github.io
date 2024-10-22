---
title: C# Inlined Variable Declaration
summary: C# syntactic sugar series - Part 3.
---

Before C# included support for tuples, the traditional approach to returning multiple values from a method was to define `out` method parameters. This method allowed developers to return additional values without creating custom data structures. For example, consider the `TryParse` method in the `Int32` struct:

```cs
public struct Int32
{
    public static bool TryParse(string? s, out int result);
}
```

A typical caller of this method would look like:

```cs
int number;
if (int.TryParse("42", out number))
{
    DoSomething(number);
}
```

C# 7 introduced a shorthand for inlining the `out` variable declarations, simplifying the syntax and improving code readability. Now, you can write:

```cs
if (int.TryParse("42", out int number))
{
    DoSomething(number);
}
```

In the above example, the scope of the variable `number` is same as the scope inside which `TryParse` method is called. This allows you to refer to the `number` outside the if-block as well.

C# also allows you to inline the declarations when using the `is` operator to check for a variable's underlying type. This feature allows you to replace the following code:

```cs
if (obj is int)
{
    int number = (int)obj;
    DoSomething(number);
}
```

with a more concise version:

```cs
if (obj is int number)
{
    DoSomething(number);
}
```

The above support falls under a broader class of syntactic sugars called 'Pattern Matching', introduced in C# 7 and further enhanced in C# 8. Pattern matching allows developers to perform complex type checks and comparisons in a more readable and concise manner. It includes features like type patterns, constant patterns, and positional patterns, which we shall cover piecewise in future posts.
