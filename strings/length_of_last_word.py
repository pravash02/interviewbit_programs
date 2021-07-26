class Solution:
    @staticmethod
    def len_of_lastword(A):
        return len(A.strip().split(' ')[-1])


if __name__ == '__main__':
    s = Solution
    M = 'A man, a plan, a canal: Panama'
    print(s.len_of_lastword(M))
