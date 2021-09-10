#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv[1:])
    sum = 0
    for i in range(n):
        s = int(argv[i+1])
        sum = sum + s
print(sum)
