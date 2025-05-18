numero1 = 70 #declaración de variable
numero2 = 3.14 #declaración de variable
booleano = False #declaración de variable
cadena = 'Hola Mundo' #declaración de variable
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #diccionario
frutas = ('guayaba', 'fresa', 'papaya') #tupla
print(type(frutas)) #revisión de tipo
print(ingredientes_pastel[2]) #accesar valor e impriir
ingredientes_pastel.append('Mantequilla') #añadir un elemento a la lista
print(persona['nombre']) #accesar con la llave par obtener el valor e imprimir
persona['nombre'] = 'Kevin' #modificando valor de llave nombre
persona['color_ojos'] = 'cafe' #agregando valor de llave color_ojos
print(frutas[2]) #accesar a 3er valor de la tupla e imprimir

if numero1 > 45:         #uso de condicional
    print("Numero mayor")
else:                   #si no cumple la condicion del if
    print("Numero menor")

if len(cadena) < 5:           #condicional 1ra condicion
    print("Cadena corta")
elif len(cadena) > 15:           #condicional 2da condicion
    print("Cadena larga")
else:                                  #Para todos los demás
    print("Cadena perfecta")

for x in range(8):          #ciclo for de 0 a 7
    print(x)
for x in range(2,8):        #ciclo for de 2 a 7
    print(x)
for x in range(2,8,2):      #ciclo for de 2 a 7, de 2 en 2
    print(x)
x = 0                       #ciclo while
while(x < 8):
    print(x)
    x += 1                  #incrementa 1 su valor

ingredientes_pastel.pop()           #quitamos mantequilla, último elemento
ingredientes_pastel.pop(1)          #quitamos leche, 2do elemento

print(persona)
persona.pop('color_ojos')               #quitamos color de ojos 
print(persona)

print(ingredientes_pastel)
for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':             #si es harina se lo salta, de otro modo imprime hasta que aparezca chocolate que imprime y termina
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():  #declarando una funcion
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()         #ejecutando la funcion

def imprime_hola_n_veces(n):        #declarando funcion con parametro n
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)             #ejecutando funcion

def imprime_hola_n_o_diez_veces(n = 10):        #por defecto imprime 10 veces, si le entrega parametro lo hace con ese valor
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

#print(numero3)  No esta definida la variable
#        numero3 = 86  error de indentacion
#frutas[0] = 'naranja'  Tuplas inmutables
#print(persona['hobbies'])  No se encuentra la llave
#print(ingredientes_pastel[11]) fuera del rango de la lista  
print(booleano)
#frutas.append('manzana') tuplas inmutables
#frutas.pop(1) tuplas inmutables