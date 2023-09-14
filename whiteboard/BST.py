from Node import Node

class BinarySearchTree:

  def __init__(self, root_value):
    self.root = Node(root_value)

  def __repr__(self):
    return f'<BST: {self.root}'
  
  def add_node(self, value, current_node=None):
    if not current_node:
      current_node = self.root
    if value > current_node.value:
      if current_node.right:
        self.add_node(value, current_node.right)
      else:
        current_node.right = Node(value)
    elif value < current_node.value:
      if current_node.left:
        self.add_node(value, current_node.left)
      else:
        current_node.left = Node(value)

  def search(self, value, current_node=None):
    if not current_node:
      current_node = self.root
    if value > current_node.value:
      if current_node.right:
        return self.search(value, current_node.right)
    elif value < current_node.value:
      if current_node.left:
        return self.search(value, current_node.left)
    else:
      return current_node
    print(f'Node: {value} not found')
    return False

  def get_min(self):
    current_node = self.root
    while current_node.left:
      current_node = current_node.left
    return current_node
  
  def get_max(self, current_node = None):
    if not current_node:
      current_node = self.root
    if current_node.right:
      return self.get_max(current_node.right)
    return current_node
  
  

        

bst = BinarySearchTree('pokemon')
bst.add_node('blastoise')
bst.add_node('wortorle')
bst.add_node('squirtle')

# print(bst.search(squirtle), 'test search')

print(bst.get_min())
print(bst.get_max())



# print(bst.root.right.right)
# print(bst.root.right.left)
# print(bst.root.left.right)