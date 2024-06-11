nome = input("Digite o seu nome: ")
disciplina = input("Digite o nome da disciplina: ")
n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))
m = (n1+n2)/2
if m >= 6:
    print (f" {nome} está APROVADO na disciplina {disciplina}")
else:
    print  (f" {nome} está REPROVADO na disciplina {disciplina}")
