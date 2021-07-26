class Solution:
    @staticmethod
    def pretty_json(A):
        prettier = []
        indentNum = 0
        temp = ""
        for i in A:
            if i == " ":
                continue
            temp += i
            if i == '[' or i == '{':
                if temp != i:
                    prettier.append("\t" * indentNum + temp[:-1])
                    temp = i
                prettier.append("\t" * indentNum + temp)
                indentNum += 1
                temp = ""
            elif i == ',':
                prettier.append("\t" * indentNum + temp)
                temp = ""
            elif i == ']' or i == '}':
                if temp != i:
                    prettier.append("\t" * indentNum + temp[:-1])
                    temp = i
                indentNum -= 1

        prettier.append("\t" * indentNum + temp)

        return prettier


if __name__ == '__main__':
    s = Solution
    a = "{'A':'B','C':{'D':'E','F':{'G':'H','I':'J'}}}"
    print(s.pretty_json(a))
