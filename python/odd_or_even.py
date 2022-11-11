#Odd or Even
number = int(input("Which number you want to check? "))

remainder = number % 2

if remainder == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
