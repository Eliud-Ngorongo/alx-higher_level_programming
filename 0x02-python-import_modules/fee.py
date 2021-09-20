fee = 4535
discount = 0.1
first_payment = int(fee * discount)
balance = int(fee- first_payment)

print("You should pay ${} and the balance will be ${}".format(first_payment, balance))


# 1 kilometer = 0.621371 miles


kilometer = float(input("Enter the miles you want:"))
kilometer *= (0.621371)
print((kilometer))
