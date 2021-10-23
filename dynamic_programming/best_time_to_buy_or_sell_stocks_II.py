class Solution:
    def maxProfit(self, A):
        maxprofit=0
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                maxprofit += A[i]-A[i-1]
        return maxprofit


if __name__ == '__main__':
    s = Solution()
    A = [1, 5, 9]
    print(s.maxProfit(A))
