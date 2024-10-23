class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)
        return f"{str(e)} is successfully pushed into stack".upper()

    def pop(self):
        if not self.is_empty():
            removed_item = self.items.pop()
            return f"{removed_item} is successfully removed from stack"
        else:
            return 'Stack is Empty'

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is Empty'

    def length(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
