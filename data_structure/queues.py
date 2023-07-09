# ------------------------------------------- python builtin queue 1 ---------------------------------------------
import queue

# Create a queue
my_queue = queue.Queue()

# Enqueue elements
my_queue.put(10)
my_queue.put(20)
my_queue.put(30)

# Dequeue elements
print(my_queue.get())  # Output: 10
print(my_queue.get())  # Output: 20

# Checking if the queue is empty
if my_queue.empty():
    print("Queue is empty.")

# Get the size of the queue
print(my_queue.qsize())  # Output: 1

# Peek at the front element of the queue without removing it
print(my_queue.queue[0])  # Output: 30


# ------------------------------------------- python builtin queue 2 ---------------------------------------------
from collections import deque

# Create an empty queue
deque_queue = deque()

# Enqueue elements
deque_queue.append(10)
deque_queue.append(20)
deque_queue.append(30)

# Dequeue elements
item = deque_queue.popleft()
print(item)  # Output: 10

item = deque_queue.popleft()
print(item)  # Output: 20

# Check if the queue is empty
if not deque_queue:
    print("Queue is empty")

# Enqueue more elements
deque_queue.append(40)
deque_queue.append(50)

# Get the size of the queue
size = len(deque_queue)
print("Size of the queue:", size)

# Iterate over the queue
for item in deque_queue:
    print(item)

# ------------------------------------ Usefull functions ------------------------------------


def reverse_queue(my_queue: type(queue)):
    stack = list()
    while not my_queue.empty():
        item = my_queue.get()
        stack.append(item)
    while stack:
        my_queue.put(stack.pop())
    return my_queue


r_queue = queue.Queue()
r_queue.put(10)
r_queue.put(20)
r_queue.put(30)
r_queue.put(40)
reverse_queue(r_queue)
print("Here")


# __________________________________________ Implement Queue ______________________________________
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)  # pop(0) means pop from left

    def size(self):
        return len(self.queue)


class QueueUsingTwoStack:
    """ O(n), this queue implemented by stack: Interview question """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return not (self.stack1 or self.stack2)

    def enqueue(self, item):
        """ O(1) """
        self.stack1.append(item)

    def dequeue(self):
        """ O(n) """
        if self.is_empty():
            raise IndexError("Queue is empty")
        self._sync_queue()
        return self.stack2.pop()

    def peek(self):
        """ O(n) """
        if self.is_empty():
            raise IndexError("Queue is empty")
        self._sync_queue()
        return self.stack2[-1]

    def _sync_queue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


my_stack = QueueUsingTwoStack()
my_stack.enqueue(10)
my_stack.enqueue(20)
my_stack.enqueue(30)
my_stack.dequeue()
my_stack.dequeue()
my_stack.dequeue()
print('Here')


# --------------------------------------- Priority Queue -------------------------------------------

"""
Heap data structure is mainly used to represent a priority queue. In Python, it is available using the “heapq” module. 
The property of this data structure in Python is that each time the smallest heap element is popped(min-heap). 
Whenever elements are pushed or popped, heap structure is maintained. 
"""

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))


class PriorityHeapQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def is_empty(self):
        return len(self._queue) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self._queue)[-1]
        raise IndexError("Priority queue is empty")

# Example usage:
pq = PriorityHeapQueue()
pq.enqueue('Task 1', 3)
pq.enqueue('Task 2', 1)
pq.enqueue('Task 3', 2)

while not pq.is_empty():
    print(pq.dequeue())


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def enqueue(self, item, priority):
        self._queue.append((item, priority))

    def dequeue(self):
        if not self.is_empty():
            highest_priority = min(self._queue, key=lambda x: x[1])
            self._queue.remove(highest_priority)
            return highest_priority[0]
        raise IndexError("Priority queue is empty")

# Example usage:
pq = PriorityQueue()
pq.enqueue('Task 1', 3)
pq.enqueue('Task 2', 1)
pq.enqueue('Task 3', 2)

while not pq.is_empty():
    print(pq.dequeue())