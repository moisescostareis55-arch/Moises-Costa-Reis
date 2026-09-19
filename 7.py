numeros = []
for i in range (10):
    numero = int(input("digite um numero:"))
    numeros.append(numero)

pares = 0 
impares = 0 
for numero in numeros:
    if numero %2 == 0:
        pares += 1
    else:
        impare += 1
print ("Pares:", pares)
print ("Impares", impares)
