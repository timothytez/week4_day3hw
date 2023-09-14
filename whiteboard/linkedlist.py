from Node import Node


#Nodes has two attributes
#value = anything that is a string, integer, or object
#the next = (all nodes have a next attribute to connect to the next node)

class linkedlist:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    #Values

    #"January"
    #"February"
    #"March"
    #"April"
    #"May"
    #"June"
    #"July"
    #"August"
    #"September"
    #"October"
    #"November"
    #"December"

node1 = linkedlist("Jaunary")
node2 = linkedlist("February")
node3 = linkedlist("March")
node4 = linkedlist("April")
node5 = linkedlist("May")
node6 = linkedlist("June")
node7 = linkedlist("July")
node8 = linkedlist("August")
node9 = linkedlist("September")
node10 = linkedlist("October")
node11 = linkedlist("November")
node12 = linkedlist("December")


node1.next_node = node2   #this shows that node 1 is connected to node 2...
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5
node5.next_node = node6
node6.next_node = node7
node7.next_node = node8
node8.next_node = node9
node9.next_node = node10
node10.next_node = node11
node11.next_node = node12

current_node = node1
while True:
    print (current_node.value, "-->")
    if current_node.value is None: 
#if after node 1 there is nothing then print none if not continue to next none
        break
        
    current_node = current_node.next_node

    def printlinkedlist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.nextnode
    print(None)



#     public class LinkedList { --------- this is the class inwhich your are making your synax about




#   Node head;                ---------------- this is your starter point and first node
#   public void append(int data) {  ------------ here is where your add or insert your data to create you node
#     if (head == null) {       --------------- if the head or the starting point comes to an end or nothing else to report you move on to the next node
#       head = new Node(data);   ------------- the head now becomes a new node and your starting point. lets say it went from A to B. Now the starting point is B going to C.
#       return;
#     }
#     Node current = head;
#     while (current.next != null) {    ----------- over all the cycle continues until there is n more data or we have reached our end.
#       current = current.next;
#       }
#     current.next = new Node(data);
#   }
# }




class linkedlist_pokemon:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    