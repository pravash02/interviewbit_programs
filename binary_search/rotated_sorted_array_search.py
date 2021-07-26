class Solution:
    @staticmethod
    def rotated_arr_search(A, B):
        if B in A:
            return (A.index(B))
        else:
            return -1


if __name__ == '__main__':
    s = Solution
    A = [3, 9, 10, 20, 17, 5, 1]
    B = 20
    print(s.rotated_arr_search(A, B))
