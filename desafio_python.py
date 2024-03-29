import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_de_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")
           
        else: 
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
         valor = float(input("Informe o valor do saque: "))

         excedeu_saldo = valor > saldo

         excedeu_limite = valor > limite

         excedeu_saques = numero_de_saques >= LIMITE_SAQUES

         if excedeu_saldo:
             print("Operação falhou! Você não tem saldo suficiente.")
              

         elif excedeu_limite:
             print("Operação falhou! O valor do saque excede o limite.")

         elif excedeu_saques:    
            print("Operação falhou! Número maximo de saques excedido.")

         elif valor >0:   
             saldo -= valor
             extrato += f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
             numero_de_saques += 1
             print("Saque realizado com sucesso!")
          

         else:    
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "q":
        print("Operação finalizada! Obrigado por utilizar nosso sistema.")
        break


    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
