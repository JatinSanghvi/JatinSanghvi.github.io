---
title: C# Throw Expression and Argument Expression
summary: 'C# syntactic sugar series - Part 1.'
---

*C# as a language continues to evolve with new versions released every year. With the introduction of new language features, it can be challenging to stay up to date. This is the first post in a series where I will cover the new syntactic sugars incorporated in the recent versions of C#.*

A common task for C# developers is ensuring that classes are initialized with valid arguments. This often involves adding null checks in the class constructor, as illustrated below:

```cs
public Person(string firstName)
{
    if (firstName is null)
    {
        throw new ArgumentNullException(nameof(firstName));
    }

    this.firstName = firstName;
}
```

As you can see, it takes several lines of code to validate constructor parameters, which can be cumbersome. However, you can simply the validation code by using the null-coalescing operator `??` combined with a *throw expression*:

```cs
this.firstName = firstName ?? throw new ArgumentNullException(nameof(firstName));
```

While this reduces the code significantly, you still need to specify the parameter name for the `ArgumentNullException`, which helps in identifying the problematic argument from the exception message, such as `Value cannot be null. (Parameter 'firstName')`.

The introduction of [`CallerArgumentExpression` attribute](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/attributes/caller-information#argument-expressions) in C# 10 allows for even more concise code. You can create a method like `EnsureNotNull` to simplify the null-check further:

```cs
public string EnsureNotNull(
    string argument,
    [CallerArgumentExpression(nameof(argument))] string paramName = null)
{
    ArgumentNullException.ThrowIfNull(argument, paramName);
    return argument;
}

this.firstName = this.EnsureNotNull(firstName);
```

This method highlights the essentials of caller argument expressions. A real-world solution will possibly implement an extension method that accommodates nullable checks and works with any argument type:

```cs
public static class EnsureExtensions
{
    public static T EnsureNotNull<T>(
        [NotNull] this T? argument,
        [CallerArgumentExpression(nameof(argument))] string? paramName = null)
    {
        ArgumentNullException.ThrowIfNull(argument, paramName);
        return argument;
    }
}

this.firstName = firstName.EnsureNotNull();
```

If you prefer not to create custom methods or rely on third-party libraries, a straightforward two-liner solution is available using methods from the C# core library starting with .NET 6:

```cs
ArgumentNullException.ThrowIfNull(firstName);
this.firstName = firstName;
```

This approach not only simplifies your code but also enhances readability and maintainability, aligning with modern C# practices.
