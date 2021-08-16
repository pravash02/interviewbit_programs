class Solution:
    @staticmethod
    def solve(A, B):
        T = {}
        num_uniq = 0
        for c in B:
            if c in T:
                x = T[c]
                T[c] = x - 1
            else:
                T[c] = 0
                num_uniq += 1

        count_uniq = 0
        head = 0
        tail = 0
        ret = ""
        while (True):
            if count_uniq < num_uniq:
                # advance head
                if head == len(A):
                    break
                c = A[head]
                if c in T:
                    x = T[c]
                    if x == 0:
                        count_uniq += 1
                    T[c] = x + 1
                head += 1
            else:
                # check if tail:head substring is shorter than existing solution
                if ret == "":
                    ret = A[tail:head]
                else:
                    if len(ret) > (head - tail):
                        ret = A[tail:head]
                # advance tail
                c = A[tail]
                if c in T:
                    x = T[c]
                    if x == 1:
                        count_uniq -= 1
                    T[c] = x - 1
                tail += 1

        return ret

    @staticmethod
    def solveB(s, t):
        dict_t = {}
        for i in t:
            if i in dict_t:
                dict_t[i] += 1
            else:
                dict_t[i] = 1
        left, right = 0, 0
        reqiured = len(dict_t)
        window_dict = {}
        formed = 0
        index1, index2 = 0, 0
        length = float('inf')
        while left < len(s) and right < len(s):
            character = s[right]
            if character in window_dict:
                window_dict[character] += 1
            else:
                window_dict[character] = 1
            if character in dict_t and window_dict[character] == dict_t[character]:
                formed += 1
            while formed == reqiured and left <= right:
                chrin = s[left]
                inlan = (right - left + 1)
                if inlan < length:
                    length = inlan
                    index1 = left
                    index2 = right
                window_dict[chrin] -= 1
                if chrin in dict_t and window_dict[chrin] < dict_t[chrin]:
                    formed -= 1
                left += 1
            right += 1

        return "" if length == float('inf') else s[index1:index2 + 1]


if __name__ == '__main__':
    s = Solution
    A = "ADOBECODEBANC"
    B = "ABC"
    print(s.solve(A, B))
    print(s.solveB(A, B))
