import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def solve(A):
        dummy = ListNode(float('inf'))
        d = dummy
        list1 = []
        for i in A:
            p = i
            while p:
                list1.append(p.val)
                p = p.next
        heapq.heapify(list1)
        for _ in range(len(list1)):
            val = heapq.heappop(list1)
            node = ListNode(val)
            d.next = node
            d = d.next

        return dummy.next


if __name__ == '__main__':
    s = Solution
    A = [3, 2]
    print(s.solve(A))
