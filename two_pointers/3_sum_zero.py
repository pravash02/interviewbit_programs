class Solution:
    @staticmethod
    def solve(A):
        A = sorted(A)
        n = len(A)
        lst_s = set({})

        for i in range(len(A) - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = A[i] + A[k] + A[j]

                if s == 0:
                    l = [A[i], A[k], A[j]]
                    l.sort()
                    lst_s.add(tuple(l))

                if s <= 0:
                    j += 1
                else:
                    k -= 1

        return list(lst_s)


if __name__ == '__main__':
    s = Solution
    A = [-1, 0, 1, 2, -1, -4]
    print(s.solve(A))
