menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            
            saldo += valor
            
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 's':
        
        if numero_saques < 3:
            
            if saldo > 0:
                
                valor = float(input("Informe o valor do saque: "))
                
                if valor <= limite:

                    numero_saques += 1
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                
                else:
                    print("Operação falhou! O valor do saque excede o limite.")

            else:
                print("Operação falhou! Você não tem saldo suficiente.")

        else:
            print("Operação falhou! Número máximo de saques excedido.")

    elif opcao == 'e':
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == 'q':
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")