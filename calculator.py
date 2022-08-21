#Simple calculator
import time
a = float(input("Enter number 1:  "))
b = float(input("Enter number 2:  "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print()

print("...Calculating...")
print(".................")
time.sleep(1.5)
print("Addition: " ,round(addition,2))
time.sleep(1.5)
print("Subtraction: ", round(subtraction,2))
time.sleep(1.5)
print("Multiplication: ", round(multiplication,2))
time.sleep(1.5)
print("Division: ", round(division,2))
time.sleep(1.5)
print()
