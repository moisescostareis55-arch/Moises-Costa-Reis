numeros = []
for i in range(5):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)
soma = 0
for numero in numeros:
    soma += numero
print("Numeros:",numeros)
print("soma:", soma)
