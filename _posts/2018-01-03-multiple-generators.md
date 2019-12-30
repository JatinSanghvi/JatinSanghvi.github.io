---
title: "LINQ Query Expression with Multiple Generators"
categories: [Language, C#]
tags: [c#, linq]
toc: false
---

Today, I went through the 'LINQ' section in C# 7.0 Pocket Reference. The section contains a sub-section on 'Multiple Generators' that illustrates how the compiler translates the query expression with multiple generators into a call to `SelectMany` LINQ query operator. An example from the book would make things clearer:

```cs
int[] numbers = { 1, 2, 3 };
string[] letters = { "a", "b" };

IEnumerable<string> query =
  from n in numbers
  from l in letters
  select n.ToString() + l;
```

The above statements in effect, set variable `query` to `new[] { "1a", "1b", "2a", "2b", "3a", "3b" }`. The compiler emits below code for the LINQ query expression.

```cs
IEnumerable<string> query =
  numbers.SelectMany(
    n => letters,
    (n, l) => select n.ToString() + l));
```

If in case this is the first time that you are witnessing this particular overload of `SelectMany` operator, it is basically implemented as an extension method that internally contains two `foreach` loops. The outer loop iterates through the sequence on which the extension method is called. The inner loop iterates through the sequence returned by lambda expression that is passed as `SelectMany`'s first argument. `SelectMany` then calls the lambda expression passed as second argument for each element-pair in outer and inner sequences.

Here is how the `SelectMany` method is implemented:

```cs
public static IEnumerable<TResult> SelectMany<TSource, TCollection, TResult>(
  this IEnumerable<TSource> source,
  Func<TSource, IEnumerable<TCollection>> collectionSelector,
  Func<TSource, TCollection, TResult> resultSelector)
{
  foreach (TSource element in source)
  {
    foreach (TCollection subElement in collectionSelector(element))
    {
      yield return resultSelector(element, subElement);
    }
  }
}
```

Back to the compiler emitted code, the first lambda expression (copied to `collectionSelector` delegate instance) basically ignores its input parameter `n` and outputs the same sequence `letters`. Hence, in effect we get a Cartesian product of the two sequences. For sake of clarity, if the `SelectMany` query operator did not exist, below non-generic method implementation would have achieved the same effect.

```cs
foreach (int element in numbers)
{
  foreach (string subElement in letters)
  {
    yield return element.ToString() + subElement;
  }
}
```

I wondered what the compiler translates the query expression into if there are three generators present in the query expression as below. Can the same `SelectMany` overload be called in a manner such that it works seemlessly for three or more generators?

```cs
IEnumerable<string> increasings =
  from a in new[] { 1, 2, 3, 4 }
  from b in new[] { 1, 2, 3, 4 }
  from c in new[] { 1, 2, 3, 4 }
  where a < b && b < c
  select a + " " + b + " " + c;

increasings.ToList().ForEach(Console.WriteLine);

/*
  Result

  1 2 3
  1 2 4
  1 3 4
  2 3 4
*/
```

So, I compiled the program and inspected the assembly with ILSpy. The compiler generated below code (listed in two parts) for the above statements:

## Compiler emitted class `<>c`

```cs
private sealed class <>c
{
  public static readonly LinqTest.<>c <>9 = new LinqTest.<>c();

  public static Func<int, IEnumerable<int>> <>9__0_0;

  public static Func<int, int, <>f__AnonymousType0<int, int>> <>9__0_1;

  public static Func<<>f__AnonymousType0<int, int>, IEnumerable<int>> <>9__0_2;

  public static Func<<>f__AnonymousType0<int, int>, int, <>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>> <>9__0_3;

  public static Func<<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>, bool> <>9__0_4;

  public static Func<<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>, string> <>9__0_5;

  internal IEnumerable<int> <Main>b__0_0(int a)
  {
    return new int[]
    {
      1,
      2,
      3,
      4
    };
  }

  internal <>f__AnonymousType0<int, int> <Main>b__0_1(int a, int b)
  {
    return new
    {
      a,
      b
    };
  }

  internal IEnumerable<int> <Main>b__0_2(<>f__AnonymousType0<int, int> <>h__TransparentIdentifier0)
  {
    return new int[]
    {
      1,
      2,
      3,
      4
    };
  }

  internal <>f__AnonymousType1<<>f__AnonymousType0<int, int>, int> <Main>b__0_3(<>f__AnonymousType0<int, int> <>h__TransparentIdentifier0, int c)
  {
    return new
    {
      <>h__TransparentIdentifier0,
      c
    };
  }

  internal bool <Main>b__0_4(<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int> <>h__TransparentIdentifier1)
  {
    return <>h__TransparentIdentifier1.<>h__TransparentIdentifier0.a < <>h__TransparentIdentifier1.<>h__TransparentIdentifier0.b && <>h__TransparentIdentifier1.<>h__TransparentIdentifier0.b < <>h__TransparentIdentifier1.c;
  }

  internal string <Main>b__0_5(<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int> <>h__TransparentIdentifier1)
  {
    return string.Concat(new object[]
    {
      <>h__TransparentIdentifier1.<>h__TransparentIdentifier0.a,
      " ",
      <>h__TransparentIdentifier1.<>h__TransparentIdentifier0.b,
      " ",
      <>h__TransparentIdentifier1.c
    });
  }
}

```

That seems a bit overwhelming at first sight but if you hold on and look carefully, you can see that the member variables within the class can be grouped into three sets:

1.  Six methods named from `<Main>b__0_0` to `<Main>b__0_5` required while translating the query expression to method calls.
2.  Six `Func` delegate instances named from `<>9__0_0`  to `<>9__0_5` corresponding to each method.
3.  Public static member named `<>9` pointing to the containing class instance.

In our case `a` and `b` are outer generator variables and `c` is inner variable. If outer variables are referenced within the query expression, the compiler needs to ensure that both inner and outer variables are available and hence needs to generate anonymous types that contain all values. That is why we can see two anonymous types in the decompiled code above viz. `<>f__AnonymousType0<int, int>` and `<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>`. To me, it was a revelation to find that generic class types are used to represent anonymous types in the same way how `Func`s and `Action`s are used as delegates for anonymous methods.

## Compiler emitted method body

```cs
IEnumerable<int> expr_07 = new int[]
{
  1,
  2,
  3,
  4
};
Func<int, IEnumerable<int>> arg_50_1;
if ((arg_50_1 = LinqTest.<>c.<>9__0_0) == null)
{
  arg_50_1 = (LinqTest.<>c.<>9__0_0 = new Func<int, IEnumerable<int>>(LinqTest.<>c.<>9.<Main>b__0_0));
}
var arg_50_2;
if ((arg_50_2 = LinqTest.<>c.<>9__0_1) == null)
{
  arg_50_2 = (LinqTest.<>c.<>9__0_1 = new Func<int, int, <>f__AnonymousType0<int, int>>(LinqTest.<>c.<>9.<Main>b__0_1));
}
var arg_93_0 = expr_07.SelectMany(arg_50_1, arg_50_2);
var arg_93_1;
if ((arg_93_1 = LinqTest.<>c.<>9__0_2) == null)
{
  arg_93_1 = (LinqTest.<>c.<>9__0_2 = new Func<<>f__AnonymousType0<int, int>, IEnumerable<int>>(LinqTest.<>c.<>9.<Main>b__0_2));
}
var arg_93_2;
if ((arg_93_2 = LinqTest.<>c.<>9__0_3) == null)
{
  arg_93_2 = (LinqTest.<>c.<>9__0_3 = new Func<<>f__AnonymousType0<int, int>, int, <>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>>(LinqTest.<>c.<>9.<Main>b__0_3));
}
var arg_B7_0 = arg_93_0.SelectMany(arg_93_1, arg_93_2);
var arg_B7_1;
if ((arg_B7_1 = LinqTest.<>c.<>9__0_4) == null)
{
  arg_B7_1 = (LinqTest.<>c.<>9__0_4 = new Func<<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>, bool>(LinqTest.<>c.<>9.<Main>b__0_4));
}
var arg_DB_0 = arg_B7_0.Where(arg_B7_1);
var arg_DB_1;
if ((arg_DB_1 = LinqTest.<>c.<>9__0_5) == null)
{
  arg_DB_1 = (LinqTest.<>c.<>9__0_5 = new Func<<>f__AnonymousType1<<>f__AnonymousType0<int, int>, int>, string>(LinqTest.<>c.<>9.<Main>b__0_5));
}
IEnumerable<string> increasings = arg_DB_0.Select(arg_DB_1);
increasings.ToList<string>().ForEach(new Action<string>(Console.WriteLine));

```

Again, the code may seem difficult to comprehend. Here, we have six local variables that get assigned the six delegate instances defined in class `<>c`. If they turn out to be null, both local and class member variables are assigned the methods defined in the same class. It would help if someone can shed light on why it is required to lazily initialize the class member delegate instances. Nevertheless, I tried to trim away the parts that are not required to understand the translation by removing the null checks and replacing the generic types for anonymous classes to non-generic named types. Here is what the code ended up with afterwards:

```cs
class AB { public int a; public int b; };
class ABC { public AB ab; public int c; };

void Main()
{
  IEnumerable<int> aList = new int[] { 1, 2, 3, 4 };

  IEnumerable<AB> abList = aList.SelectMany(
    a => new int[] { 1, 2, 3, 4 },
    (a, b) => new AB { a = a, b = b });

  IEnumerable<ABC> abcList = abList.SelectMany(
    ab => new int[] { 1, 2, 3, 4 },
    (ab, c) => new ABC { ab = ab, c = c });

  IEnumerable<string> increasings = abcList
    .Where(abc => abc.ab.a < abc.ab.b && abc.ab.b < abc.c)
    .Select(abc => abc.ab.a + " " + abc.ab.b + " " + abc.c);

  increasings.ToList().ForEach(Console.WriteLine);
}

```

So finally, I could understand what the code was trying to achieve. With introduction of each new generator in the LINQ expression, the compiler creates an anonymous class nesting previous anonymous/named type into current one until all the generators are exhausted. The outer the variable is in the list of generators, the deeper it becomes the member of the final anonymous type.

To conclude, I have always preferred fluent query syntax (e.g. `aList.Where(a => a < 10).Select(a => a + 2)`) over query expression (`from a in aList where a < 10 select a + 2`) and have managed to successfully avoid the latter in my projects until date. Still if a requirement similar to above ever arises, the non-query syntax would be far too complicated and error prone and it will need to be dropped in favor of query expression.
