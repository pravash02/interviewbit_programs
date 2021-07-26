class Solution:
    @staticmethod
    def valid_num(A):
        try:
            a = float(A)
            if A[-1] == '.':
                return 0
            for i in range(len(A)):
                if A[i] == 'e':
                    if A[i - 1] == '.':
                        return 0
            return 1
        except Exception as e:
            return 0

    @staticmethod
    def valid_numB(A):
        try:
            x = float(A)
            y = A.split('e')
            for ele in y:
                if ele == "":
                    return 0
                if ele[-1] == ".":
                    return 0

            return 1

        except Exception as e:
            return 0


if __name__ == '__main__':
    s = Solution
    a = "0"
    print(s.valid_num(a))
