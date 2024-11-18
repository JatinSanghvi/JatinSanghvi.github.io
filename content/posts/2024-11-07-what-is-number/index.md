---
title: "What is a Number?"
summary: "How my perception of innocent-looking numbers evolved over time."
tags: ["Mathematics"]
---

{{< katex >}}

When I first entered school, I viewed numbers as mere collections of digits—nothing more. Take, for instance, the number:

$$ 42 $$

However, my perspective got quickly changed when I first learned about the **negative numbers**. Many of us as children must have once stumbled upon a subtraction like \\(3 - 5\\) and imagined what its result should be. Unlike fractions and percentages, we haven't adopted negative numbers in our everyday conversation. If someone asks, "How much older are you than your friend?" then responding with "Negative six months" would sound odd. A more acceptable reply would be, "I'm actually six months younger."

Negative numbers revealed that positive values were just one side of the coin. To denote a negative number, we place a minus sign (\\(−\\)) in front of the value. For positive numbers, we can can use the plus sign (\\(+\\)) to be specific, but we often omit it, treating the unsigned numbers as positive by default.

$$ +42 $$

Next, I was introduced to **fractions**, which expanded my horizon beyond whole numbers. It made me realize the importance of having a system that deals with partial values. A fraction like \\( \frac{3}{5} \\) signifies three parts of "one-fifth." In this sense, every whole number is also a fraction with denominator \\(1\\).

$$ \frac{42}{1} $$

Soon after, I discovered **decimal numbers**. This let me view finite numbers as an infinite sequence of digits, with zeros extending in both directions. We use the decimal point (\\(.\\)) to fixate decimal numbers and the place value of digits are determined by their positions relative to this point.

Decimal point plays a crucial role when perfoming hand-calculations on paper. Whether it's addition, subtraction, multiplication, division or finding square-root using long-division method, we always vertically align the initial, intermediate and resultant terms using their decimal points as reference.

For the sake of brevity, we typically trim leading and trailing zeros, allowing us to express \\(0042.4200\\) simply as \\(42.42\\). We follow a couple of rules here: if all digits before the decimal are zero, we keep the last one, turning \\(0000.42\\) into \\(0.42\\). If all digits after the decimal are zero, we discard them along with the decimal point, so \\(42.0000\\) becomes \\(42\\).

$$ ...00042.000... $$

In high school, I encountered **scientific notation** for expressing very large or small numbers. The first example that struck me was Avogadro's number: \\(6.022 \times 10^{23}\\), which is roughly the number of atoms present in one gram of hydrogen. Scientific notation simplifies calculations, especially in scientific formulas involving multiplication and division. For instance, \\((a_1 \times 10^{b_1}) \times (a_2 \times 10^{b_2})\\) simplifies to \\(a_1 \times a_2 \times 10^{b_1 + b_2}\\), which is less error-prone than multiplying their decimal representations and ensuring that decimal point is correctly placed in the result.

$$ 4.2 \times 10^{1} $$

After tenth grade, my parents enrolled me in computer classes to familiarize me with technology. It was the year 1998, and MS-DOS and Windows 95 were the primary operating systems. Next to my classroom, there were advanced computer classes held for people older than me. One day, when all classes were over and after doing an overtime on the game of Solitaire, I passed by the advanced classroom. I noticed a table drawn on the blackboard listing numbers from 0 to 15 on one side and figures 0000 to 1111 on the other. It made no sense at first, so I kept staring until I could draw the pattern out of zeros and ones, and there I had the first mind-blown experience in my life.

It never crossed my mind that the ten symbols we use for numbers are merely a choice, not a mathematical necessity. We could just as easily use a different number of symbols, or in other words, a different **base system** and all the arithmetic methods we developed had remain unchanged. To denote a number with its base, we write it in parentheses with the base as a subscript, like \\((52)_8\\). If the base is not specified, it is assumed to be 10, which is the most common base system.

$$ (42)_{10} $$

My first year of engineering introduced me to **complex numbers**, which consist of a real part and an imaginary part. These numbers are essential in fields like engineering and physics. They often appear in intermediate calculations and we typically pick the real component in the final result. In these contexts, we treat all real numbers as complex numbers with an imaginary part of zero.

$$ 42 + 0i $$

Finally, while studying **matrices**, I realized I had only been working with single values until then, whereas matrices lets us represent multitude of values. In fact, any number can be viewed as a 1x1 matrix, and all matrix operations—such as addition, multiplication, finding determinants, or inverses—yield expected results.

$$ \begin{bmatrix} 42 \end{bmatrix} $$

And so concludes my journey through the world of numbers—unless I've overlooked something. I could have touched on **exponents** (\\(42^1\\)) or **derivatives** (\\(d^042/dx^0\\)), but I feel they don't quite fit here. Thank you for reading!
