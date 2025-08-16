
# Queue
# FIFO
# Dequeue(), Eneuquq(), front(), rear() - all O(1)

# Deque is preferred for Queue implementation for O(1) append and pop operations compared to list O(n).

from collections import deque


queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

print("Dequed item: ")
print(queue.popleft())

print(queue)


# queue.Queue(maxsize) initializes a variable to max size. maxsize of 0 is infinite queue. This Queue follows the FIFO rule.
from queue import Queue

queue = Queue()

print(queue.qsize())

queue.put(1)
queue.put(2)
queue.put(3)

print(queue)

print(queue.get())
print(queue.get())

print(queue)

print(queue.empty())

print(queue.get())
print(queue.empty())

print(queue.full())




