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


def string_reverser(string: str) -> str:
    reverse = ''
    str_stack = [s for s in string]
    while str_stack:
        reverse += str_stack.pop()
    return reverse


result = string_reverser("abcd")
print(result)


expression_dict = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}


def expression(string: str):
    # Edge cases: ( , ((), ()), ), )(, {], <>},
    e_stack = list()
    for s in string:
        if s in expression_dict.keys():
            e_stack.append(s)
        if s in expression_dict.values():
            if not e_stack:
                return False
            top = e_stack.pop()
            if expression_dict.get(top) != s:
                return False
    return not bool(e_stack)


is_correct = expression('( 1 + 3 )')
print("here, ", is_correct)
