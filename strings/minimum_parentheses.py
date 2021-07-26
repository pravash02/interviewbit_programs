class Solution:
    @staticmethod
    def min_parenetheses(A):
        stack = []
        for i in range(len(A)):
            if A[i] == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(A[i])
        return len(stack)


if __name__ == '__main__':
    s = Solution
    M = "())"
    print(s.min_parenetheses(M))
