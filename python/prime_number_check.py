#Prime number Check

n = int(input("What number do you want to check?\n"))


def prime_checker(number):
    for i in range(2, number): 
            if number % i == 0:
                return False
    return True
    
if n > 2:
    if prime_checker(n):
        print("It's a prime number")
    else:
        print("It's not a prime number")
else:
    print(f"{n} isn't a valid number")


