nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade>15 and idade<18:
    print("Você já pode emitir seu título de eleitor.")
elif idade<=15:
    print("Você ainda não pode emitir seu título de eleitor.")
else:
    print("Você TEM que emitir o seu título de eleitor.")
