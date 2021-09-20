#!/usr/bin/python3
if __name__ == "__main__":    
    from calculator_1 import mul, sub, add, div
    from sys import argv
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = argv[2]
    funcs = {"*": mul, "+": add, "-": sub, "/": div}
    if ops not in list(funcs.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
print("{} {} {} = {}".format(a, ops, b, funcs[ops](a, b)))



# so this is a comment as long as I never get to that new line character. The above program does simple arithmentic from the CLI and returns the desire results
'''So this is also a comment
 as long is its not a docstring'''

