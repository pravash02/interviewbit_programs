class Solution:
    @staticmethod
    def solve(A):
        hasht = {}
        ans = []

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] in hasht:
                    final = []
                    final.extend(hasht[A[i] + A[j]])

                    final.append(i)
                    final.append(j)

                    if len(final) == len(set(final)):
                        ans.append(final)
                else:
                    hasht[A[i] + A[j]] = [i, j]
                    # print(hasht)

        ans.sort()
        return ans[0]


if __name__ == '__main__':
    s = Solution
    A = [3, 4, 7, 1, 2, 9, 8]
    print(s.solve(A))
