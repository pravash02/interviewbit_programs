class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solveA(self, A):
        slow = A
        fast = A
        while True:
            if fast.next == None or fast.next.next == None:
                break

            else:
                slow = slow.next
                fast = fast.next.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrom
        while prev and A:
            if prev.val != A.val:
                return 0
            prev = prev.next
            A = A.next

        return 1

    ### interviewbit solution
    def solveB(self):
        # middle element
        cur = self.head
        mid = self.head
        while cur:
            if cur.next and cur.next.next:
                mid = mid.next
                cur = cur.next.next
            else:
                break

        # reverse the second half of the linked list after the mid element
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        # check for palindrome
        while prev and self.head:
            if prev.val != self.head.val:
                return 0
            prev = prev.next
            self.head = self.head.next

        return 1

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
    mylist1 = ListNode()
    lst1 = [2, 3, 1, 3, 2, 1]

    for i in range(0, len(lst1)):
        mylist1.push_at_begining(lst1[i])

    print(mylist1.solveB())

