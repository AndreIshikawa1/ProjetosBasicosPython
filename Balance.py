balance = 100

while True:
    try:
        add = float(input("Deposit: "))
        break
    except ValueError:
        print("Valor invalido! ")

balance +=add

print(f"Você possui {balance}")