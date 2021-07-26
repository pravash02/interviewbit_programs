import math


class Solution:
    @staticmethod
    def solve(A, B):
        # According to number of elements there will be "n" blocks in total permutations
        # and there are (n-1)! permutations present in each block

        arr = [i for i in range(1, A + 1)]
        ans = ""
        while (arr):
            index = B // (math.factorial(len(arr) - 1))  # by doing this we find our 1st element of kth
            # permutation i.e from which block our 1st element belongs to

            if (B % (math.factorial(len(arr) - 1)) == 0):
                index -= 1
            ans += str(arr[index])  # then we add element into string

            B = B - (math.factorial(len(arr) - 1)) * index  # decrementing our k because now
            # we have to obtain another element of kth permutation

            arr.remove(arr[index])  # removing element which has been used
        return (ans)


if __name__ == '__main__':
    s = Solution
    A = 11
    B = 2
    print(s.solve(A, B))
