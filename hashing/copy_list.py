class Solution:

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    ### interviewbit solution
    def solve(self, head):
        curr = head
        while curr:
            node = Solution(curr.label)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = curr.next.next
        curr = head
        while curr:
            temp = curr.next.next
            curr.next.next = temp.next if temp else None
            curr.next.random = curr.random.next if curr.random else None
            curr = temp

        return head.next

    ### interviewbit solution
    def solveB(self, head):
        from collections import defaultdict
        d = defaultdict(lambda: Solution(0))
        d[None] = None
        m = head

        while m:
            d[m].label = m.label
            d[m].next = d[m.next]
            d[m].random = d[m.random]
            m = m.next

        return d[head]


if __name__ == '__main__':
    s = Solution
    A = []
    print(s.solve(A))
