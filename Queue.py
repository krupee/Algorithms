class Queue():
    def __init__(self, data = []):
        self.data = []

    def pop(self):
        return self.data.pop(0)

    def push(self, new_value):
        self.data.append(new_value)
    
    def peek(self):
        print("Peek: ", self.data[0])


def main():
    print("Queue Testing")
    
    q = Queue()

    print(q.data)

    q.push(1)
    q.push(3)
    q.push(5)

    print(q.data)

    q.pop()
    q.pop()

    print(q.data)

main()

