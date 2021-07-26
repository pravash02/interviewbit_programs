class Solution:
    @staticmethod
    def reverse_str(A):
        d = A.split()
        d.reverse()
        p = ' '
        p = p.join(d)
        return p


if __name__ == '__main__':
    s = Solution
    M = 'A man, a plan, a canal: Panama'
    print(s.reverse_str(M))
