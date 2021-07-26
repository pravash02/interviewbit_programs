class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A, B):
        head1 = A
        head2 = B

        p1 = head1
        p2 = head2

        p1_prev = None
        while p1 and p2:
            if p1.val <= p2.val:
                p1_prev = p1
                p1 = p1.next
            else:
                if p1_prev != None: p1_prev.next = p2
                p1, p2 = p2, p1
        p1_prev.next = p2

        return head1 if head1.val <= head2.val else head2

    ### practice with custom inputs
    def solveB(self, l1, l2):
        head1 = l1.head
        head2 = l2.head

        p1 = head1
        p2 = head2

        prev = None
        while p1 and p2:
            if p1.val <= p2.val:
                prev = p1
                p1 = p1.next
            else:
                if prev is not None:
                    prev.next = p2
                p1, p2 = p2, p1

        prev.next = p2

        return head1 if head1.val <= head2.val else head2

    ### practice with custom inputs
    def solveC(self, l1, l2):
        head1 = l1.head
        head2 = l2.head

        head = None
        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        temp = head
        while head1 and head2:
            if head1.val < head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next

            temp = temp.next

        if head1:
            temp.next = head1
        if head2:
            temp.next = head2
        return head

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
    mylist2 = ListNode()
    mylist3 = ListNode()
    lst1 = [2, 3, 5]
    lst2 = [1, 4, 6]

    for i in range(0, len(lst1)):
        mylist1.push_at_begining(lst1[i])

    for i in range(0, len(lst2)):
        mylist2.push_at_begining(lst2[i])

    # print(mylist3.solveB(mylist1, mylist2))
    print(mylist3.solveC(mylist1, mylist2))
