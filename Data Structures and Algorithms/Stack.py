# Stack
# LIFO
# Primary Operations: pop(), push()
# Auxiliary Operations: peek()/top(), isEmpty(), isFull()
# Implementation: Array or Linked List
# Used to solve popular problems like Next Greater, Previous Greater, Next Smaller, Previous Smaller, Largest Area in a Histogram and Stock Span Problems.


from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack")
print(stack)

print("Elements popped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack after elements have been removed")
print(stack)


