menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
    # Depositar apenas valores POSITIVOS
        valor_do_deposito = float(input("Qual valor você deseja depositar? R$ "))
                
        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            print(f"Você depositou R$ {valor_do_deposito:.2f}. Saldo atual R$ {saldo:.2f}.")
            extrato += f"Depósito: + R$ {valor_do_deposito:.2f}\n"

        else:
            print("O valor a ser depositado deve ser maior que 0 (zero).")
    
    elif opcao == "s":
    #Saque deve ser menor que R$500,00 e máximo de 3 saques por dia
        valor_do_saque = float(input("Qual valor você deseja sacar? R$ "))

        if numero_saques >= (LIMITE_SAQUES):
            print(f"Não é possível sacar. Você já fez {numero_saques} saques hoje. Volte amanhã.")

        elif valor_do_saque > limite:
            print(f"Não é possível sacar esse valor. Seu limite para saque é de R$ {limite:.2f}.")
        
        elif valor_do_saque > saldo:
                print(f"Não é possível sacar esse valor. Seu saldo é de R$ {saldo:.2f}.")

        elif valor_do_saque > 0:
                saldo -= valor_do_saque
                print(f"Você sacou R$ {valor_do_saque:.2f}.\nSaldo atual: R$  {saldo:.2f}.")
                numero_saques += 1
                extrato += f"Saque:    - R$ {valor_do_saque:.2f}\n"

        else:
            print("Insira um valor válido.")
                        
    elif opcao == "e":
    #Listar todas as movimentações realizadas
        print(str.center(" EXTRATO ", 30, "#"))
        print("\nNão há registro de movimentações na data de hoje\n" if not extrato else f"\n{extrato}") #implementado após conferir a solução
        print(f"Saldo:      R$  {saldo:.2f}.\n")
        print(str.center("", 30, "#"))
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    