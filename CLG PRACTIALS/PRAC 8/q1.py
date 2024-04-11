class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def display(self):
        if not self.is_empty():
            print("Stack:", self.items)
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  
print("Peek:", stack.peek()) 
print("Pop:", stack.pop())  
stack.display() 
