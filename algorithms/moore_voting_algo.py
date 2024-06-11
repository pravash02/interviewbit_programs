## Moore's Voting Algorithm

def majority_elem(A):
    n = len(A)
    count = 0
    major_index = 0

    for i in range(0, n):
        if A[i] == A[major_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            A[major_index] = i
            count += 1

    count = 0
    for i in range(0, n):
        if A[i] == A[major_index]:
            count += 1
        if count > n // 2:
            return 1
        else:
            return 0


print(majority_elem([1, 2, 3, 1, 1]))
