#!/usr/bin/python3
# Import a simple function from a simple file
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
