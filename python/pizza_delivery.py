#Pizza delivery
print("Welcome to pizza deliveries!")
size = input("What size pizza do you want? S, M or L?\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N\n").upper()


total = 0


if size == 'S':
    total +=  15
elif size == 'M':
    total +=  20
elif size == 'L':
    total +=  25
else:
    total += 25


if add_pepperoni == 'Y' and size == 'S':
    total +=  2

if add_pepperoni == 'Y' and size == 'M' or 'L':
    total += 3


if extra_cheese == 'Y':
    total +=  1

print(f"Your final bill is: ${total}.")