class Solution:
    @staticmethod
    def solve(A):
        toOperate = []
        operators = ["+", "-", "*", "/"]
        for e in A:
            if e not in operators:
                toOperate.append(int(e))
            else:
                opTwo = toOperate.pop()
                opOne = toOperate.pop()
                if e == "+":
                    toOperate.append(opOne + opTwo)
                elif e == "-":
                    toOperate.append(opOne - opTwo)
                elif e == "*":
                    toOperate.append(opOne * opTwo)
                elif e == "/":
                    toOperate.append(opOne // opTwo)
        return toOperate.pop()


if __name__ == '__main__':
    s = Solution
    A = ["4", "13", "5", "/", "+"]
    print(s.solve(A))
