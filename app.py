menu = """

[d] Depositar
[s] Sacar
[e] extrato
[q] sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

    


while True:

    opcao = input(menu)

    if opcao == "d":
        print("qual valor deseja depositar?")
        dep = int(input())
        saldo += dep
        extrato += f"Depósito: +{dep}\n"

    elif opcao == "s":
        print("qual valor deseja sacar?")
        sac = int(input())
        if sac > saldo:
            print("Saldo insuficiente")
        elif sac > 500:
            print("Limite de saque diario excedido")
        else:
            saldo -= sac
            LIMITE_SAQUE -= 1
            if LIMITE_SAQUE == 0:
                print("limite de saques excedido")
        extrato += f"Saque: -{sac}\n"
            

    elif opcao == "e":
        print("Extrato:")
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação invalida por favor selecione uma opção")
