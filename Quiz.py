quiz1 = ["Qual o nome do criador do QUIZ?",
         "A - André",
         "B - André"]

quiz2 = ["Qual a idade do criador do QUIZ?",
         "A - 20",
         "B - 19"]


pontos = 0




quiz = input("Você deseja iniciar o QUIZ?(Digite sim) ").title()
if quiz == "Sim" or quiz =="S":
    for q1 in quiz1:
        print(q1)
    user = input("Digite a resposta correta: ").upper()
    if user == "A" or user == "ANDRÉ":
        print('Parabéns você acertou o quiz!')
        pontos +=1
    else:
        print("Você errou!")

    for q2 in quiz2:
        print(q2)
    user = input("Digite a reposta correta: ").upper()
    if user == "A" or user == "20":
        print("Parabéns você acertou!")
        pontos +=1
    else:
        print("Você errou!")

    print(f"O QUIZ acabou e você fez {pontos} pontos!")
else:
    print("Quiz encerrado!")

