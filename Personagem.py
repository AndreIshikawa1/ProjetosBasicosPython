class Personagem:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return (f"Nome do personagem: {self.nome} | Idade do personagem: {self.idade}")
  
p1 = Personagem("André", 20)
print(p1)
    