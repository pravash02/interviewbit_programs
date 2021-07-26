class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solveA(self, A):
        marker = ListNode(0)
        while True:
            tmp = A
            A = A.next
            tmp.next = marker

            if A is None:
                return None

            if A.next == marker:
                return A

    ### interviewbit solution
    def solveB(self, A):
        print(A.val)
        temp = A
        res = set()
        while temp:
            if temp.val not in res:
                res.add(temp.val)
            else:
                return temp
            temp = temp.next
        else:
            return None

    ### practice with custom inputs
    def solveC(self):
        temp = self.head
        res = set()
        while temp:
            if temp.val not in res:
                res.add(temp.val)
            else:
                return temp
            temp = temp.next
        else:
            return None

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
    lst1 = [2, 4, 3, 2]

    for i in range(0, len(lst1)):
        mylist1.push_at_begining(lst1[i])

    print(mylist1.solveC())
