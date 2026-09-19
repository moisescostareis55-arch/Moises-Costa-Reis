notas = []
for i in ranger (10):
    nota = float(input("Digite s nota"))
    notas.append(nota)
soma = 0 
aprovados = 0
reprovados = 0

for nota in notas:
    soma += nota
    if nota >= 7:
        aprovados += 1
    else:
        reprovado += 1

media = soma / len(notas)
print ("Media:", media)
print ("Aprovados:", aprovados)
print ("Reprovados:", reprovado)