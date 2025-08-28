from statistics import mode, median, mean 
import random 

""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

edad = int(input("Ingrese su edad: ")) #pido la edad del usuario

if edad >= 18:
    print("Es mayor de edad")           #si es mayor o igual que 18 imprimo que es mayor

""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”. """

nota = int(input("Ingrese su nota: ")) #pido la nota del usuario

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". """

numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. """

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")
else:
    print("Ingrese una edad valida")

""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string.  """

password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud_password = len(password)       #guardo en una variable la longitud de la contraseña

if longitud_password >= 8 and longitud_password <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

""" Escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.  """

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #lista de 50 numeros entre 1 y 100

media= mean(numeros_aleatorios)
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)

if media > mediana and mediana > moda:  # Sesgo positivo: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
    print("Sesgo positivo")
elif media < mediana and mediana < moda: #Sesgo negativo: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda
    print("Sesgo negativo")
elif mediana == media == moda:          #Sin sesgo: cuando la media, la mediana y la moda son iguales. 
    print("Sin sesgo")
else:
    print("No cumple ninguna")

""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.  """

frase = input("Ingrese una palabra o frase: ")

ultima_letra = frase[len(frase) - 1] #tomo la ultima letra de la frase con la longitud de la frase - 1 para la ultima posicion
LETRA_A = "a"                        #constantes con las vocales
LETRA_E = "e"
LETRA_I = "i"
LETRA_O = "o"
LETRA_U = "u"


if ultima_letra == LETRA_A or ultima_letra == LETRA_E or ultima_letra == LETRA_I or ultima_letra == LETRA_O or ultima_letra == LETRA_U: #chequeo si la ultima letra es alguna vocal
    frase = frase + "!"

print(frase)

""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. """

nombre = input("Ingrese su nombre: ")
menu =int(input("Ingrese: " \
"1. Si quiere su nombre en mayúsculas " \
"2. Si quiere su nombre en minúsculas " \
"3. Si quiere su nombre con la primera letra mayúscula: "))  #menu de opciones

if menu == 1:
    nombre = nombre.upper()
elif menu == 2:
    nombre = nombre.lower()
elif menu == 3:
    nombre = nombre.title()
else:
    print("Opcion inexistente")

print(nombre)

""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).  """

magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto >= 0 and magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Magnitud incorrecta")

"""10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. """

hemisferio = input("Ingrese en el hemisferio que se encuentra (N para NORTE y S para SUR): ").upper()   #pido el hemisferio y lo convierto en mayuscula para comparar luego
mes = input("Ingrese mes del año que se encuentra: ").lower()       #pido el mes y lo convierto a minuscula para comparar luego
dia = int(input("Ingrese el dia en el que se encuentra: "))

#listado de meses para comparar
ENERO = "enero"
FEBRERO = "febrero"
MARZO = "marzo"
ABRIL = "abril"
MAYO = "mayo"
JUNIO = "junio"
JULIO = "julio"
AGOSTO = "agosto"
SEPTIEMBRE = "septiembre"
OCTUBRE = "octubre"
NOVIEMBRE = "noviembre"
DICIEMBRE = "diciembre"

if hemisferio == "N":
    if (dia >= 21 and mes == DICIEMBRE) or mes == ENERO or mes == FEBRERO or (dia < 21 and mes == MARZO):
        print("Invierno")
    elif (dia >= 21 and mes == MARZO) or mes == ABRIL or mes == MAYO or (dia < 21 and mes == JUNIO):
        print("Primavera")
    elif (dia >= 21 and mes == JUNIO) or mes == JULIO or mes == AGOSTO or (dia < 21 and mes == SEPTIEMBRE):
        print("Verano")
    elif (dia >= 21 and mes == SEPTIEMBRE) or mes == OCTUBRE or mes == NOVIEMBRE or (dia < 21 and mes == DICIEMBRE):
        print("Otoño")
elif hemisferio == "S":
    if (dia >= 21 and mes == DICIEMBRE) or mes == ENERO or mes == FEBRERO or (dia < 21 and mes == MARZO):
        print("Verano")
    elif (dia >= 21 and mes == MARZO) or mes == ABRIL or mes == MAYO or (dia < 21 and mes == JUNIO):
        print("Otoño")
    elif (dia >= 21 and mes == JUNIO) or mes == JULIO or mes == AGOSTO or (dia < 21 and mes == SEPTIEMBRE):
        print("Invierno")
    elif (dia >= 21 and mes == SEPTIEMBRE) or mes == OCTUBRE or mes == NOVIEMBRE or (dia < 21 and mes == DICIEMBRE):
        print("Primavera")
else:
    print("Opcion invalida")