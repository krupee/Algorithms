class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# Method to add Nodes to LL
def insert(root, value):
    if (root is None):
        root = Node(value)
    else:
        curr = root
        while (curr.next is not None):
            curr = curr.next
        curr.next = Node(value)
    return root

# Method to print LL
def printLL(root):
    curr = root
    while (curr is not None):
        print(str(curr.val) + " -> ", end = "")
        curr = curr.next
    




# Remove Duplicates
def removeDups(root):
    s = set()
    prev = None
    curr = root
    while (curr is not None):
        if (curr.val in s):
            prev.next = curr.next
            curr = curr.next
        else:
            s.add(curr.val)
            prev = curr
            curr = curr.next
    return root

# Kth to Last
def kthToLast(root, k):
    slow = root
    fast = root
    count = 0
    while (count <= k):
        fast = fast.next
        count = count + 1
    while (fast is not None):
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return root

# Delete Middle Node
def deleteMiddleNode(node):
    node.val = node.next.val
    node.next = node.next.next

# Partition
def partition(root, n):

    return root





def main():
    root = None
    root = insert(root, 1)
    root = insert(root, 1)
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 3)
    root = insert(root, 5)
    
    print("Current State")
    printLL(root)
    print()
    
    print("Remove Dups")
    root = removeDups(root)
    printLL(root)
    print()

    root = insert(root, 7)
    root = insert(root, 9)
    root = insert(root, 11)

    print("Current State")
    printLL(root)
    print()

    print("Kth to Last")
    root = kthToLast(root, 4)
    printLL(root)


main()





    