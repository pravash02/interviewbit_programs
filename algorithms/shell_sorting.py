"""

Shell Sort Algorithm
------------------------

 Step1: First we have to find the gap that the shell where we would be comparing the elements at the
        respective position and do the swapping

 Step2: We basically need to maintain the 3 loops, first for decrementing the gap,
        second for the iterating the gap and third for comparing the elements within that gap.

 Step3: Here we also compare the elements on the previous index within the same gap.
"""


def shell_sort(lst):
    gap = len(lst)//2
    while gap >=1:
        for j in range(gap, len(lst)):
            i = j-gap
            while i >= 0:
                if lst[i+gap] > lst[i]:
                    break
                else:
                    lst[i+gap], lst[i] = lst[i], lst[i+gap]
                i -= gap
        gap = gap//2

    return lst

print(shell_sort([0, 3, 8, 2, 7, 5]))
