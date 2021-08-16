class Solution:

    @staticmethod
    def solve(A, B):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1 if A[0] == B else 0

        count = 0

        hashmap = {}
        hashmap[0] = 1
        xor = 0
        for i in range(len(A)):
            xor ^= A[i]
            if xor ^ B in hashmap:
                count += hashmap[xor ^ B]

            if xor not in hashmap:
                hashmap[xor] = 0
            hashmap[xor] += 1

        return count


if __name__ == '__main__':
    s = Solution
    A = [4, 2, 2, 6, 4]
    B = 6
    print(s.solve(A, B))
