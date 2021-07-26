class Solution:
    @staticmethod
    def hamm_dist(A):
        ans = 0
        for i in range(0, 32):
            countone = 0
            for j in range(len(A)):
                if int(A[j] & 1 << i):
                    countone += 1

            countzero = len(A) - countone
            ans = ans + countone * countzero * 2
        return ans % 1000000007

    @staticmethod
    def hamm_distB(A):
        l = []

        for i in A:
            l.append('{:032b}'.format(i))
        c = 0

        l = list(zip(*l))
        for i in l:
            a = i.count('0')
            b = i.count('1')
            c += (2 * a * b)

        return c % 1000000007


if __name__ == '__main__':
    s = Solution
    n = [1, 3, 6]
    print(s.hamm_distB(n))
