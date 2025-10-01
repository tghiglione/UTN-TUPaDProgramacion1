
import math

""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal. """

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

"""  2. Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”.  Llamar a esta función desde el programa
 principal solicitando el nombre al usuario. """

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los 
 datos al usuario y llamar a esta función con los valores ingresados. """

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal("Tomas", "Ghiglione", 26, "Temperley")

"""  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
que reciba el radio como parámetro y devuelva 
el perímetro del círculo. Solicitar el radio al usuario y llamar 
ambas funciones para mostrar los resultados. """

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = int(input("Ingrese el radio del circulo: "))

print("Area=", calcular_area_circulo(radio))
print("Perimetro=", calcular_perimetro_circulo(radio))

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función. """

def segundos_a_horas(segundos):
    return segundos / 3600

segundos_ingresados = int(input("Ingrese segundos para convertir a horas: "))
print(f"{segundos_ingresados} segundos son {segundos_a_horas(segundos_ingresados)} horas")

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la función. """

def tabla_multiplicar(numero):
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero_tabla_multiplicar = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla_multiplicar)

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los 
resultados de forma clara. """

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)
a = 4
b = 2
print(f"Suma {a} + {b} = {operaciones_basicas(a,b)[0]}\n Resta {a} - {b} = {operaciones_basicas(a,b)[1]}\n Multiplicacion {a} x {b} = {operaciones_basicas(a,b)[2]}\n Division {a} / {b} = {operaciones_basicas(a,b)[3]}")

"""  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
 para mostrar el resultado con dos decimales. """

def calcular_imc(peso, altura):
    return peso / altura**2

peso_usuario = int(input("Ingrese su peso en KG: "))
altura_usuario = float(input("Ingrese su altura en metros: "))
print(f"IMC = {calcular_imc(peso_usuario,altura_usuario)}")

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función. """

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

grados_celsius = int(input("Ingrese temperatura en Celsius: "))
print(f"{grados_celsius} C es equivalente a {celsius_a_fahrenheit(grados_celsius)} F")

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función. """

def calcular_promedio(a, b, c):
    total = a + b + c
    return total / 3

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

print(f"El promedio entre {num1}, {num2} y {num3} es {calcular_promedio(num1,num2,num3)}")