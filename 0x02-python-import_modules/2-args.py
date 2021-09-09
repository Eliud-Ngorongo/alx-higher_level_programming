#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = (len(sys.argv[1:]))
    if n <= 0:
        print("{} arguments.".format(n))
    else:
        if n == 1:
            print("{} argument:".format(n))
            print("{}: {}".format(n, sys.argv[1]))
        else:
            print("{} arguments:".format(n))
            for i in range(n):
                s = sys.argv[i+1] 
                print("{}: {}".format(i+1, s))