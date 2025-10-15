""" 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad """

""" 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato """

with open("./Archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}| Precio: ${precio}| Cantidad: {cantidad}")

""" 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente. """

producto = input("Ingrese un producto: ")
precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))


with open("./Archivos/productos.txt", "a") as archivo:
    archivo.write(f"\n{producto},{precio},{cantidad}")

""" 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad. """

productos= []

with open("./Archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": int(precio),
            "cantidad": int(cantidad),
        }
        productos.append(producto)

""" 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error. """

nombreBuscado = input("\nIngrese nombre del producto a buscar: ")
productoEncontrado = False
i=0
while(i < len(productos) and not productoEncontrado):
    prod = productos[i]
    if(prod['nombre'] == nombreBuscado):
        print(f"\nProducto: {prod['nombre']}| Precio: ${prod['precio']}| Cantidad: {prod['cantidad']}\n")
        productoEncontrado = True
    i += 1

if not productoEncontrado:
    print("No existe el producto en la lista")


""" 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista. """


lineas = []
for producto in productos:
    nombre = producto['nombre']
    precio = producto['precio']
    cantidad = producto['cantidad']
    linea = (f"{nombre},{precio},{cantidad}\n")
    lineas.append(linea)

with open("./Archivos/productos.txt", "w") as archivo:
    archivo.writelines(lineas)