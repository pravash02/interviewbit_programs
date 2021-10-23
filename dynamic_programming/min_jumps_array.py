class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def jump(self, A):
        max_jump = 0
        jumps = 0
        i = 0

        if (A[0] == 0 and len(A) > 1):
            return (-1)
        if (A[0] == 0 and len(A) == 1):
            return (0)

        while (i < len(A) - 1):
            maxi = float("-inf")
            indi = float("inf")
            max_jump = A[i] + i

            if (max_jump < len(A) - 1):
                jumps += 1
            elif (max_jump >= len(A) - 1):
                jumps += 1
                break

            for j in range(i + 1, A[i] + i + 1):
                if (j <= len(A) - 1):
                    if (A[j] + j > maxi):
                        maxi = A[j] + j
                        indi = j

            ele = indi
            i = ele

        return jumps

    def solve(self, A):
        n = len(A)
        current_range = A[0]
        if current_range == 0 and n == 1:
            return 0
        max_range = A[0]
        jumps = 1
        can_reach = 0
        i = 0
        while i <= current_range:
            max_range = max(max_range, i + A[i])
            if i == n - 1:
                can_reach = 1
                break
            if i == current_range:
                current_range = max_range
                jumps += 1
            i += 1

        if can_reach == 1:
            return jumps

        return -1


if __name__ == '__main__':
    s = Solution()
    A = [2, 1, 1]
    print(s.jump(A))
