class Solution:
    @staticmethod
    def merge_ovrlp(A):
        new_interval = []
        i = 0
        A.sort(key=lambda x: x[0])
        new_interval.append(A[0])

        while i < len(A) - 1:
            if new_interval[i - 1][-1] == A[i + 1][0]:
                new_interval[i - 1][-1] = A[i + 1][-1]

            elif new_interval[i - 1][-1] > A[i + 1][0]:
                new_interval[i - 1][-1] = A[i + 1][-1]

            else:
                new_interval.append(A[i + 1])

            i += 1
        return new_interval


if __name__ == '__main__':
    s = Solution
    lst = [[1, 3], [2, 4], [5, 7], [6, 8]]
    lst2 = [[1, 3], [3, 5], [4, 6]]
    lst3 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(s.merge_ovrlp(lst2))
