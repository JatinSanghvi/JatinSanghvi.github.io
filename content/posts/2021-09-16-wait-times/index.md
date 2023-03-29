---
title: Balancing the Wait Times
summary: An arrangement that ensures every student in a classroom waits an equal amount of time.
---

## Background

So, my younger son studies in an online classroom and it was the time for their oral tests last week. Well, you know that the written tests, when taken online, are not a good measure for assessing student performance for an obvious reason :smile:. The oral tests covered three subjects, each on a separate day. Each day, the teacher would ask students, one at a time, to be online with her and answer all questions.

There were 31 students in the classroom. Had the teacher called the students by their roll numbers (from 1 to 31) every day, the students with higher roll numbers had to always wait for the longest. So, to ensure that the wait times are distributed evenly, the teacher informed all parents that she will call students in the following order on each day:

- **Day 1** - By roll numbers from **1 to 31**.
- **Day 2** - By roll numbers from **31 to 1**.
- **Day 3** - By roll numbers from **16 to 31** and then from **1 to 15**.

On hearing this, my immediate reaction was that this does not balance the waiting times evenly. With this setup, the student with number 16 waits for half the time on days 1 and 2 but does not wait at all on day 3. On other hand, the student with number 15 waits almost half the time on days 1 and 2 but waits full time on day 3. So, there is discrepancy, and we could have set it up in a way such that the wait times were evenly distributed (after tallying across three days) across all students.

## Comparing Student Arrangements

A few days later, when the oral tests for my son begun, I thought about this problem again. Intuitively, I believed that the following arrangement should yield a better outcome than the arrangement made by the teacher:

- **Day 1** - By roll numbers from **1 to 31**.
- **Day 2** - By roll numbers from **11 to 31** and then from **1 to 10**.
- **Day 3** - By roll numbers from **21 to 31** and then from **1 to 20**.

By the way, the day 1 ordering can stay the same (from 1 to 31) without loss in generality. Now, let's say that the first student to be called does not wait at all, or in other words, waits for 0 time-units, and the wait time increases by 1 unit for each successive student, reaching 30 for the last student who gets called.

### Teacher's Arrangement

With the teacher's arrangement,

- Student with roll number **16** waits for (15 + 15 + 0) = **30** units.
- Student with roll number **17** waits for (16 + 14 + 1) = **31** units.
- Student with roll number **18** waits for (17 + 13 + 2) = **32** units.
- ...
- ...
- Student with roll number **13** waits for (12 + 18 + 28) = **59** units.
- Student with roll number **14** waits for (13 + 17 + 29) = **59** units.
- Student with roll number **15** waits for (14 + 16 + 30) = **60** units.

Here are how the wait-times will look like for each student.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: 'rgba(153, 102, 255, 0.2)',
      borderColor: 'rgba(153, 102, 255)',
    },
    {
      label: 'Day 2',
      data: [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235)',
    },
    {
      label: 'Day 3',
      data: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192)',
    },
  ]
},
options: {
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    }
  }
}
{{< /chart >}}

### New Arrangement

And with the new arrangement,

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

Here are how the new wait times will be distributed.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: 'rgba(153, 102, 255, 0.2)',
      borderColor: 'rgba(153, 102, 255)',
    },
    {
      label: 'Day 2',
      data: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235)',
    },
    {
      label: 'Day 3',
      data: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192)',
    },
  ]
},
options: {
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    }
  }
}
{{< /chart >}}

The new arrangement was neither better or worse that the teacher's arrangement. It only managed to redistribute the wait times from 30 time-units to 60 time-units among a different permutation of students.

### Optimal Arrangement

After some more scribbling on paper, I could finally come up with the optimal arrangement. Check the table below. Notice how the first-half and second-half of roll numbers are interleaved on day 3.

| Day 1 Sequence | Day 2 Sequence | Day 3 Sequence |
|---------------:|---------------:|---------------:|
| 1              | 16             | 31             |
| 2              | 17             | 15             |
| 3              | 18             | 30             |
| 4              | 19             | 14             |
| 5              | 20             | 29             |
| 6              | 21             | 13             |
| 7              | 22             | 28             |
| ...            | ...            | ...            |
| 14             | 29             | 9              |
| 15             | 30             | 24             |
| 16             | 31             | 8              |
| 17             | 1              | 23             |
| 18             | 2              | 7              |
| ...            | ...            | ...            |
| 29             | 13             | 17             |
| 30             | 14             | 1              |
| 31             | 15             | 16             |

To prove that the above arrangement works, here is another table, this time ordered by roll numbers. Take a close look at the differences in per-day wait times of successive students to get a sense of how the above arrangement delivers balanced wait times.

| Roll Number | Day 1 Wait Time | Day 2 Wait Time | Day 3 Wait Time | Total Wait Time |
|------------:|----------------:|----------------:|----------------:|----------------:|
| **1**       | 0               | 16              | 29              | 45              |
| **2**       | 1               | 17              | 27              | 45              |
| **3**       | 2               | 18              | 25              | 45              |
| **4**       | 3               | 19              | 23              | 45              |
| **5**       | 4               | 20              | 21              | 45              |
| **6**       | 5               | 21              | 19              | 45              |
| **7**       | 6               | 22              | 17              | 45              |
| **...**     | ...             | ...             | ...             | ...             |
| **14**      | 13              | 29              | 3               | 45              |
| **15**      | 14              | 30              | 1               | 45              |
| **16**      | 15              | 0               | 30              | 45              |
| **17**      | 16              | 1               | 28              | 45              |
| **18**      | 17              | 2               | 26              | 45              |
| **...**     | ...             | ...             | ...             | ...             |
| **29**      | 28              | 13              | 4               | 45              |
| **30**      | 29              | 14              | 2               | 45              |
| **31**      | 30              | 15              | 0               | 45              |

And if the table does not help, here is the chart to help visualize the wait-time distribution.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: 'rgba(153, 102, 255, 0.2)',
      borderColor: 'rgba(153, 102, 255)',
    },
    {
      label: 'Day 2',
      data: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235)',
    },
    {
      label: 'Day 3',
      data: [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0],
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192)',
    },
  ]
},
options: {
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    }
  }
}
{{< /chart >}}

## Generalizing the Solution

### For Arbitrary Number of Days

The challenge to arrange the students arises only if the number of days is odd. Had there been an even number of days, we could have simply arranged students from start to end on the odd days and from end to start on the even days. Naturally, we would have failed in balancing the wait times if there were a single day. But for other odd numbers of days, we would have arranged the students from start to end on each odd day and then from end to start on each even day, until we were down to 3 days remaining at which point, we could use the same arrangement as described above for the final 3 days.

### For Arbitrary Number of Students

Now, consider what happens if we have three days and an even number of students. Would we be able to get the same wait times for all students if summed across the three days? The answer is a 'no'. Let's say, there are **S** students. The wait times everyday varies from **0** to **S - 1** averaging at **(S - 1) / 2**. Hence, if all students had the same total wait times after the three days, every student would have a total wait time of **3 x (S - 1) / 2** which can be a whole number only if **S**, the number of students is odd.

But we can still reach a near-balanced solution for students with even count. We can have a solution where the total wait time for each student is just **0.5** above or below the value **3 x (S - 1) / 2**. The following table shows one such possible sequence for **6** students.

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

And the chart for visualizing the above table.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5],
      backgroundColor: 'rgba(153, 102, 255, 0.2)',
      borderColor: 'rgba(153, 102, 255)',
    },
    {
      label: 'Day 2',
      data: [3, 4, 5, 0, 1, 2],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235)',
    },
    {
      label: 'Day 3',
      data: [4, 2, 0, 5, 3, 1],
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192)',
    },
  ]
},
options: {
  indexAxis: 'y',
  scales: {
    x: {
      title: {
        display: true,
        text: 'Total Wait Times',
      },
      stacked: true,
    },
    y: {
      display: true,
      title: {
        display: true,
        text: 'Roll Numbers',
      },
      stacked: true,
    }
  }
}
{{< /chart >}}
