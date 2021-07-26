class Solution:
    @staticmethod
    def ispalindrome(A):
        s = ''.join(e for e in A.lower() if e.isalnum())
        if s == s[::-1]:
            return 1
        else:
            return 0


if __name__ == '__main__':
    s = Solution
    M = 'A man, a plan, a canal: Panama'
    print(s.ispalindrome(M))
