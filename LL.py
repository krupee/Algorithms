class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, root = None):
        self.root = root

    def insert(self, new_node):
        current = self.root
        if (self.root is not None):
            while (current.next is not None):
                current = current.next
            current.next = new_node
        else:
            self.root = new_node

    def insertAtPosition(self, position, new_node):
        if (position == 1):
            new_node.next = self.root
            self.root = new_node
        else:
            current = self.root
            count = 1
            while (current is not None and count < position):
                if (count == position - 1):
                    new_node.next= current.next
                    current.next = new_node
                current = current.next
                count = count + 1

    def deleteValue(self, value):
        current = self.root
        prev = None
        while (value != current.value and current.next is not None):
            prev = current
            current = current.next
        if (value == current.value):
            if (prev is None):
                self.root = current.next
            else:
                prev.next = current.next


    def printList(self):
        current = self.root
        while (current is not None):
            print(str(current.value) + " -> ", end = "")
            current = current.next
        print()

    # Methods for Stack Implementation

    def deleteAndReturnFront(self):
        current = self.root
        if (current is not None):
            temp_node = current.next
            self.root = temp_node
            return current
        return None

    
    def insertIntoFront(self, new_node):
        new_node.next = self.root
        self.root = new_node



def main():
    LL = LinkedList()
    
    LL.insert(Node(1))
    LL.insert(Node(3))
    LL.insert(Node(5))
    
    LL.printList()
    
    LL.insertAtPosition(2, Node(2))
    LL.printList()
    
    LL.insertAtPosition(4, Node(4))
    LL.printList()
    
    LL.insertAtPosition(6, Node(6))
    LL.printList()

    LL.deleteValue(1)
    LL.printList()

    LL.deleteValue(3)
    LL.printList()

    LL.deleteValue(6)
    LL.printList()



#main()