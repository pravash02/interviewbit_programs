class Solution:
    @staticmethod
    def zigzag_str(A, B):
        ans = {}
        temp = 0
        flag = 0

        if B >= len(A):
            return A
        if B == 1:
            return A

        for i in range(1, len(A)+1):
            if flag == 0:
                temp += 1
            if flag == 1:
                temp -= 1
            if temp == B:
                flag = 1
            if temp == 1:
                flag = 0

            if temp in ans.keys():
                ans[temp] += A[i-1]
            else:
                ans[temp] = A[i-1]

        res = ""
        for j in range(1, B+1):
            res += ans[j]

        return res

    @staticmethod
    def zigzag_strB(A, B):
        res = ""
        n = len(A)
        spaces = 2 * (B - 1) - 1  # appropriate spaces acc. to lines below the current one
        zeros = -1  # appropriate spaces acc. to lines above the current one

        if B == 1 or A == "":
            return A

        for i in range(B):
            j = i
            while j < n:
                if spaces > 0:
                    res += A[j]
                    j += spaces + 1

                if zeros > 0 and j < n:
                    res += A[j]
                    j += zeros + 1

            spaces -= 2
            zeros += 2

        return res


if __name__ == '__main__':
    s = Solution
    A = 'PAYPALISHIRING'
    B = 3
    print(s.zigzag_str(A, B))
    print(s.zigzag_strB(A, B))
