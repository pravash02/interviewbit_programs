class Solution:
    @staticmethod
    def solve(A):
        if len(A) % 2 != 0:
            return 0

        stack = []
        for i in A:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack:
                    stack.pop()

        if A[0] == ')':
            return 0

        if stack:
            return 0
        else:
            return 1


if __name__ == '__main__':
    s = Solution
    A = '()'
    print(s.solve(A))
