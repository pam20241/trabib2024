hora = int(input("Digite um número de 0 a 23:"))
if hora<12:
    print("Está de manhã ")
elif hora>=12 and hora<18:
    print("Está de tarde ")
else: 
    print("Está de noite ")
