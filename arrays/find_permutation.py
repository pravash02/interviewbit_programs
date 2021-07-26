class Solution:
    @staticmethod
    def find_perm(S, N):
        lst = []
        j = 0
        count = 0
        fnl_lst = []

        for i in range(0, N):
            count += 1
            lst.append(count)

        for i in range(0, len(S)):
            if S[i] == 'D':
                val = lst.pop(lst.index(max(lst)))
                fnl_lst.append(val)
            else:
                val = lst.pop(lst.index(min(lst)))
                fnl_lst.append(val)

        while j < len(lst):
            fnl_lst.append(lst[j])
            j += 1

        return fnl_lst

    @staticmethod
    def find_permB(s, n):
        res = []
        inc = 1
        dec = n
        for i in s:
            if i == 'I':
                res += [inc]
                inc += 1
            else:
                res += [dec]
                dec -= 1
        res += [inc if s[-1] == 'I' else dec]
        return res


if __name__ == '__main__':
    s1 = Solution
    n = 5
    s = 'DIDD'
    print(s1.find_permB(s, n))
