from apsstack import Stack

# Create a stack instance
stack = Stack()

# Push items onto the stack
print(stack.push(10))
print(stack.push(20))

# Peek at the top item
print(stack.peek())

# Pop an item from the stack
print(stack.pop())

# Check the length of the stack
print(stack.length())

# Try popping from an empty stack
print(stack.pop())

