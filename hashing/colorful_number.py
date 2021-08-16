class Solution:
    @staticmethod
    def solve(A):
        A = list(str(A))
        products = set()
        for i in range(len(A)):
            p = 1
            for j in range(i, len(A)):
                p *= int(A[j])
                if p not in products:
                    products.add(p)
                else:
                    return 0
        return 1


if __name__ == '__main__':
    s = Solution
    A = 23
    print(s.solve(A))
