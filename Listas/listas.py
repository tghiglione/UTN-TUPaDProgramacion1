""" 1) Crear una lista con las notas de 10 estudiantes. 
• Mostrar la lista completa. 
• Calcular y mostrar el promedio. 
• Indicar la nota más alta y la más baja.  """

notas = [6, 4, 9, 5, 6, 2, 10, 7, 8, 9, 4]
sumatoria = 0
nota_alta = notas[0]
nota_baja = notas[0]

print("notas",notas)

for nota in notas:
    sumatoria += nota
    if nota > nota_alta:
        nota_alta = nota
    elif nota < nota_baja:
        nota_baja = nota

promedio = sumatoria / len(notas)

print("promedio:",promedio)
print("nota mas alta:",nota_alta)
print("nota mas baja:",nota_baja)

""" 2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista. """

productos= []

for i in range(1,6):
    producto = input("Ingrese un producto a la lista: ")
    productos.append(producto)

print(sorted(productos))

eliminar_producto = input("Ingrese producto a eliminar: ")

if(eliminar_producto in productos):
    productos.remove(eliminar_producto)

print(productos)

""" 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista.  """

import random

numeros = []
pares= []
impares= []

for i in range(1,16):
    numeros.append(random.randint(1,100))

for num in range(len(numeros)):
    if numeros[num] % 2 == 0:
        pares.append(numeros[num])
    else:
        impares.append(numeros[num])

print("impares:",impares, "longitud: ",len(impares))
print("pares:",pares,"longitud: ",len(pares))

""" Dada una lista con valores repetidos: 
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado."""

datos = [1,3,5,3,7,1,9,5,3]
nueva_lista = []
for dato in datos:
    if not(dato in nueva_lista):    
        nueva_lista.append(dato)

print(nueva_lista)

""" 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada. """

alumnos = ["Juan", "Pedro", "Matias", "Micaela", "Luna", "Marta", "Pablo", "Gabriela"]

respuesta = int(input("Desea ingresar un usuario o eliminar? 0 para ingresar, 1 para eliminar "))

if respuesta == 0:
    nuevo_alumno = input("Ingrese el nombre del nuevo alumno: ")
    alumnos.append(nuevo_alumno)
elif respuesta == 1:
    eliminar_alumno = input("Ingrese el nombre del alumno a eliminar: ")
    alumnos.remove(eliminar_alumno)
else:
    print("Opcion invalida")

print("Lista actualizada de alumnos:", alumnos)

""" 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
último pasa a ser el primero).  """

numeros = [1,5,6,2,3,8,9]
aux = []
for i in range(len(numeros)):
    indice_final = (len(numeros)-1) - i
    numero_final = numeros[indice_final]
    aux.append(numero_final)

print(aux)

""" 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
semana. 
• Calcular el promedio de las mínimas y el de las máximas. 
• Mostrar en qué día se registró la mayor amplitud térmica. """

temperaturas = [
    [24.4, 25, 26.1, 23.4, 29.3, 30, 27.5],
    [14.2, 13, 16.6, 13.5, 19.8, 10, 15.5]
]
sumatoria_max = 0
sumatoria_min = 0

amplitud = 0
dia = 0

for fila in range(len(temperaturas)):
    for columna in range(len(temperaturas[fila])):
        if fila == 0:
            sumatoria_max += temperaturas[fila][columna]
        elif fila == 1:
            sumatoria_min += temperaturas[fila][columna]

for i in range(len(temperaturas[0])):
    amplitudAux = temperaturas[0][i] - temperaturas[1][i]
    if amplitudAux > amplitud:
        amplitud = amplitudAux
        dia = i + 1
    

promedio_max = sumatoria_max / len(temperaturas[0])
promedio_min = sumatoria_min / len(temperaturas[1])

print("promedio maximas:", promedio_max)
print("promedio minimas:", promedio_min)

print("dia de mayor amplitud:", dia)

""" 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia.  """

notas = [
    [5,6,8],
    [6,2,3],
    [6,3,5],
    [9,8,7],
    [4,8,7]
]

for fila in range(len(notas)):
    sumatoria = 0
    for columna in range(len(notas[fila])):
        sumatoria += notas[fila][columna]
    print("promedio alumno", fila + 1,"=", sumatoria / len(notas[fila]))

for j in range(len(notas[0])):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    print("promedio materia", j + 1, "=", suma / len(notas))

""" 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
• Mostrar el tablero después de cada jugada.  """

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]

]

simbolos = ["X", "O"]
turno = 0
salida = 1

for fila in tablero:
    print(fila)

salida = 1

while salida != 0:
    entrada = input("Jugador " + str(turno + 1) + " (" + simbolos[turno] + "), fila y columna (1-3 1-3) dejando un espacio (ejemplo 2 2): ")
    partes = entrada.split()

    if len(partes) == 2:
        fila = int(partes[0]) - 1
        col = int(partes[1]) - 1

        if fila >= 0 and fila < 3 and col >= 0 and col < 3:
            if tablero[fila][col] == "-":
                tablero[fila][col] = simbolos[turno]

                for fila in tablero:
                    print(fila)

                
                salida = int(input("presione 0 para salir, 1 para continuar"))
                if turno == 0:
                    turno = 1
                else:
                    turno = 0
            else:
                print("Casilla ocupada. Elegí otra.")
        else:
            print("Coordenadas fuera de rango (1 a 3).")
    else:
        print("Formato inválido. Ejemplo: 2 3")

""" 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana.  """

ventas = [
    [10, 11,  9,  8, 15, 11,  7],
    [ 5,  7,  6,  9, 12, 10,  4],
    [ 8,  6,  7, 10, 14,  9,  5],
    [11,  9, 10,  6, 13,  8,  6]
]

totales_productos = []

for i in range(len(ventas)):
    suma = 0
    for j in range(len(ventas[i])):
        suma = suma + ventas[i][j]
    totales_productos.append(suma)
    print("Total producto", i + 1, "=", suma)

totales_dias = []
for j in range(len(ventas[0])):
    suma = 0
    for i in range(len(ventas)):
        suma = suma + ventas[i][j]
    totales_dias.append(suma)

dia_max = 0
max_dia = totales_dias[0]
for j in range(1, len(totales_dias)):
    if totales_dias[j] > max_dia:
        max_dia = totales_dias[j]
        dia_max = j
print("Día con mayores ventas totales: día", dia_max + 1, "con", max_dia)

prod_max = 0
max_prod = totales_productos[0]
for i in range(1, len(totales_productos)):
    if totales_productos[i] > max_prod:
        max_prod = totales_productos[i]
        prod_max = i
print("Producto más vendido en la semana: producto", prod_max + 1, "con", max_prod)
