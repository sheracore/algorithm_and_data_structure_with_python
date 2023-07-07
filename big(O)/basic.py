# -------------------------- Time complexity _________________________

def o_3():
    """ O(3) because three time printed """
    print('one')
    print('two')
    print('three')


def o_n(n: list):
    """ O( n + n + 2) == O(n) == Linear """
    print("Hello")  # O(1)
    for i in n:  # O(n)
        print(i)
    for i in n:  # O(n)
        print(i)
    print("Hello again")


def o_n2(n: list):
    """ O( n + n^2( n * n ) + 2) == O(n^2) == Quadratic """
    print("Hello")  # O(1)
    for i in n:  # O(n)
        print(i)
    for i in n:  # O(n * n)
        for j in n:  # O(n)
            print(i, j)
    print("Hello again")


def o_n3(n: list):
    """ O( n + n^3( n * n * n ) + 2) == O(n^3) far slower than O(n^2) far slower than O(n)"""
    print("Hello")  # O(1)
    for i in n:  # O(n)
        print(i)
    for i in n:  # O(n * n * n)
        for j in n:  # O(n * n)
            for z in n:  # O(n)
                print(i, j, z)
    print("Hello again")


# -------------------------- Space complexity _________________________


def space_o_n(n):
    """O(n): It will allocate n space in memory so than it will be O(n)"""
    l = [i for i in range(n)]
    return l
