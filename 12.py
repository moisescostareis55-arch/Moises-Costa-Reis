notas = []
for i in range(10):
    nota = float(input("Digite a nota:"))
    notas.append(nota)
soma = 0
aprovados = 0
reprovados = 0
notas10 = 0
for nota in notas:
    soma += nota
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1
    if nota == 10:
        notas10 += 1
media = soma / len(notas)
acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1
print("Notas:", notas)
print("Quantidade de notas:",lean(notas))
print("Soma:",soma)
print("Média:",media)
print("Aprovados",aprovados)
print("Notas 10:", notas10)
print("Acima da media:", acima_media)
