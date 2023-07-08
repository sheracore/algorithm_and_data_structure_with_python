""" In python you can create stack by list """
stack = []

# Pushing elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

# Popping elements from the stack
print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20

# Checking if the stack is empty
if not stack:
    print("Stack is empty.")

# Peek at the top element of the stack without removing it
print(stack[-1])  # Output: 10

# ------------------------------- Reverse String -------------------------------------------


def string_reverser(str: str) -> str:
    reverse = ''
    str_stack = [s for s in str]
    while str_stack:
        reverse += str_stack.pop()
    return reverse


result = string_reverser("abcd")
print(result)
