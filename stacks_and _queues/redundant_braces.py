class Solution:
    @staticmethod
    def solve(A):
        stack = []
        ops = ['+', '*', '/', '-']

        for i in A:
            if i == '(':
                stack.append(i)
            if i in ops and stack:
                stack.pop()

        if not stack:
            return 0
        else:
            return 1

    @staticmethod
    def solveB(expr):
        stack = []  # brackets' stack
        operators = {"+", "-", "*", "/"}
        for char in expr:
            if char == "(":  # push current bracket to the stack
                stack.append(False)  # since we don't know yet if there's an operator
            elif char in operators:
                if not stack:  # no brackets on the stack, just skip it
                    continue
                stack[-1] = True  # found an operator, so last brackets on the stack are valid
            elif char == ")":
                if stack[-1]:  # if the last brackets are valid
                    stack.pop()  # take them off the stack
                else:  # last brackets didn't have an operator inside
                    return 1
        return 0


if __name__ == '__main__':
    s = Solution
    A = "(a + (a + b))"
    print(s.solve(A))
    print(s.solveB(A))
