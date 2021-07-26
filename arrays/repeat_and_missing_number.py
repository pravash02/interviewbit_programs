class Solution:
    @staticmethod
    def repeat_miss_nbr(A):
        d = {}
        count = 0
        x = y = -1

        for i in range(1, len(A)+1):
            d[i] = count

        for i in range(0, len(A)):
            if A[i] in d:
                d[A[i]] = d[A[i]] + 1
            else:
                d[A[i]] = count

        for i, j in d.items():
            if d[i] > 1:
                x = i
            if d[i] == 0:
                y = i

        return x, y

    @staticmethod
    def repeat_miss_nbrB(A):
        n = len(A)
        return [sum(A) - sum(set(A)), int((n * (n + 1)) / 2 - sum(set(A)))]


if __name__ == '__main__':
    s = Solution
    lst = [3, 1, 2, 5, 3]
    print(s.repeat_miss_nbr(lst))
