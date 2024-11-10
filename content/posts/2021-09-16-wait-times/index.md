---
title: "Balancing the Wait Times"
summary: "An arrangement that evenly distributes the waiting times for student in a classroom."
tags: ["Mathematics"]
---

## Background

My younger son studies in an online classroom, and last week was the time for their oral tests. As you might know, written tests are often not reliable indicators of student performance in an online setting, especially when it is India 🙂 The oral tests covered three subjects, each conducted on a separate day. Each day, the teacher would call students one at a time in a specific order to join her online and answer questions.

There were 31 students in the classroom. If the teacher had called the students by their roll numbers - from 1 to 31 - every day, those with higher roll numbers would always have to wait until the evening. To ensure that wait times were more evenly distributed, the teacher informed the parents that she would call students in the following order over the three days:

- **Day 1**: By roll numbers from **1 to 31**.
- **Day 2**: By roll numbers from **31 to 1**.
- **Day 3**: By roll numbers from **16 to 31**, followed by **1 to 15**.

Upon hearing this, my immediate reaction was that this plan does not fully balance the wait times. For instance, the student with roll number 16 would wait for half the time on Days 1 and 2 but would not wait at all on Day 3. Conversely, the student with roll number 15 would experience nearly equal wait times on Days 1 and 2 but would have to wait until the end on Day 3. Thus, the wait times were not fairly distributed, and there might be a better arrangement that could produce a more even distribution of wait times across the three days.

## Comparing Wait Time Distributions

A few days later, when my son's oral tests began, I revisited this issue. Intuitively, I believed that the following arrangement would yield a better outcome than the teacher's original plan:

- **Day 1**: By roll numbers from **1 to 31**.
- **Day 2**: By roll numbers from **11 to 31**, followed by **1 to 10**.
- **Day 3**: By roll numbers from **21 to 31**, followed by **1 to 20**.

It's worth noting that the order for Day 1 can remain consistent, rolling from 1 to 31 regardless of the overall arrangement, without losing generality. For the sake of analysis, let's assume that the first student called on any given day waits for 0 time-units, and this waiting time increases by 1 unit for each subsequent student, culminating in a wait time of 30 units for the last student of that day.

With the teacher's arrangement,

- Student with roll number **16** waits for (15 + 15 + 0) = **30** units.
- Student with roll number **17** waits for (16 + 14 + 1) = **31** units.
- Student with roll number **18** waits for (17 + 13 + 2) = **32** units.
- ...
- ...
- Student with roll number **13** waits for (12 + 18 + 28) = **58** units.
- Student with roll number **14** waits for (13 + 17 + 29) = **59** units.
- Student with roll number **15** waits for (14 + 16 + 30) = **60** units.

Here's how the wait times appear for each student:

<!-- Referenced https://www.chartjs.org/docs/latest/charts/bar.html -->

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: 'rgba(255, 99, 132)',
    },
    {
      label: 'Day 2',
      data: [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
      backgroundColor: 'rgba(255, 159, 64)',
    },
    {
      label: 'Day 3',
      data: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      backgroundColor: 'rgba(75, 192, 192)',
    },
  ],
},
options: {
  barPercentage: 1.8,
  borderWidth: 4,
  borderColor: 'rgba(0, 0, 0, 0)',
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      max: 60,
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    },
  },
}
{{< /chart >}}

In contrast, with the new arrangement I proposed,

- Student with roll number **21** waits for (20 + 10 + 0) = **30** units.
- Student with roll number **11** waits for (10 + 0 + 21) = **31** units.
- Student with roll number **1** waits for (0 + 21 + 11) = **32** units.
- Student with roll number **22** waits for (21 + 11 + 1) = **33** units.
- ...
- ...
- Student with roll number **30** waits for (29 + 19 + 9) = **57** units.
- Student with roll number **20** waits for (19 + 9 + 30) = **58** units.
- Student with roll number **10** waits for (9 + 30 + 20) = **59** units.
- Student with roll number **31** waits for (30 + 20 + 10) = **60** units.

Here's how the new wait times look:

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: 'rgba(255, 99, 132)',
    },
    {
      label: 'Day 2',
      data: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      backgroundColor: 'rgba(255, 159, 64)',
    },
    {
      label: 'Day 3',
      data: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      backgroundColor: 'rgba(75, 192, 192)',
    },
  ],
},
options: {
  barPercentage: 1.8,
  borderWidth: 4,
  borderColor: 'rgba(0, 0, 0, 0)',
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      max: 60,
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    },
  },
}
{{< /chart >}}

Ultimately, the new arrangement did not prove to be better or worse than the teacher's plan; it merely redistributed the wait times among a different permutation of students.

After some more scribbling on paper, I finally discovered an optimal arrangement. Take a look at the table below, which illustrates how the first and second halves of the roll numbers are interleaved on Day 3.

| Day 1 Sequence | Day 2 Sequence | Day 3 Sequence |
|---------------:|---------------:|---------------:|
| 1              | 17             | 16             |
| 2              | 18             | 31             |
| 3              | 19             | 15             |
| 4              | 20             | 30             |
| 5              | 21             | 14             |
| 6              | 22             | 29             |
| ...            | ...            | ...            |
| 14             | 30             | 25             |
| 15             | 31             | 9              |
| 16             | 1              | 24             |
| 17             | 2              | 8              |
| ...            | ...            | ...            |
| 30             | 15             | 17             |
| 31             | 16             | 1              |

To demonstrate that this arrangement is effective, here's another table, this time ordered by roll numbers. Pay close attention to the differences in per-day wait times for successive students; this will give you a clearer understanding of how the arrangement achieves balanced wait times.

| Roll Number | Day 1 Wait Time | Day 2 Wait Time | Day 3 Wait Time | Total Wait Time |
|------------:|----------------:|----------------:|----------------:|----------------:|
| **1**       | 0               | 15              | 30              | 45              |
| **2**       | 1               | 16              | 28              | 45              |
| **3**       | 2               | 17              | 26              | 45              |
| **4**       | 3               | 18              | 24              | 45              |
| **5**       | 4               | 19              | 22              | 45              |
| **6**       | 5               | 20              | 20              | 45              |
| **...**     | ...             | ...             | ...             | ...             |
| **14**      | 13              | 28              | 4               | 45              |
| **15**      | 14              | 29              | 2               | 45              |
| **16**      | 15              | 30              | 0               | 45              |
| **17**      | 16              | 0               | 29              | 45              |
| **...**     | ...             | ...             | ...             | ...             |
| **30**      | 29              | 13              | 3               | 45              |
| **31**      | 30              | 14              | 1               | 45              |

If the above table doesn't clarify things, here's a chart to help visualize the distribution of wait times.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: 'rgba(255, 99, 132)',
    },
    {
      label: 'Day 2',
      data: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
      backgroundColor: 'rgba(255, 159, 64)',
    },
    {
      label: 'Day 3',
      data: [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],
      backgroundColor: 'rgba(75, 192, 192)',
    },
  ],
},
options: {
  barPercentage: 1.8,
  borderWidth: 4,
  borderColor: 'rgba(0, 0, 0, 0)',
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      max: 60,
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    },
  },
}
{{< /chart >}}

I also discovered a couple of other arrangements that provided balanced wait times. However, upon further inspection, it turned out that all of these could be derived by either shuffling the three days or rearranging the roll numbers. Essentially, there were no unique arrangements that could not be constructed by simply reordering the optimal arrangement mentioned above.

## Generalizing the Solution

### For an Arbitrary Number of Days

The challenge of arranging students arises only when the number of days is odd. If there were an even number of days, we could simply arrange students from start to end on every odd day and from end to start on the even days. Naturally, balancing wait times would be impossible with just a single day. However, for any odd number of days greater than one, we could start by arranging the students from start to end on every odd day, followed by end to start on the even days, continuing the pattern until we reach three days, at which point we could apply the same arrangement as described earlier.

### For an Arbitrary Number of Students

Now, let's consider the scenario where we have three days and an even number of students. Can we balance wait times for all students? Sadly, this is not possible and here is a brief explanation to convince you. Let's denote the number of students as **S**. The wait times for students on a given day will progressively increase from **0** to **S-1**, averaging at **(S-1)/2**. Consequently, the three-day average would be **3(S-1)/2**. If we assume there exists an arrangement that produces the same wait time for all students after three days, then the total wait time for each student would be equal the average wait time, which is **3(S-1)/2**. This expression does not produce a whole number if **S** is even.

But let's not lose hope. We can still achieve a near-balanced solution for an even number of students. We can create an arrangement where the total wait time is a whole number that is **0.5** above the value of **3(S-1)/2** for half of the students and is **0.5** below that value for the other half. The following table illustrates one such possible sequence for **6** students.

| Day 1 Sequence | Day 2 Sequence | Day 3 Sequence |
|---------------:|---------------:|---------------:|
| 1              | 4              | 3              |
| 2              | 5              | 6              |
| 3              | 6              | 2              |
| 4              | 1              | 5              |
| 5              | 2              | 1              |
| 6              | 3              | 4              |

And now the wait times ordered by the roll numbers.

| Roll Number | Day 1 Wait Time | Day 2 Wait Time | Day 3 Wait Time | Total Wait Time |
|------------:|----------------:|----------------:|----------------:|----------------:|
| **1**       | 0               | 3               | 4               | 7               |
| **2**       | 1               | 4               | 2               | 7               |
| **3**       | 2               | 5               | 0               | 7               |
| **4**       | 3               | 0               | 5               | 8               |
| **5**       | 4               | 1               | 3               | 8               |
| **6**       | 5               | 2               | 1               | 8               |

Finally, for the sake of completeness, here's a chart to visualize the above table.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5],
      backgroundColor: 'rgba(255, 99, 132)',
    },
    {
      label: 'Day 2',
      data: [3, 4, 5, 0, 1, 2],
      backgroundColor: 'rgba(255, 159, 64)',
    },
    {
      label: 'Day 3',
      data: [4, 2, 0, 5, 3, 1],
      backgroundColor: 'rgba(75, 192, 192)',
    },
  ],
},
options: {
  aspectRatio: 5,
  barPercentage: 1.8,
  borderWidth: 4,
  borderColor: 'rgba(0, 0, 0, 0)',
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      max: 10,
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    },
  },
}
{{< /chart >}}

In summary, the problem turned out to be far more challenging than I had anticipated. I realized that I could neither expect the teacher to find the solution nor the parents to remember the order if it were shared for their child. However, I made a couple of discoveries along the way, and I'm glad I spent time in tackling it.
