class Solution:
    @staticmethod
    def isVowel(letter):
        set1 = {'a', 'e', 'o', 'i', 'u'}
        return (letter in set1)

    @staticmethod
    def solve(A):
        count = 0
        consoCount = 0
        vowelCount = 0
        for letter in A:
            if Solution.isVowel(letter):
                count += consoCount  # consider all previous conso as start, and this vowel as end
                vowelCount += 1
            else:
                count += vowelCount  # consider all previous vowels as start, and this conso as end
                consoCount += 1

        return count % (10 ** 9 + 7)


    @staticmethod
    def solveB(A):
        tot = 0
        for i in range(0, len(A)):
            if A[i] == 'a' or A[i] == 'e' or A[i] == 'o' or A[i] == 'i' or A[i] == 'u':
                tot += 1

        return (tot * (len(A) - tot)) % 1000000007


if __name__ == '__main__':
    s = Solution
    M = 'A man, a plan, a canal: Panama'
    print(s.solveB(M))
