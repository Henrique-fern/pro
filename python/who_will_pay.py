#Banker Roulette, Who will pay?
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_choice = random.randint(0, len(names) - 1)

last_buyer = names[random_choice]

#last_buyer = random.choice(names)

print(f"{last_buyer} is going to pay today!")


