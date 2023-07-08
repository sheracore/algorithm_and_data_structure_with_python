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