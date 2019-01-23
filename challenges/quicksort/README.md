# Quicksort

Implement Quicksort

## Challenge

Write a function that accepts an array of integers, and returns an array sorted by a recursive quicksort algorithm.

## Approach & Efficiency
Quick sort works by selecting a value in the list and setting it to the pivot point value. The leftmost value is compared to the pivot point and the rightmost value is as well. If the left point is lower than the pivot point the next index is incremented until a left point is found that is greater than the pivot. The right side is reviewed and decremented. When a point is found that is less than the pivot value the current right and left points are swapped. once the right side is less than the left side the right side becomes swapped with the pivot point and the list is split to the left and right of this pivot point
it is rerun recursively on left and right until entire list has been sorted
Time is O(n log n ) and Space complexity is O (1) as the list is modified in place

## Solution

![](../../assets/.jpg)
