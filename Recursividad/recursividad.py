"""1- Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario """

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero_factorial = int(input("Ingrese un número entero: "))

print(f"\nFactoriales desde 1 hasta {numero_factorial}:\n")

for i in range(1, numero_factorial + 1):
    print(f"{i}! = {factorial(i)}")

""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición hasta la cual desea mostrar la serie de Fibonacci: "))

print(f"\nSerie de Fibonacci hasta la posición {posicion}:\n")

for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")


""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente. Prueba esta función en un algoritmo general. """

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

resultado = potencia(base, exponente)

print(f"\n{base} elevado a la {exponente} es: {resultado}")

""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero_dec_a_bin = int(input("Ingrese un número entero positivo en base decimal: "))

if numero_dec_a_bin < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    binario = decimal_a_binario(numero_dec_a_bin)
    print(f"\nEl número {numero_dec_a_bin} en binario es: {binario}")

""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es. """

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"\n'{texto}' es un palíndromo.")
else:
    print(f"\n'{texto}' no es un palíndromo.")

""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos. """

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"\nLa suma de los dígitos de {numero} es: {resultado}")

""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide """

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_inferior = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

if nivel_inferior <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"\nPara construir una pirámide con {nivel_inferior} bloques en la base, se necesitan {total} bloques en total.")

""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número. """

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


numero_a_contar = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0 a 9): "))

if numero_a_contar < 0 or digito < 0 or digito > 9:
    print("Por favor, ingrese valores válidos (número positivo y dígito entre 0 y 9).")
else:
    cantidad = contar_digito(numero_a_contar, digito)
    print(f"\nEl dígito {digito} aparece {cantidad} veces en el número {numero_a_contar}.")