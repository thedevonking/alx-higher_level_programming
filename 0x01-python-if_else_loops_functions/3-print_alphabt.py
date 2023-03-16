#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c != ord('c') and c != ord('q'):
        print("{:c}".format(c), end=" ")
