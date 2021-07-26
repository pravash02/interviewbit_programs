class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A):
        if not A: return A
        curr, sortedLL = A.next, ListNode(A.val)
        sLL_h = sortedLL
        while curr:
            prev = None
            while sortedLL:
                if sortedLL.val < curr.val:
                    prev = sortedLL
                    if sortedLL.next:
                        sortedLL = sortedLL.next
                    else:
                        sortedLL.next = ListNode(curr.val)
                        break
                elif prev:
                    prev.next = ListNode(curr.val)
                    prev.next.next = sortedLL
                    break
                else:
                    prev = ListNode(curr.val)
                    prev.next = sLL_h
                    sLL_h = prev
                    break
            sortedLL = sLL_h
            curr = curr.next
        return sLL_h

    ### practice with custom inputs
    def solveB(self):
        start = Node(None)
        start.next = self.head
        prev = start
        curr = self.head

        while curr:
            if curr.next and curr.next.val < curr.val:
                while prev.next is not None and prev.next.val < curr.next.val:
                    prev = prev.next

                temp = prev.next
                prev.next = curr.next
                curr.next = curr.next.next
                prev.next.next = temp
                prev = start
            else:
                curr = curr.next

        return start.next

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
    # v = mylist.solveB()
    # while v:
    #     print(v.val)
    #     v = v.next
