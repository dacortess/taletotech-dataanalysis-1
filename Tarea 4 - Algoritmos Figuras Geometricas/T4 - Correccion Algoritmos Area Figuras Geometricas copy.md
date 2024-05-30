# Algoritmo Area de Figuras Geometricas

### **Estudiante:** David Camilo Cortes Salazar

## Algoritmo

**Entradas**

lado, base, altura, radio

**Pasos**

```
INICIO

//las siguientes variables guardan el valor del lado, base, altura y radio de las figuras geométricas

Entradas

Escribir: “Digite el valor del lado para el área cuadrado: ”
Leer lado
Escribir: “Digite el valor de la base para hallar el área del triángulo, del rectángulo y del paralelogramo: ”
Leer base
Escribir: “Digite el valor de la altura para hallar el área del triángulo, del rectángulo y del paralelogramo: ”
Leer altura
Escribir: “Digite el valor del radio para hallar el área del círculo: ”
Leer radio

PROCESOS

area_cuadrado = lado * lado
area_rectangulo = base * altura
area_triangulo = base * altura / 2
area_paralegramo = base * altura
area_circunferencia = PI * r * r 

SALIDA

Escribir: “Área Cuadrado:” + lado + “*” + lado + “=” + area_cuadrado  
Escribir: “Área Rectangulo:” + base + “*” + altura + “=” + area_rectangulo
Escribir: “Área Triangulo:” + base + “*” + altura + “/ 2” + “=” + area_triangulo  
Escribir: “Área Paralelogramo:” + base + “*” + altura + “=” + area_paralelogramo
Escribir: “Área Circunferencia:” + "PI" + “*” + radio + “*” + radio + “=” + area_circunferencia

FIN
```
