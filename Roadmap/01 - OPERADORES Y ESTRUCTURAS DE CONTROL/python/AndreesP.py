"""
Operadores
"""

#Operadores aritmeticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Moldulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")


#operadores de comparación

print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")


#Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")
print (f"NOT !: not 10 + 3 === 14 es {not 10 + 3 == 14}")

#Operadores de asginación

my_number = 11 #asignación
print(my_number)
my_number += 1 #Suma y asignación
print(my_number)
my_number -= 1 #SResta y asignación
print(my_number)
my_number *= 1 #Multiplicación y asignación
print(my_number)
my_number /= 1 #División y asignación
print(my_number)
my_number %= 1 #Modulo y asignación
print(my_number)
my_number **= 1 #Exponenete y asignación
print(my_number)
my_number //= 1 #División entera y asignación
print(my_number)

#Operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia

print(f" 'a' in 'andres' ={'a' in 'andres'}")
print(f" 'c' not in 'andres' ={'a'  not in 'andres'}")

#Operadores de bit

a = 10 # 1010
b = 3  # 0013
print(f" AND 10 & 3 = {10 & 3}")
print(f" OR 10 | 3 = {10 | 3}")
print(f" XOR 10 & 3 = {10 ^ 3}")
print(f" NOT ~10  = {~10}")
print(f" desplazamiento a la derecha 10 >>> 2 = {10 >> 2}")
print(f" desplazamiento a la izquierda 10 <<< 2 = {10 << 2}")

"""
Estructuras de control
"""
#Condicionales 

my_string = "Felipe"

if my_string == "Andres":
    print("my_string es 'Andres'")
elif my_string == "Felipe":
    print ("my_string es 'Felipe'")
else:
    print("my_string no es 'Andres'")