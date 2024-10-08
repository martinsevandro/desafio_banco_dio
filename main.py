menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        deposit = float(input("digite o valor de depósito: "))

        if deposit >= 0:
            saldo += deposit
            extrato += f"Depósito: R${deposit:.2f}\n"
        else:
            print("o valor digitado é negativo, por favor adicione um valor válido!")
    
    elif opcao == "s":
        print("Sacar")
        saque = float(input("digite o valor de saque: "))

        if saque >= 0:
            if saque <= saldo:
                if numero_saques < LIMITE_SAQUE:
                    if saque <= limite:
                        saldo -= saque
                        numero_saques += 1
                        print(f"saque de R${saque:.2f} realizado com sucesso!")
                        extrato += f"Saque: R${saque:.2f}\n"
                    else: 
                        print("valor de saque é maior que o limite de 500, obedeça o limite de saque.")
                else:
                    print("o limite diário de 3 saques foi atingido.")
            else:
                print("o saldo atual é insuficiente para o saque desejado")
        else:
            print("o valor digitado é negativo, por favor adicione um valor válido!")

    elif opcao == "e":        
        print("#Extrato:")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}\n")

    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Opção inválida, escolha uma função existente!")