#calculadora basica
import time
a = float(input("Ingrese numero 1:  "))
b = float(input("Ingrese numero 2:  "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print()

print("...Calculando...")
print("................")
time.sleep(1.5)
print("suma" ,round(suma,2))
time.sleep(1.5)
print("resta", round(resta,2))
time.sleep(1.5)
print("multiplicacion", round(multiplicacion,2))
time.sleep(1.5)
print("division", round(division,2))
print()