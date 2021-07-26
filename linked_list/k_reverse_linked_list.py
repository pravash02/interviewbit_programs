class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A, B):
        tmp = A
        while tmp:
            arr = []
            t1 = tmp
            i = B
            while (i > 0) and tmp:
                arr.append(tmp.val)
                tmp = tmp.next
                i -= 1
            i = B - 1
            while (i > -1) and t1:
                t1.val = arr[i]
                t1 = t1.next
                i -= 1
            tmp = t1
        return A

    ### practice with custom inputs
    def solveB(self, B):
        if B == 1:
            return self.head
        curr = self.head
        if curr is None or curr.next is None:
            return self.head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = self.count()
        temp = []
        for i in range(n // B):
            temp.extend(arr[:B][::-1])
            del arr[:B]

        curr = self.head
        for i in range(len(temp)):
            curr.val = temp[i]
            curr = curr.next

        return self.head

    def count(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

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

    B = 3
    print(mylist.solveB(B))
