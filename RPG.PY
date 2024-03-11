import random

def batalha(heroi, monstro):
    while heroi["vida"] > 0 and monstro["vida"] > 0:
        dano_heroi = random.randint(1, 10)
        dano_monstro = random.randint(1, 10)
        heroi["vida"] -= dano_monstro
        monstro["vida"] -= dano_heroi
        print("Você causou", dano_heroi, "de dano ao monstro.")
        print("O monstro causou", dano_monstro, "de dano a você.")
        print("Vida do herói:", heroi["vida"])
        print("Vida do monstro:", monstro["vida"])
        print()

    if heroi["vida"] <= 0:
        print("Você foi derrotado!")
    else:
        print("Você derrotou o monstro e encontrou um tesouro!")

heroi = {"nome": "Herói", "vida": 100}
monstro = {"nome": "Monstro", "vida": 50}

print("Bem-vindo ao jogo de RPG!")
print("Você está em uma masmorra escura em busca de tesouros.")
print("Um monstro apareceu!")

batalha(heroi, monstro)