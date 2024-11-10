---
title: "C# Inlined Variable Declaration"
summary: "C# syntactic sugar series - Part 3."
tags: ["C#", "Syntactic Sugar Series"]
---

<!-- IDE0018, IDE0019, IDE0020 -->

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

C# 7.0 introduced a shorthand for inlining the `out` variable declarations, simplifying the syntax and improving code readability. Now, you can write:

```cs
if (int.TryParse("42", out int number))
{
    DoSomething(number);
}
```

In the above example, the scope of the variable `number` is same as the scope inside which `TryParse` method is called. This allows you to refer to the `number` outside the if-block as well.

Traditionally, to check for the variable's underlying type, one had to use the `as` operator followed by a null-check as in the following code:

```cs
int number = obj as int;
if (number != null)
{
    DoSomething(number);
}
```

C# 7.0 also added support for the `is` operator to check for the variable's type that eliminated the null-check as follows:

```cs
if (obj is int)
{
    int number = (int)obj;
    DoSomething(number);
}
```

By inlining the declaration of variable `number` similar to that for `out` variables, we can further modify the previous code with a more succinct version:

```cs
if (obj is int number)
{
    DoSomething(number);
}
```

The above support falls under a broader class of syntactic sugars called 'Pattern Matching', introduced in C# 7 and further enhanced in C# 8. Pattern matching allows developers to perform complex type checks and comparisons in a more readable and concise manner. It includes features like type patterns, constant patterns, and positional patterns, which we shall cover piecewise in future posts.
