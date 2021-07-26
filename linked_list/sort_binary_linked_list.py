class Node:
    # Function to initialize the node object
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    # Function to initialize the Linked List
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A):
        node = Node(0)
        start = end = node
        while A:
            nextA = A.next
            if A.val == 0:  # Inserting at head
                nextS = start
                start = A
                start.next = nextS
            else:  # Inserting at tail
                end.next = A
                end = end.next
                end.next = None
            A = nextA
        return start.next

    ### practice with custom inputs
    def solveB(self):
        count = [0, 0]

        ptr = self.head
        while ptr is not None:
            count[ptr.val] += 1     # incrementing the values based on index
            ptr = ptr.next

        i = 0
        ptr = self.head
        while ptr is not None:
            if count[i] == 0:
                i += 1      # incrementing the index if that value's count is 0
            else:
                ptr.val = i
                count[i] -= 1
                ptr = ptr.next

    ### creating a reversed linkedlist
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def push_at_begining(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        cur = self.head
        if cur is None:
            self.head = new_node
            return
        else:
            while cur.next is not None:
                cur = cur.next
        cur.next = new_node

    def printList(self):
        lst = []
        temp = self.head
        while temp != None:
            lst.append(temp.val)
            temp = temp.next
        print(lst)


if __name__ == '__main__':
    mylist = ListNode()
    lst = [0, 1, 0, 0, 1, 1]
    for i in range(0, len(lst)):
        mylist.push_at_begining(lst[i])

    mylist.printList()
    mylist.solveB()
    mylist.printList()
