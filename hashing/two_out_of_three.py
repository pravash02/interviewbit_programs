class Solution:
    @staticmethod
    def solve(A, B, C):
        return sorted(list(((set(A) & set(B)) | (set(B) & set(C)) | (set(A) & set(C)))))

    @staticmethod
    def solveB(A, B, C):
        dic = {}
        for i in set(A):
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for j in set(B):
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1

        for k in set(C):
            if k in dic:
                dic[k] += 1
            else:
                dic[k] = 1

        A = set(A)
        B = set(B)
        C = set(C)
        ans = []
        for m in dic:
            if m in A and m in B and m in C:
                ans.append(m)

            elif m in A and m in B and m not in C:
                ans.append(m)

            elif m in A and m not in B and m in C:
                ans.append(m)

            elif m not in A and m in B and m in C:
                ans.append(m)

            else:
                continue
        ans.sort()
        return ans


if __name__ == '__main__':
    s = Solution
    A = [1, 2]
    B = [1, 3]
    C = [2, 3]
    print(s.solve(A, B, C))
