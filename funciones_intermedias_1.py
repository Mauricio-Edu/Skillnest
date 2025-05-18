#1
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]


matriz[1][0] = 6        #Cambia el valor de 3 en matriz por 6
print(matriz)           

cantantes[0]["nombre"] = "Enrique Martin Morales"       # “Ricky Martin” a “Enrique Martin Morales”
print(cantantes)

ciudades["México"][2] = "Monterrey"                     #En ciudades, cambia “Cancún” por “Monterrey”
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431                   #cambia el valor de “latitud” por 9.9355431
print(coordenadas)


#2

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
        for cantante in lista:
            print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

iterarDiccionario(cantantes)


#3

def iterarDiccionario2(llave, lista):
      for cantante in lista:
            print(f" {cantante[llave]}")

iterarDiccionario2("nombre", cantantes)

print()

iterarDiccionario2("pais", cantantes)


#4

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    ciudades = diccionario["ciudades"]
    comidas = diccionario["comidas"]

    print(f"{len(ciudades)} CIUDADES")
    for ciudad in ciudades:
        print(ciudad)
    
    print()  # Línea en blanco

    print(f"{len(comidas)} COMIDAS")
    for comida in comidas:
        print(comida)


imprimirInformacion(costa_rica)