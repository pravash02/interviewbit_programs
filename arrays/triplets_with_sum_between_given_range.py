class SolutionA:
    @staticmethod
    def triplet_sum(A, val):
        A = list(map(float, A))
        A.sort()

        triplet_nbrs = SolutionA.calc_sum(A, val[-1]) - SolutionA.calc_sum(A, val[0] - 1)
        return triplet_nbrs

    @staticmethod
    def calc_sum(A, val):
        res = 0

        for i in range(0, len(A)-1):
            j = i + 1
            k = len(A) - 1

            while j != k:
                s = A[i] + A[j] + A[k]

                if s >= val:
                    k -= 1
                else:
                    res += (k - j)
                    j += 1
        return res


class SolutionB:
    @staticmethod
    def solve(A, val):
        A = list(map(float, A))
        A.sort()

        for i in range(0, len(A)-1):
            j = i + 1
            k = len(A) - 1

            while j != k:
                    s = A[i] + A[j] + A[k]

                    if val[0] < s < val[-1]:
                        return 1
                    elif s >= val[-1]:
                        k -= 1
                    elif s <= val[0]:
                        j += 1
                    else:
                        pass
        return 0

    @staticmethod
    def solveB(A):
        a = 0
        t = [0] * len(A)
        for i in range(0, len(A)):
            t[i] = float(A[i])
        t.sort()
        for i in range(len(A) - 2):
            j = i + 1
            k = j + 1
            if k < len(A) and j < len(A):
                a = t[i] + t[j] + t[k]
            if a > 2:
                a = t[k] + t[0] + t[1]
            if a > 1 and a < 2:
                return 1
        return 0


if __name__ == '__main__':
    range_val = [1, 2]
    s = SolutionA
    # lst = ["0.002804", "0.000298", "0.748024", "0.139023", "0.082317", "0.013348", "4.209490", "0.098512", "0.055635", "0.060427", "3.290499", "0.073212", "0.071914", "0.065654", "0.044422", "0.024968", "0.110226", "0.090197", "0.060240", "0.100432", "0.109920", "0.023673", "0.081927", "0.066987", "0.058557", "0.043674", "0.057256", "0.050478", "0.024976", "0.048124", "0.071043", "0.048199", "0.023894", "0.058934", "0.047465", "0.088664", "0.002571", "0.070546", "0.042776"]
    # lst = ["2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191"]
    # lst = ["0.234022", "0.051717", "0.820402", "0.492629", "0.004825", "0.589073"]
    lst = ["0.297657", "0.420048", "0.053365", "0.437979", "0.375614", "0.264731", "0.060393", "0.197118", "0.203301", "0.128168"]
    print(s.triplet_sum(lst, range_val))

    s1 = SolutionB
    print(s1.solve(lst, range_val))
    print(s1.solveB(lst))
