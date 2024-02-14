
# 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack = self.stack[::-1]
        output = self.stack.pop()
        self.stack = self.stack[::-1]

        return output

    def peek(self):
        return self.stack[0]

    def empty(self):
        if self.stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Testing
myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek()  # return 1
myQueue.pop()  # return 1, queue is [2]
myQueue.empty()  # return false
