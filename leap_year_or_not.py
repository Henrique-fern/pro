#Leap Year or Not
year = int(input("Which year do you want to check?"))

remainder1 = year % 4
remainder2 = year % 100
remainder3 = year % 400

if remainder1 == 0:
    if remainder2 == 0:
        if remainder3 == 0:
                print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")        
else:
    print(f"{year} is not a leap year.")