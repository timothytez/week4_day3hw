from Node import Node
from BST import BinarySearchTree

class LinkedList:

    def __init__(self, head_value):
        self.head = Node(head_value)
    
    def __repr__(self):
        return f'<LinkedList: {" -> ".join(node.value for node in self)}>'

    def __iter__(self):
        current_node = self.head
        while current_node.right:
            yield current_node
            current_node = current_node.right
        yield current_node

    def append_node(self, value):
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = Node(value)

    def insert(self, neighbor, value):
        for node in self:
            if node.value == neighbor:
                next_node = node.right
                node.right = Node(value)
                node.right.right = next_node
                return
        print(f'{neighbor} not in LinkedList')

    def update_head(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.right = old_head

    def search(self,value):
        for node in self:
            if node.value == value:
                return node
        return False
    
    def get_tail(self):
        for node in self:
            pass
        return node
    
    def remove(self, value):
        pass

    def create_sorted_ll(self, alist):
        bst = BinarySearchTree(self.head.value)
        for num in alist:
            bst.add_node(num)
        return bst


ll == LinkedList(100)

ll.create_sorted_ll([109,8,88,77,200,4])

linkedlist = LinkedList('Monday')
linkedlist.append_node('Tuesday')
linkedlist.append_node('Wednesday')
linkedlist.append_node('Friday')


    