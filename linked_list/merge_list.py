class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solveB(self, A):
        if not A or not A.next:
            return A
        first, second = self.divide(A)
        first = self.solveB(first)
        second = self.solveB(second)
        return self.merge(first, second)

    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        left, right = first, second
        if left.val <= right.val:
            cur = left          # current pos of node
            head = first        # starting pos of node
            left = left.next
        else:
            cur = right
            head = second
            right = right.next
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return head

    def divide(self, head):
        fast, slow = head.next, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        second_part = slow.next
        slow.next = None
        return head, second_part

    def push_at_begining(self, node_data):
        new_node = Node(node_data)
        new_node.next = None
        cur = self.head
        if cur is None:
            self.head = new_node
            return
        else:
            while cur.next is not None:
                cur = cur.next
        cur.next = new_node


if __name__ == '__main__':
    mylist = ListNode()
    lst = [61, 3, 4, 7, 5, 6, 16, 15]
    for i in range(0, len(lst)):
        mylist.push_at_begining(lst[i])

    print(mylist.solveB())