class Solution:
    def maxProduct(self, x):
        def one_side_max(A):
            result = A[0]
            positive_product = 1
            total_product = 1
            for i in range(len(A)):
                total_product *= A[i]
                positive_product *= A[i]
                result = max(result, max(positive_product, total_product))
            if total_product == 0:
                total_product = 1
            if positive_product <= 0:
                positive_product = 1
            return result
        X = []
        for i in x:
            X.append(i)
        r1 = one_side_max(X)
        Y = X[::-1]
        r2 = one_side_max(Y)
        return max(r1, r2)


if __name__ == '__main__':
    s = Solution()
    A = [-120, -202, -293, -60, -261]
    print(s.maxProduct(A))
