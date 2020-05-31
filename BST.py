class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self, root = None):
        self.root = root

    def insert(self, value):
        if (self.root is None):
            self.root = Node(value)
        else:
            self.insertHelper(self.root, value)

    def search(self, value):
        return self.searchHelper(self.root, value)
    
    def insertHelper(self, current, value):
        if (current.value > value):
            if (current.left is None):
                current.left = Node(value)
            else:
                self.insertHelper(current.left, value)
        else:
            if (current.right is None):
                current.right = Node(value)
            else:
                self.insertHelper(current.right, value)

    def searchHelper(self, current, value):
        if (current is not None):
            if (current.value < value):
                return self.searchHelper(current.right, value)
            elif (current.value > value):
                return self.searchHelper(current.left, value)
            else:
                return True
        else:
            return False
    
def main():
    bst = BST()
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    print(bst.search(1))
    print(bst.search(3))
    print(bst.search(5))
    print(bst.search(7))
    print(bst.search(0))
    bst.insert(7)
    print(bst.search(7))


main()




