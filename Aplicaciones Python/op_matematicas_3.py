
"""
Elabore un algoritmo que realice las cinco operaciones matemáticas 
entre dos números (+. -, *, /, %)
"""

# INICIO

numero1: float = float(input("Ingrese el primer número: "))
numero2: float = float(input("Ingrese el segundo número: "))

# PROCESO

suma: float = numero1 + numero2
resta: float = numero1 - numero2
multiplicacion: float = numero1 * numero2
division: float = None if numero2 == 0 else numero1 / numero2
modulo: float = None if numero2 == 0 else numero1 % numero2

# SALIDA

print(f"La suma de {numero1} y {numero2} es {suma}")
print(f"La resta de {numero1} y {numero2} es {resta}")
print(f"La multiplicacion de {numero1} y {numero2} es {multiplicacion}")
if division != None:
    print(f"La division de {numero1} y {numero2} es {division}")
    print(f"El modulo de {numero1} y {numero2} es {modulo}")
else:
    print(f"La division y modulo de {numero1} y {numero2} no es posible")