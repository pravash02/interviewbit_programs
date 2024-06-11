"""
Fix Sized Window -
30. Substring with Concatenation of All Words                                                           solved
187. Repeated DNA Sequences                                                                             solved
438. Find All Anagrams in a String
567. Permutation in String
643. Maximum Average Subarray I                                                                         priority
1100. Find K-Length Substrings With No Repeated Characters (P)
1151. Minimum Swaps to Group All 1's Together (P)
1176. Diet Plan Performance (P)
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
1423. Maximum Points You Can Obtain from Cards
1456. Maximum Number of Vowels in a Substring of Given Length                                           priority
1652. Defuse the Bomb
1876. Substrings of Size Three with Distinct Characters
2090. K Radius Subarray Averages
2269. Find the K-Beauty of a Number
2379. Minimum Recolors to Get K Consecutive Black Blocks

Variable Sized Window -
3. Longest Substring Without Repeating Characters                                                       solved
76. Minimum Window Substring                                                                            priority
159. Longest Substring with At Most Two Distinct Characters
209. Minimum Size Subarray Sum                                                                          solved
340. Longest Substring with At Most K Distinct Characters (P)                                           priority
424. Longest Repeating Character Replacement
487. Max Consecutive Ones II (P)
904. Fruit Into Baskets
992. Subarrays with K Different Integers
1004. Max Consecutive Ones III                                                                          priority
1297. Maximum Number of Occurrences of a Substring
1493. Longest Subarray of 1's After Deleting One Element                                                priority
1695. Maximum Erasure Value
1838. Frequency of the Most Frequent Element
1852. Distinct Numbers in Each Subarray (P)
2024. Maximize the Confusion of an Exam
2260. Minimum Consecutive Cards to Pick Up
2062. Count Vowel Substrings of a String

"""

import collections
import copy
from collections import Counter, defaultdict
from heapq import heappush, heappop


def lengthOfLongestSubstring(s):
    # d = {}
    # start = count = 0
    # for i in range(len(s)):
    #     if s[i] in d and start <= d[s[i]]:
    #         start = d[s[i]] + 1
    #     else:
    #         count = max(count, i - start + 1)
    #     d[s[i]] = i
    # return count

    seen = {}
    left_ind = 0
    right_ind = 0
    len_substr = 1

    for right_ind in range(len(s)):
        if s[right_ind] in seen:
            # max() to ensure that left_ind always goes to the right of it, or just stays at its position
            left_ind = max(left_ind, seen[s[right_ind]] + 1)
        len_substr = max(len_substr, right_ind - left_ind + 1)
        seen[s[right_ind]] = right_ind

    print("Longest Substring Without Repeating Characters - ", len_substr)
    return len_substr


def findSubstring(s, words):
    hmap = Counter(words)
    wlen = len(words[0])
    tlen = len(words) * wlen

    def checksubstr(substr, hmap):
        # every word is of same len, so we skip that amount
        for i in range(0, len(substr), wlen):
            if hmap[substr[i:i + wlen]] != 0:
                hmap[substr[i:i + wlen]] -= 1
            else:
                return False
        return True

    res = []
    start = 0
    for i in range(tlen, len(s) + 1):
        if checksubstr(s[start:i], copy.deepcopy(hmap)):
            res.append(start)
        start += 1

    return res


def minWindow(s, t):
    def is_substring(expected, actual):
        for c in expected:
            if expected[c] > actual[c]:
                return False
        return True

    expected, window = Counter(t), defaultdict(int)
    start = 0
    min_string = ""

    for end, c in enumerate(s):
        window[c] += 1
        while start <= end and is_substring(expected, window):
            if not min_string or end - start + 1 < len(min_string):
                min_string = s[start:end + 1]
            window[s[start]] -= 1
            start += 1

    return min_string


def findRepeatedDnaSequences(s):
    occurences = {}
    for i in range(len(s)-9):
        substr = s[i:i+10]
        occurences[substr] = occurences.get(substr, 0) + 1

    return [substr for substr in occurences if occurences[substr] > 1]


def minSubArrayLen(nums, target):
    left, right, total = 0, 0, 0

    # initialize minimum length to be the length of the array plus 1 (invalid)
    min_len = len(nums) + 1

    while right < len(nums):
        # add current number to the sum
        total += nums[right]
        # move right pointer
        right += 1

        # check if the sum is greater than or equal to target
        while total >= target:
            # update minimum length if necessary
            min_len = min(min_len, right - left)
            # subtract left number from the sum and move left pointer
            total -= nums[left]
            left += 1

    # if minimum length is still the initialized value, there is no valid subarray
    if min_len == len(nums) + 1:
        return 0
    else:
        return min_len


def containsNearbyDuplicate(nums, k):
    found = {}

    for i, val in enumerate(nums):
        if val in found and i - found[val] <= k:
            return True
        found[val] = i

    return False


def maxSlidingWindow(nums, k):
    # res = []
    # for i in range(0, len(nums)-k+1):
    #     res.append(nums[i:i+k])

    # h, ans = [], []
    # for i in range(0, len(nums)):
    #     heappush(h, (-nums[i], i))
    #     while h[0][1] <= i - k: heappop(h)
    #     if i >= k - 1: ans.append(-h[0][0])
    # return ans

    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))

        while d and nums[d[-1]] < n:
            d.pop()
            print("\t Popped from d because d has elements and nums[d.top] < curr element")

        d.append(i)
        print("\t Added i to d")

        if d[0] == i - k:
            d.popleft()
            print("\t Popped left from d because it's outside the window's leftmost (i-k)")

        if i>=k-1:
            out.append(nums[d[0]])
            print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
    return out


def sumOfConsecutiveSubArray(s, k):
    max_sum = 0
    cur_sum = 0
    for i in range(len(s)):
        cur_sum += s[i]
        if i >= k - 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= s[i - (k - 1)]

    return max_sum


def longestSubstring(s: str, k: int) -> int:
    if len(s) < k:
        return 0

    counter = Counter(s)

    for char, count in counter.items():
        if count < k:
            return max(longestSubstring(substring, k) for substring in s.split(char))


if __name__ == '__main__':
    # print("Longest Substring Without Repeating Characters - ", lengthOfLongestSubstring('abcabcbb'))
    # print("Substring with Concatenation of All Words - ", findSubstring("barfoothefoobarman", ["foo", "bar"]))
    # print(minWindow("ADOBECODEBANC", "ABC"))      # need to check
    # print("Repeated DNA Sequences - ", findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    # print("Minimum Size Subarray Sum - ", minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
    # print(containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    # print(sumOfConsecutiveSubArray([1, 2, 3, 4, 5, 6, 1, 2], 3))
    print(longestSubstring(s="aaabb", k=3))

