numeros = []
for i in range(7):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print ("Maior numero", maior)
