class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A):
        tempList = []
        curr = A
        curr = curr.next
        while curr and curr.next and curr.next.next:
            tempList.append(curr.val)
            curr = curr.next.next
        if curr:
            tempList.append(curr.val)
        curr = A
        curr = curr.next
        while curr and curr.next and curr.next.next:
            curr.val = tempList.pop()
            curr = curr.next.next
        if curr and tempList:
            curr.val = tempList.pop()

        return A

    ### practice with custom inputs
    def solveB(self):
        tempList = []
        curr = self.head
        curr = curr.next
        while curr and curr.next and curr.next.next:
            tempList.append(curr.val)
            curr = curr.next.next
        if curr:
            tempList.append(curr.val)
        curr = self.head
        curr = curr.next
        while curr and curr.next and curr.next.next:
            curr.val = tempList.pop()
            curr = curr.next.next
        if curr and tempList:
            curr.val = tempList.pop()
        return self.head

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
    lst = [3, 4, 7, 5, 6, 16, 15, 61, 16]
    for i in range(0, len(lst)):
        mylist.push_at_begining(lst[i])

    mylist.solveB()
