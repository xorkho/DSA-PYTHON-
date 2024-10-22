class Stack:
    def __init__(self, max_size=-1):
        self.stack = []
        self.max_size = max_size  # max_size = -1 means unlimited size
        self.tos = -1  # Top of Stack initialized to -1 (indicating empty)

    # Check if the stack is empty
    def is_empty(self):
        return self.tos == -1

    # Check if the stack is full (only if max_size is not -1)
    def is_full(self):
        if self.max_size == -1:  # Unlimited size
            return False
        return self.tos + 1 == self.max_size

    # Push an element onto the stack
    def push(self, item):
        if self.is_full():
            print("Stack is full! Cannot push element:", item)
        else:
            self.stack.append(item)
            self.tos += 1  

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            popped_item = self.stack.pop()
            self.tos -= 1  
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        return self.stack[self.tos]

    def size(self):
        return self.tos + 1  
    
    def display(self):
        print("Stack (top -> bottom):", self.stack)

# s=Stack(5)
# s.push(5)
# s.display()
# # print(s.is_full())
# s.pop()
# print(s.is_empty())
# s.pop()
# print(s.size())