#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv[1:])
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    for i in range(n):
        s = sys.argv[i+1]
        print("{}: {}".format(i+1, s))
