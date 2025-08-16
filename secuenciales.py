""" Ejercicio 1 """

print("Hola Mundo!")

""" Ejercicio 2 """

nombre = input("Escriba su nombre: ")
print(f"Hola {nombre}!")

""" Ejercicio 3 """

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = int(input("Escriba su edad: "))
lugarResidencia = input("Escriba el lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

""" Ejercicio 4 """

PI = 3.1415
radio = int(input("Ingrese el radio del circulo: "))
area = PI * radio**2
perimetro = 2*PI*radio
print(f"Area del circulo: {area}")
print(f"Perimetro del circulo: {perimetro}")

""" Ejercicio 5 """

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

""" Ejercicio 6 """

numero = (int(input("Escriba un numero: ")))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

""" Ejercicio 7 """

numero1 = int(input("Ingrese un numero entero distinto de 0: "))
numero2 = int(input("Ingrese otro numero entero distinto de 0: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Resultado Suma: {suma}")
print(f"Resultado Resta: {resta}")
print(f"Resultado Multiplicacion: {multiplicacion}")
print(f"Resultado Division: {division}")

""" Ejercicio 8 """

altura = float(input("Ingrese altura en metros: "))
peso = int(input("Ingrese peso en kg: "))

imc = peso /(altura ** 2)

print(f"Indice masa corporal: {imc}")

""" Ejercicio 9 """

celsius = float(input("Ingrese temperatura en celsius: "))

fahrenheit = 9/5*celsius + 32
print(f"Temperatura en F: {fahrenheit}")

""" Ejercicio 10 """

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio entre {num1}, {num2} y {num3} es: {promedio}")

