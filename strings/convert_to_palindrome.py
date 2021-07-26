class Solution:
    @staticmethod
    def palindrome(A):
        lst = []
        n = len(A) - 1

        for i in range(0, len(A) // 2):
            if A[i] != A[n-i]:
                lst.append(i)
                lst.append(n-i)

        if len(lst) == 0:
            return 1

        ## to iterate through the rest of the element
        i = lst[0]
        j = lst[1]
        ## removing the elements
        res1 = A[:i] + A[i + 1:]
        res2 = A[:j] + A[j + 1:]

        if res1 == res1[::-1]:
            return 1
        elif res2 == res2[::-1]:
            return 1
        else:
            return 0


if __name__ == '__main__':
    s = Solution
    a = 'abecbea'
    print(s.palindrome(a))
