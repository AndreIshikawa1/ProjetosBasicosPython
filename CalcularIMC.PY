def exibirIMC(imc):
    print(f"Seu índice de massa corporal é: {imc}")

print("===== Cálculo de IMC =====")
altura = float(input("Digite sua altura em metros: ").replace(',', '.'))
peso = float(input("Digite seu peso em kg: "))

imc_calculado = peso / (altura * altura)
exibirIMC(imc_calculado)

if imc_calculado > 40:
    print("Você tem obesidade de nível 3 - mórbida")
elif imc_calculado >= 35 and imc_calculado <= 39.9:
    print("Você tem obesidade de nível 2 - severa")
elif imc_calculado >= 30 and imc_calculado <= 34.9:
    print("Você tem obesidade de nível 1")
elif imc_calculado >= 25 and imc_calculado <= 29.9:
    print("Você possui sobrepeso!")
elif imc_calculado >= 18.5 and imc_calculado <= 24.9:
    print("Você possui um peso normal!")
elif imc_calculado >= 17 and imc_calculado <= 18.5:
    print("Você possui peso abaixo do normal!")
else:
    print("Você possui peso muito abaixo do normal")
