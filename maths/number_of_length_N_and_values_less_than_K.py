import math


class Solution:
    @staticmethod
    def solution(A, N, K):
        ans = 0

        if len(A) == 0:
            return 0

        if N > len(str(K)):
            return 0
        elif N < len(str(K)):
            if A[0] == 0:
                return int((len(A)-1)*math.pow(len(A), N-1))
            else:
                return int(math.pow(len(A), N))
        else:
            if N == 1:
                for i in range(len(A)):
                    if A[i] < K:
                        ans += 1
            else:
                count = 0
                temp = list(str(K))
                temp = [int(i) for i in range(len(temp))]
                for i in range(0, len(A)):
                    if A[i] == 0:
                        continue
                    if A[i] > temp[0]:
                        break
                    count += 1

                ans += ((count) * int(math.pow(len(A), N-1)))

                flag = 0
                j = 0
                for i in range(0, len(A)):
                    if A[i] == temp[0]:
                        flag = 1
                        j += 1
                while flag == 1 and j <= N-1:
                    countx = 0
                    flag = 0
                    for i in range(0, len(A)):
                        if A[i] > temp[j]:
                            countx += 1
                        if A[i] == temp[j]:
                            flag = 1
                        ans -= ((countx) * int(math.pow(len(A), N-j-1)))
                    j += 1

                    if j == N and flag == 1:
                        ans -= 1

        return ans

    @staticmethod
    def solutionB(A, B, C):
        if not A:
            return 0
        elif C < 10 ** (B - 1):
            return 0
        elif C > 10 ** B:
            n = len(A)
            if A[0] == 0 and B > 1:
                return (n - 1) * math.pow(n, B - 1)
            else:
                return math.pow(n, B)
        elif B == 1:
            return len([i for i in A if i < C])
        else:
            n = len(A)
            T = str(C)
            output = 0
            for i in range(B):
                temp_lt = 0
                temp_eq = 0
                for j in A:
                    if j < int(T[i]):
                        temp_lt += 1
                    elif j == int(T[i]):
                        temp_eq = 1
                    else:
                        break
                if i == 0 and A[0] == 0:
                    output += (temp_lt - 1) * math.pow(n, B - i - 1)
                else:
                    output += temp_lt * math.pow(n, B - i - 1)
                if temp_eq == 0:
                    break

        return output


if __name__ == '__main__':
    s = Solution
    lst = [0, 1, 2, 5]
    lst1 = [1, 2, 4, 5]
    lst2 = [0, 1, 2, 3, 4]
    b = 2
    c = 21
    print(s.solutionB(lst, b, c))
