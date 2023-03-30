---
title: Balancing the Wait Times
summary: An arrangement that evenly distributes the waiting times for student in a classroom.
---

## Background

So, my younger son studies in an online classroom. It was the time for their oral tests last week. Well, you know that the written tests are not good indicators of student performance in an online situation, and that too when you are in India :) The oral tests covered three subjects, each to be carried out on a separate day. Each day, the teacher would call students, one at a time in some order, to join her online and answer the questions.

Now, there were 31 students in the classroom. Had the teacher called the students by their roll numbers i.e., from 1 to 31 every day, the students with higher roll numbers had to always wait until the evening. Therefore, in order to ensure that the wait times are more evenly distributed, the teacher informed the parents that she will call students in the following order on each of the three days:

- **Day 1**: By roll numbers from **1 to 31**.
- **Day 2**: By roll numbers from **31 to 1**.
- **Day 3**: By roll numbers from **16 to 31** and then from **1 to 15**.

On hearing this, my immediate reaction was that this plan does not entirely balance the wait times. With this layout, the student with number 16 will wait for half the time on day 1 and 2 but will not wait at all on day 3. On the other hand, the student with number 15 will (almost) equally wait for half the time on day 1 and 2 but will need to wait until the end on day 3. Hence, the wait times were not fairly distributed, and there could be a better arrangement that had produced an even distribution of wait times after summing over the three days.

## Comparing Wait Time Distributions

A few days later, when the oral tests for my son begun, I thought about this problem again. Intuitively, I believed that the following arrangement should have yielded a better outcome than the teacher's arrangement:

- **Day 1**: By roll numbers from **1 to 31**.
- **Day 2**: By roll numbers from **11 to 31** and then from **1 to 10**.
- **Day 3**: By roll numbers from **21 to 31** and then from **1 to 20**.

By the way, the day 1 ordering can always stay the same i.e., from 1 to 31 irrespective of the arrangement without any loss in generality. Now, let's say that the first student to be called on a given day does not wait at all, or in other words, waits for 0 time-units, and this waiting time increases by 1 unit for each successive student, reaching a duration of 30 units for the last student of that day.

With the teacher's arrangement,

- Student with roll number **16** waits for (15 + 15 + 0) = **30** units.
- Student with roll number **17** waits for (16 + 14 + 1) = **31** units.
- Student with roll number **18** waits for (17 + 13 + 2) = **32** units.
- ...
- ...
- Student with roll number **13** waits for (12 + 18 + 28) = **58** units.
- Student with roll number **14** waits for (13 + 17 + 29) = **59** units.
- Student with roll number **15** waits for (14 + 16 + 30) = **60** units.

Here is how the wait times will look like for each student.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: '#6D28D9',
      borderWidth: 0,
    },
    {
      label: 'Day 2',
      data: [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
      backgroundColor: '#8B5CF6',
      borderWidth: 0,
    },
    {
      label: 'Day 3',
      data: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      backgroundColor: '#C4B5FD',
      borderWidth: 0,
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
      max: 60,
      stacked: true,
    }
  }
}
{{< /chart >}}

With the new arrangement that I mentioned above,

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

Here is how the new wait times will look like.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: '#6D28D9',
      borderWidth: 0,
    },
    {
      label: 'Day 2',
      data: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      backgroundColor: '#8B5CF6',
      borderWidth: 0,
    },
    {
      label: 'Day 3',
      data: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      backgroundColor: '#C4B5FD',
      borderWidth: 0,
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

The new arrangement did not turn out to be either better or worse that the teacher's arrangement. It just managed to redistribute the wait times among a different permutation of students.

After some more scribbling on paper, I could finally discover an optimal arrangement. Check out the table below. Notice how the first half and second half of roll numbers are interleaved on day 3.

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

To prove that the above arrangement works, here is another table, this time ordered by roll numbers. Take a close look at the differences in per-day wait times of successive students to get a sense of how the above arrangement delivers balanced wait times.

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

If the above table does not help, here is the chart to help visualize the wait-time distribution.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      backgroundColor: '#6D28D9',
      borderWidth: 0,
    },
    {
      label: 'Day 2',
      data: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
      backgroundColor: '#8B5CF6',
      borderWidth: 0,
    },
    {
      label: 'Day 3',
      data: [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],
      backgroundColor: '#C4B5FD',
      borderWidth: 0,
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
    }
  }
}
{{< /chart >}}

I could find a couple of other arrangements that also delivered balanced wait times. However, on inspecting further, it turned out that all of them could be obtained by either shuffling the three days or the roll numbers. In effect, there were no arrangements that were unique in the sense that they could not be constructed by simply reordering the above arrangement.

## Generalizing the Solution

### For Arbitrary Number of Days

The challenge to arrange the students arises only if the number of days is odd. Had there been an even number of days, we could have simply arranged students from start to end on every odd day and from end to start on the even days. Naturally, we would have failed in balancing the wait times if there were a single day. But for other number of odd days, we could begin by arranging the students from start to end on every odd day and then from end to start on the even day until we were left with 3 days, and then we could use the same arrangement as described above for the final 3 days.

### For Arbitrary Number of Students

Now, consider what happens if we have three days and an even number of students. Would we be able to balance wait times for all students? Sadly, this is not possible and here is a small proof. Let's say that there are **S** students. The wait times for students on a given day will progressively increase from **0** to **S-1**, averaging at **(S-1)/2**. The three-day average would be **3(S-1)/2** Hence, if we assume that there is an arrangement that produces the same wait time for all students after three days, then the value of total wait time for each student would be same as the average wait time i.e., **3(S-1)/2**. This expression does not produce a whole number if **S** is an even number.

But let's not lose hope. We can still reach a near-balanced solution for students with even count. We can have a solution where the total wait time is a whole number that is **0.5** above the value of **3(S-1)/2** for one half of the students and is **0.5** below that value for the other half of student. The following table shows one such possible sequence for **6** students.

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

And for the sake of completeness, a chart for visualizing the above table.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6'],
  datasets: [
    {
      label: 'Day 1',
      data: [0, 1, 2, 3, 4, 5],
      backgroundColor: '#6D28D9',
      borderWidth: 0,
    },
    {
      label: 'Day 2',
      data: [3, 4, 5, 0, 1, 2],
      backgroundColor: '#8B5CF6',
      borderWidth: 0,
    },
    {
      label: 'Day 3',
      data: [4, 2, 0, 5, 3, 1],
      backgroundColor: '#C4B5FD',
      borderWidth: 0,
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
