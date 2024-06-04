import math

"""
Elabore un algoritmo que halle área de 5 figuras
#geométricas y muestre los resultados en forma de
#ecuación
"""

# INICIO

lado: float = float(input("Digite el valor del lado para el área del cuadrado: "))
base: float = float(input("Digite el valor de la base para el área del triangulo, del rectangulo y del paralelogramo: "))
altura: float = float(input("Digite el valor de la altura para el área del triangulo, del rectangulo y del paralelogramo: "))
radio: float = float(input("Digite el valor del radio para el área del circulo: "))

# PROCESO

area_cuadrado: float = lado * lado
area_rectangulo: float = base * altura
area_triangulo: float = base * altura / 2
area_paralelogramo: float = base * altura
area_circunferencia: float = math.pi * radio ** 2

# SALIDA

print(f"\nÁrea cuadrado: {lado} * {lado} = {area_cuadrado}")
print(f"Área rectangulo: {base} * {altura} = {area_rectangulo}")
print(f"Área triangulo: {base} * {altura} / 2 = {area_triangulo}")
print(f"Área paralelogramo: {base} * {altura} = {area_paralelogramo}")
print(f"Área circunferencia: {math.pi} * {radio} * {radio} = {area_circunferencia}")