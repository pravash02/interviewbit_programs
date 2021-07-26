class Solution:
    @staticmethod
    def sub_array(A):
        c = 0
        for i in range(len(A)):
            if A[i] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                c = c + (len(A) - i)  ###
        return c % 10003

    ### handling repeated strings
    @staticmethod
    def sub_arrayB(A):
        count = 0
        n = len(A)
        result = set({})
        for i in range(0, n):
            if A[i] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                for j in range(i, n+1):
                    result.add(A[i:j])

        result.remove('')
        return len(result) % 10003


if __name__ == '__main__':
    s = Solution
    a = "ABEC"
    print(s.sub_array(a))
    print(s.sub_arrayB(a))
