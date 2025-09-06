import random

""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """

for num in range(101):
    print(num)

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """

numero = int(input("Ingrese un numero: "))
cant_digitos = 0

while numero > 0:
    cant_digitos += 1
    numero = numero // 10

print("Cantidad de digitos:", cant_digitos)

""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. """

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
sumatoria = 0

for i in range(num1 + 1, num2):
    sumatoria += i

print(f"La sumatoria de los numeros comprendidos entre {num1} y {num2} es {sumatoria}")

""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0. """

num = int(input("Ingrese un numero, 0 para salir del programa: "))
sumatoria = 0

while num != 0:
    sumatoria += num 
    num = int(input("Ingrese un numero, 0 para salir del programa: "))

print("La sumatoria de numeros es:", sumatoria)

""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """

NUMERO_ALEATORIO = random.randint(0,9)

num = int(input("Adivine el numero entre 0 y 9: "))
intentos = 1

while num != NUMERO_ALEATORIO:
    intentos += 1
    num = int(input("Adivine el numero entre 0 y 9: "))

print("Acertaste! Cantidad de intentos:", intentos)

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente """

for num in range(100, -1, -2):
    print(num)

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario. """

num = int(input("Ingrese un numero entero positivo: "))
sumatoria = 0
if num <=0:
    print("No ingreso un numero positivo!")
else:
    for i in range(0,num + 1):
        sumatoria += i
    print(f"La sumatoria entre 0 y {num} es {sumatoria}")

""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """

TOPE = 100
cant_numeros = 0

cant_pares = 0
cant_impares = 0
cant_negativos = 0
cant_positivos = 0

while cant_numeros != TOPE:
    num = int(input("Ingrese un numero: "))
    if num < 0:
        cant_negativos += 1
    else:
        cant_positivos += 1
    
    if num % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1

    cant_numeros += 1

print(f"\nCantidad de pares: {cant_pares}\nCantidad de impares: {cant_impares}\nCantidad de negativos: {cant_negativos} \nCantidad de positivos: {cant_positivos}")

""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor). """

TOPE = 100
sumatoria = 0
for i in range(1, TOPE + 1):
    num = int(input("Ingrese un numero: "))
    sumatoria += num
media= sumatoria / TOPE

print("media:",media)

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """

numero = int(input("Ingrese un numero: "))
numero_formado= ""
while numero > 0:
    digito = numero % 10
    numero_formado = numero_formado + str(digito)
    numero = numero // 10

print(f"Numero al reves {numero_formado}")
