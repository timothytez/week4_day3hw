# from Node import Node
# from BST import BinarySearchTree


# #Nodes has two attributes
# #value = anything that is a string, integer, or object
# #the next = (all nodes have a next attribute to connect to the next node)

# class linkedlist:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

#     #Values

#     #"January"
#     #"February"
#     #"March"
#     #"April"
#     #"May"
#     #"June"
#     #"July"
#     #"August"
#     #"September"
#     #"October"
#     #"November"
#     #"December"

# node1 = linkedlist("Jaunary")
# node2 = linkedlist("February")
# node3 = linkedlist("March")
# node4 = linkedlist("April")
# node5 = linkedlist("May")
# node6 = linkedlist("June")
# node7 = linkedlist("July")
# node8 = linkedlist("August")
# node9 = linkedlist("September")
# node10 = linkedlist("October")
# node11 = linkedlist("November")
# node12 = linkedlist("December")


# node1.next_node = node2   #this shows that node 1 is connected to node 2...
# node2.next_node = node3
# node3.next_node = node4
# node4.next_node = node5
# node5.next_node = node6
# node6.next_node = node7
# node7.next_node = node8
# node8.next_node = node9
# node9.next_node = node10
# node10.next_node = node11
# node11.next_node = node12

# current_node = node1
# while True:
#     print (current_node.value, "-->")
#     if current_node.value is None: 
# #if after node 1 there is nothing then print none if not continue to next node
#         break
        
#     current_node = current_node.next_node

#     def printlinkedlist(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.value)
#             current_node = current_node.nextnode
#     print(None)



# #     public class LinkedList { --------- this is the class inwhich your are making your synax about




# #   Node head;                ---------------- this is your starter point and first node
# #   public void append(int data) {  ------------ here is where your add or insert your data to create you node
# #     if (head == null) {       --------------- if the head or the starting point comes to an end or nothing else to report you move on to the next node
# #       head = new Node(data);   ------------- the head now becomes a new node and your starting point. lets say it went from A to B. Now the starting point is B going to C.
# #       return;
# #     }
# #     Node current = head;
# #     while (current.next != null) {    ----------- over all the cycle continues until there is n more data or we have reached our end.
# #       current = current.next;
# #       }
# #     current.next = new Node(data);
# #   }
# # }




# class linkedlist_pokemon:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

from Node import Node
from BST import BinarySearchTree

class LinkedList:

  def __init__(self, head_value):
    self.head = Node(head_value)

  def __repr__(self):
    # output =  f'<LinkedList: '
    # for node in self:
    #   output += f'{str(node.value)} -> '
    # return output.rstrip(' -> ')
    return f'<LinkedList: {" -> ".join(str(node.value) for node in self)}>'
  
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
    # new_head = Node(value)
    # new_head.right = self.head
    # self.head = new_head

  def search(self, value):
    for node in self:
      if node.value == value:
        return node
    return False
  
  def get_tail(self):
    for node in self:
      pass
    return node
  

  def remove(self, value):
    if value == self.head.value:
      self.head = self.head.right
      return
    for node in self:
      if node.right and value == node.right.value:
        node.right = node.right.right
        return

  def create_sorted_ll(self, alist):
    bst = BinarySearchTree(self.head.value)
    for num in alist:
      bst.add_node(num)
    bst.store_sorted()
    for value in bst.sorted_values:
      self.append_node(value)
    self.remove(self.head.value)


    


ll = LinkedList(100)

ll.create_sorted_ll([109,8,88,77,200,4])

print(ll)

    