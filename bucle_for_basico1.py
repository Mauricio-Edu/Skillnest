for x in range(0,101):      #Básico: imprime todos los números enteros del 0 al 100.
    print(x)

for i in range(2,500,2):    #Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 501
    print(i)

for x in range(0,101):      #imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
    if x == 0:
        print(x)
    elif x%10 == 0:
        print("baby")      
    elif x%5 == 0:
        print("ice ice")

    else:
        print(x)

suma_par = 0                    #suma los números pares del 0 al 500,000 e imprime la suma total
for x in range(0,500001,2):
    suma_par += x
print(suma_par)

for x in range (2024,0,-3):     #imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3
    print(x)

numInicial = 3                  #contador dinámico
numFinal = 10
multiplo = 2
for x in range(numInicial,numFinal+1):
    if x%multiplo == 0 and x != 0:
        print(x)




