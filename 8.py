numeros = []
for i in range(8):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)
positivos = 0
negativos = 0
zero = 0
for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero <0 :
        negativos += 1
    else:
        zeros += 1
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zero)
