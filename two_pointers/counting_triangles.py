class Solution:
    @staticmethod
    def solve(A):
        n = len(A)
        triForms = 0
        sortA = sorted(A, reverse=True)

        for i in range(n - 2):
            c_idx = i
            a_idx = n - 1
            b_idx = c_idx + 1

            while a_idx > b_idx:
                if sortA[a_idx] + sortA[b_idx] > sortA[c_idx]:
                    triForms += (a_idx - b_idx)
                    b_idx += 1
                else:
                    a_idx -= 1
        return triForms % 1000000007


if __name__ == '__main__':
    s = Solution
    A = [1, 1, 1, 2, 2]
    print(s.solve(A))
