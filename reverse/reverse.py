"""
reverse the contents of the list using recursion, *not a loop.*

For example,
```
1->2->3->None
```
would become...
```
3->2->1->None
```

# CORRECITON: Loops are okay. Recursion is optional.

"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    # use recursion (optional) to reverse a singly-linked list
    # refer to "problem_visualization.jpg" for a visualization of the problem
    def reverse_list(self, node, prev):
        
        # check to see if list is empty
        if self.head == None:
            return

        # if the next node is None, we have reached the end of the list (base case)
        # assign head to this node and set its pointer to the previous node (reverse pointer direction)
        elif node.next_node == None:
            self.head = node
            node.set_next(prev)

            return self

        # If we are not at the base case
        else:
            # Get the next node.  This will become the "current" node
            next = node.next_node
            
            # Reverse the direction of the current node's pointer
            node.next_node = prev

            # Recursively call reverse_list
            # Input the "next" node as the current node and the current node as the previous
            # This will let us reverse the pointer between them and move us closer to the tail (base case)
            self.reverse_list(next, node)
