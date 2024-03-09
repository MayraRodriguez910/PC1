#Variables

#Problema 1:
# Solicitar el nombre de usuario
nombre_usuario = input("Introduce tu nombre de usuario: ")
# Mostrar el saludo
print("¡" + "Hola " + nombre_usuario + "!")

#Problema 2:
# Solicitar el costo de la comida al usuario
costo_comida = float(input("Ingrese el costo de su comida: $"))
# Solicitar el porcentaje de propina al usuario
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15): "))
# Calcular la cantidad de propina
propina = (porcentaje_propina / 100) * costo_comida
# Mostrar la cantidad de propina a dejar
print("Debe dejar $" + "{:.2f}".format(propina) + " como propina.")

#Problema 3:
# Definir el peso de un payaso y una muñeca en gramos
peso_payaso = 112
peso_muñeca = 75
# Solicitar al usuario la cantidad de payasos y muñecas vendidos
cantidad_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
cantidad_muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))
# Calcular el peso total del paquete
peso_total = (cantidad_payasos * peso_payaso) + (cantidad_muñecas * peso_muñeca)
# Mostrar el peso total del paquete
print("El peso total del paquete es de", peso_total, "gramos.")

#Problema 4
# Solicitar al usuario un entero positivo
N = int(input("Ingrese un entero positivo, N: "))
# Verificar si N es un entero positivo
if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    # Calcular la suma de todos los enteros desde 1 hasta N
    suma_total = sum(range(1, N + 1))
    # Mostrar la suma en pantalla
    print("La suma de todos los enteros desde 1 hasta", N, "es:", suma_total)

#Problema 5
# Solicitar al usuario la cantidad de shows musicales vistos
cantidad_shows = int(input("Ingrese la cantidad de shows musicales que ha visto en el último año: "))
# Verificar si ha visto más de 3 shows
ha_visto_mas_de_3 = cantidad_shows > 3
# Mostrar el resultado en pantalla
print("¿Ha visto más de 3 shows musicales? ", ha_visto_mas_de_3)

#Problema 6
# Solicitar al usuario la edad del cliente
edad_cliente = int(input("Ingrese la edad del cliente: "))
# Calcular el precio de entrada según la edad
if edad_cliente < 4:
    precio_entrada = 0  # Menor de 4 años, entrada gratis
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5  # Entre 4 y 18 años, entrada $5
else:
    precio_entrada = 10  # Mayor de 18 años, entrada $10
# Mostrar el precio de entrada en pantalla
print("El precio de entrada es: $" + str(precio_entrada))

#Problema 7
# Solicitar al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Menú de opciones
print("Seleccione una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (primer número - segundo número)")
print("3. Mostrar la multiplicación de los dos números")
# Obtener la opción del usuario
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")
# Realizar la operación según la opción seleccionada
if opcion == '1':
    resultado = num1 + num2
    print("La suma de", num1, "y", num2, "es:", resultado)
elif opcion == '2':
    resultado = num1 - num2
    print("La resta de", num1, "y", num2, "es:", resultado)
elif opcion == '3':
    resultado = num1 * num2
    print("La multiplicación de", num1, "y", num2, "es:", resultado)
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

#Problema 8
# Solicitar al usuario la hora en formato HH:MM
hora_str = input("Ingrese la hora en formato HH:MM: ")
# Dividir la cadena de la hora en horas y minutos
hora_dividida = hora_str.split(":")
hora = float(hora_dividida[0]) + float(hora_dividida[1]) / 60  # Convertir a formato decimal
# Definir los rangos de tiempo para cada comida
desayuno_inicio, desayuno_fin = 7.0, 8.0
almuerzo_inicio, almuerzo_fin = 12.0, 13.0
cena_inicio, cena_fin = 18.0, 19.0
# Determinar si es hora de desayunar, almorzar o cenar
if desayuno_inicio <= hora <= desayuno_fin:
    print("Es hora de desayunar.")
elif almuerzo_inicio <= hora <= almuerzo_fin:
    print("Es hora de almorzar.")
elif cena_inicio <= hora <= cena_fin:
    print("Es hora de cenar.")
else:
    # No enviar nada si no es hora de comer
    pass

#Colecciones de Datos

#Problema 9
# Definir la lista original
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
# Crear una copia de la lista original e invertirla
lista_invertida = lista_original.copy()
lista_invertida.reverse()
# Mostrar la lista invertida
print(lista_invertida)

#Problema 10
# Definir la lista de muestra
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
# Eliminar elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]
# Crear una nueva lista sin los elementos en las posiciones indicadas
lista_resultado = [lista_muestra[i] for i in range(len(lista_muestra)) if i not in posiciones_a_eliminar]
# Mostrar la lista resultante
print(lista_resultado)

#Problema 11
# Definir la lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
# Crear un conjunto para eliminar duplicados y convertirlo a lista
lista_procesada = list(set(lista_original))
# Mostrar la lista resultante
print(lista_procesada)

#Problema 12
# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")
# Obtener la extensión del archivo (sufijo)
if '.' in nombre_archivo:
    sufijo = nombre_archivo.split('.')[-1].lower()
else:
    sufijo = ""
# Asignar el tipo MIME correspondiente
if sufijo in ['gif', 'jpg', 'jpeg', 'png']:
    tipo_mime = 'image/' + sufijo
elif sufijo == 'pdf':
    tipo_mime = 'application/pdf'
elif sufijo == 'txt':
    tipo_mime = 'text/plain'
elif sufijo == 'zip':
    tipo_mime = 'application/zip'
else:
    tipo_mime = 'application/octet-stream'
# Mostrar el resultado
print("Tipo MIME del archivo:", tipo_mime)



