notas = []
for i in range(5):
    nota = float (input("Digite a nota:"))
    notas.append(nota)
soma = 0 
for nota in notas:
    soma += nota
media = soma / lean(notas)
print("nota:", notas)
print("soma:", soma)
print("Media", media)

