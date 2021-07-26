class Solution:

    @staticmethod
    def plus_one(A):
        a = A
        n = len(a)

        a[n - 1] += 1
        carry = a[n - 1] / 10   # quotient
        a[n - 1] = a[n - 1] % 10    # remainder

        for i in range(n - 2, -1, -1):
            if (carry == 1):
                a[i] += 1
                carry = a[i] / 10
                a[i] = a[i] % 10

        if (carry == 1):
            a.insert(0, 1)

        str_a = ''.join(str(i) for i in a)
        new_a = str_a.lstrip('0')

        a = list(new_a)

        return a


if __name__ == '__main__':
    s = Solution
    lst = [0, 0, 1, 5, 6, 8]
    print(s.plus_one(lst))
