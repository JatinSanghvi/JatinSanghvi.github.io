---
title: C# Throw Expression and Argument Expression
summary: 'C# syntactic sugar series #1.'
---

*C# as a language continues to evolve with new versions released every year. With the introduction of new language features, it can be challenging to stay up to date. This is the first post in a series where I will cover the new syntactic sugar incorporated in the recent versions of C#.*

A common task for every C# developer to ensure that a C# class is initialized with the correct arguments is to add null checks on the class constructor parameters, as shown below:

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

As you can see, it takes six lines of code (to satisfy style checkers) to validate every constructor argument. However, you can replace the above code with a single line using the null-coalescing operator `??` and a throw expression.

```cs
this.firstName = firstName ?? throw new ArgumentNullException(nameof(firstName));
```

C# did not stop there though. You see that you are still required to pass the name of the input argument to `ArgumentNullException` constructor so that the exception message can be set to something like `Value cannot be null. (Parameter 'firstName')` and lets you identify which of the many input arguments was problematic. C# 10 introduced the [`CallerArgumentExpression` attribute](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/attributes/caller-information#argument-expressions), allowing you to write a method, say `EnsureNotNull` to simplify the above line further.

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

The above method definition was simplified to highlight just the essentials of caller argument expression. A more elaborate method that uses extension methods, allows nullable checks and works for any argument type will look like below.

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

If you prefer not to implement your own set of such methods or use a third-party library, there is a straightforward two-liner solution using just the methods available in the C# core library starting from .NET 6.

```cs
ArgumentNullException.ThrowIfNull(firstName);
this.firstName = firstName;
```
