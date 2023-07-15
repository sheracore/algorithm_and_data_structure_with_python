"""
Insert O(1)
Lookup: O(1)
Delete: O(1)
"""

"""
Question1: Find first non repeated character in the text
e.g. an apple green l: A->2: No , p->2: No, l->1 Yes(Found)
"""


def non_reapeated_char(text):
    """ If you iterate twice on it, you will get O(n^2) but by dict it will be O(n) """
    d = dict()
    text = text.replace(" ", "")
    for ch in text:
        if ch not in d.keys():
            d[ch] = 1
        else:
            d[ch] += 1
    for key, value in d.items():
        if value == 1:
            return key
    return "All chars are repeated"

char = non_reapeated_char("fan apple ggrreen l")
print(char)
