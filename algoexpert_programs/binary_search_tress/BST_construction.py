"""
Creating a Binary Search Tree from given input list of vslues

"""


class Newnode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        # val = self.value

    # def print_node_values(self, val):
    #     if val != None:
    #         self.print_node_values(val.left)
    #         print(str(val.value))
    #         self.print_node_values(val.right)


class BinarySearchTree:
    def __init__(self):
        self.node = None

    def insert_root_nodes(self, value):
        if self.node == None:
            self.node = Newnode(value)
        else:
            self.insert_child_nodes(self.node, value)

    def insert_child_nodes(self, cur_node, value):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Newnode(value)
            else:
                self.insert_child_nodes(cur_node.left, value)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = Newnode(value)
            else:
                self.insert_child_nodes(cur_node.right, value)
        else:
            'value is already in the tree'

    def print_bst_tree(self):
        if self.node != None:
            self.print_node_values(self.node)

    def print_node_values(self, cur_node):
        if cur_node != None:
            self.print_node_values(cur_node.left)
            print(str(cur_node.value))
            self.print_node_values(cur_node.right)


if __name__ == '__main__':
    list_nodes = [2, 5, 3, 15, 10, 7, 8, 4, 19, 5]
    bst_tree = BinarySearchTree()

    for i in list_nodes:
        bst_tree.insert_root_nodes(i)

    bst_tree.print_bst_tree()
    # nnode = Newnode(bst_tree.node)
    # nnode.print_node_values(nnode.value)
