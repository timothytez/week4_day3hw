from node import node

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
    if current_node.nextnode is None: #if after none 1 there is nothing then print none if not continue to next none
        print(None)
        break
    current_node = current_node.next_node