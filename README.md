
# Iteration Sort
Iteration sort is a sorting algorithm based on counting.

To run this application, run `python3 iteration_sort.py`. The interface expects users to input the list of integers they wish to sort in the order they appear in the list. Alternatively, the defined function `iteration_sort(comp, lst)` can be called in code, where `comp` is the comparator for the items of the list (defined as if `x < y`, then `comp(x, y) < 0`, if `x == y`, then `comp(x, y) == 0`, and if `x > y`, then `comp(x, y) > 0`), and `lst` is the list of items to be sorted. The list will be sorted in ascending order.

## Algorithm

Iteration sort starts with an in order list of items, `[0, 1, 2, ... ,n-1]` where `n` is the length of the list. It then iterates it, adding one to this number in base `n`, checking at each stage if the new indices has all of the items of the list in order. If it does, then it halts. 

## Time Complexity

The worst case time complexity is `n^(n + 1)`, trivially achieved by iterating through all possible values. The best case is `n`, achieved by the order lexicographically before the sorted ordering. The average case is `n^(n+1)`, since on average one would have to iterate through half of the possible space to reach the sorted configuration.
