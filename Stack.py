from LL import LinkedList, Node

class Stack():
    def __init__(self, top = None):
        self.LL = LinkedList()

    def pop(self):
        value = self.LL.deleteAndReturnFront()
        return value

    def push(self, new_node):
        self.LL.insertIntoFront(new_node)


def main():
    stack = Stack()

    stack.LL.printList()

    stack.push(Node(1))
    stack.push(Node(3))
    stack.push(Node(5))

    stack.LL.printList()

    stack.pop()

    stack.LL.printList()

main()

