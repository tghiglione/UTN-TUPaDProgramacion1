"""1) Añadir las siguientes frutas con sus respectivos precios al diccionario precios_frutas:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
print("----------------------\n")

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Actualizado: \n",precios_frutas)
print("----------------------\n")

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios """

listado_frutas= []

for fruta in precios_frutas:
    listado_frutas.append(fruta)

print("Listado de frutas: \n",listado_frutas)
print("----------------------\n")

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe. """


contactos_telefonicos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto a guardar: ")
    numero = int(input("Ingrese el numero telefonico del contacto: "))
    if nombre in contactos_telefonicos:
        print(f"Contacto {nombre} actualizado")
    contactos_telefonicos[nombre] = numero

contacto_buscado = input("\nIngrese el nombre del contacto a buscar: ").strip()

if contacto_buscado in contactos_telefonicos:
    print(f"\nEl numero telefonico de {contacto_buscado} es {contactos_telefonicos[contacto_buscado]}")
else:
    print("\nNo existe el contacto en el listado")

print("----------------------\n")


""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra """

frase = input("Ingrese una frase: ")

listado_palabras = frase.split(" ")
set_palabras = set(listado_palabras)

recuento_palabras = {}

for palabra in listado_palabras:
    if palabra not in recuento_palabras:
        recuento_palabras[palabra] = 1
    else:
        recuento_palabras[palabra] += 1

print("Palabras sin repetir: \n", set_palabras)
print("----------------------\n")
print("Recuento de palabras repetidas: \n", recuento_palabras)
print("----------------------\n")

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. """

alumnos = {}

for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    nota1 = int(input("Ingrese la primer nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercer nota: "))
    notas = (nota1,nota2,nota3)
    if alumno in alumnos:
        print(f"Notas del alumno {alumno} actualizadas.\n")
    alumnos[alumno] = notas

for alumno in alumnos:
    notas = alumnos[alumno]
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno} = {promedio}")

print("----------------------\n")

""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

aprobados_parcial1  = {1, 2, 3, 4, 5, 6} #alumnos 1 2 3 4 5 6
aprobados_parcial2 = {4, 5, 6, 7, 8, 9} #alumnos 4 5 6 7 8 9

aprobaron_ambos = aprobados_parcial1 & aprobados_parcial2 
print("Estudiantes que aprobaron ambos parciales:", aprobaron_ambos)

aprobaron_solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Estudiantes que aprobaron solo uno de los dos:", aprobaron_solo_uno)

aprobaron_al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("Estudiantes que aprobaron al menos un parcial:", aprobaron_al_menos_uno)

print("----------------------\n")

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. """

productos = {"Remera": 1, "Buzo": 2}

entrada = 1

while entrada != 0:
    opcion = int(input(" 1)Consultar el stock de un producto\n 2)Agregar unidades al stock del producto\n 3)Agregar un nuevo producto\n"))

    match opcion:
        case 1:
            producto_buscado = input("Ingrese nombre del producto buscado: ").capitalize()
            producto_stock = productos[producto_buscado]
            print(f'Stock de {producto_buscado} = {producto_stock}')
        case 2:
            producto_agregado = input("Ingrese nombre del producto para agregar stock: ").capitalize()
            if producto_agregado not in productos:
                print("No existe el producto!")
            else:
                stock_nuevo = int(input("Ingrese cantidad de unidades para agregar: "))
                productos[producto_agregado] += stock_nuevo
        case 3:
            nuevo_producto = input("Ingrese nombre del nuevo producto: ").capitalize()
            if nuevo_producto in productos:
                print("El producto ya se encuentra!")
            else:
                cantidad_unidades = int(input("Ingrese cantidad de unidades para agregar: "))
                productos[nuevo_producto] = cantidad_unidades
        case _:
            print("Opcion no valida!\n")

    print(productos)
    entrada = int(input("Ingrese 0 para salir o cualquier digito para continuar. \n"))

print("----------------------\n")


""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos """

agenda = {}

entrada = 1
while entrada != 0:
    dia = input("Ingrese dia del evento (dd/mm/yyyy): ")
    hora = input("Ingrese hora del evento (hh:mm): ")
    evento = input("Ingrese el evento: ")
    fecha = (dia,hora)
    if fecha in agenda:
        print("Dia ocupado!")
    else:
        agenda[fecha] = evento
    entrada =int(input("Ingrese 0 para salir o cualquier otro digito para continuar: "))

print("Agenda: \n",agenda)
print("----------------------\n")

""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores """

capitales_original = {"Francia": "Paris", "Italia": "Roma", "Portugal": "Lisboa"}
capitales_invertido = {}

for capital in capitales_original:
    ciudad = capitales_original[capital]
    capitales_invertido[ciudad] = capital


print("Original: \n",capitales_original)
print("Invertido: \n",capitales_invertido)






