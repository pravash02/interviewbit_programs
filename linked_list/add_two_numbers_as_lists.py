class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A, B):
        l1 = A
        l2 = B
        carry = 0
        cur = temp = ListNode(0)

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next

            carry = carry // 10
        return temp.next

    ### practice with custom inputs
    def solveB(self, l1, l2):
        new_node = Node(0)
        self.head = new_node
        result = self.head  # to iterate over the self.head for this instance

        lst1 = l1.head
        lst2 = l2.head

        sum = 0
        carry = 0
        while lst1 is not None or lst2 is not None or carry != 0:
            sum = 0

            if l1 is not None:
                sum += lst1.val
                lst1 = lst1.next

            if l2 is not None:
                sum += lst2.val
                lst2 = lst2.next

            sum = sum + carry
            carry = sum//10     # calculating the quotient

            result.next = Node(sum % 10)    # passing the remainder to the linked list
            result = result.next

        # while self.head:
        #     self.head = self.head.next
        #     print(self.head.val)

        return self.head.next

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
    lst1 = [2, 4, 3]
    lst2 = [5, 6, 4]

    for i in range(0, len(lst1)):
        mylist1.push_at_begining(lst1[i])

    for i in range(0, len(lst2)):
        mylist2.push_at_begining(lst2[i])

    print(mylist3.solveB(mylist1, mylist2))

