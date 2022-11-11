#Tip Calculator
print ("Welcome to the tip calculator")

x = float(input("What was the total bill? $"))

y = int(input("How many people to split the bill? "))

z = int(input("What percentage tip would you like to give? 10, 12 or 15? "))



percentagem_tip = z / 100
total_tip = x * percentagem_tip

conta_total = total_tip + x

conta_para_cada_um = conta_total / y


print(round(conta_para_cada_um, 1))
