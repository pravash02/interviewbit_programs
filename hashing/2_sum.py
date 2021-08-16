class Solution:
    @staticmethod
    def solve(A, B):
        result = []
        dic = {}
        for i in range(len(A)):
            if A[i] in dic:
                result.append([dic[A[i]], i + 1])
            else:
                if B - A[i] not in dic:
                    dic[B - A[i]] = i + 1

        return result[0] if len(result) > 0 else []


if __name__ == '__main__':
    s = Solution
    A = [2, 7, 11, 15]
    B = 9
    print(s.solve(A, B))
