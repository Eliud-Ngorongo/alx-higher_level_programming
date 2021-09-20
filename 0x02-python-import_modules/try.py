#!/usr/bin/python3
numbers = [1, 2, 5, 67, 90]
print(len(numbers))

A = "10"
print(A)
number = int(input("Enter number:"))
quotient = number / 16
if quotient == 10:
    hex = 'A'
    print(hex)
elif quotient == 11:
    hex = 'B'
    print(hex)
elif quotient == 12:
    hex = 'C'
    print(hex)  
elif quotient == 13:
    hex = 'D'
    print(hex)
elif quotient == 14:
    hex = 'E' 
    print(hex) 
elif quotient == 15:
    hex = 'F'
    print(hex)
else:
    hex = quotient
    print ("{:.0f}".format(hex))     
                    

