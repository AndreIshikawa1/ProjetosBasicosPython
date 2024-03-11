import random


gerar = random.randint(1,10)
tentativas = 1
print(gerar)

user = int(input("Digite um número de 1 a 10: "))
while gerar != user:
    print("Você errou!")
    user = int(input("Digite um número de 1 a 10 novamente: "))
    tentativas += 1
    if tentativas >= 5:
        print(f"Você alcançou o limite maximo de {tentativas} tentativas!")
        break

if user == gerar:
    print("Parabéns você acertou!")
