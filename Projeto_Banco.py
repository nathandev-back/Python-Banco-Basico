print("""
========Seja Bem-vindo ao Banco Amigo========
    Banco feito especialmente para você
        Entrando no Menu Do banco...
=============================================
""")

limite_saques = 3
limite = 500
extrato = ""

print("Perfeito, agora primeiramente vamos realizar seu primeiro Deposito")

while True:
    saldo = float(input("Digite o valor que deseja depositar: R$"))

    if saldo > 0 :
    
        print(f"Deposito no valor de R${saldo} realizado com sucesso!!!")
        
        extrato += f"Depósito: R$ {saldo:.2f}\n"
        
        break
            
    else:
        print("Não foi possivel realizar o Deposito, Tente novamente")



while True:

    print("""
========Banco Amigo========
1 - Saque
2 - Extrato bancario
0 - Sair
===========================
""")

    opcao = int(input("Digite a opção que deseja: "))
    
    
    if opcao == 1:

        limite_saques -= 1

        if limite_saques > 0:
            
            print("Você escolheu Sacar")
            
            while True:
    
                valor_saque = float(input("Digite a quantia que deseja Sacar: R$"))
            
                if valor_saque > limite:
    
                    print("Limite de saque é apenas 500 reais, Tente novamente com um valor menor")
                    continue
                
                elif valor_saque > saldo:
                    print("Não foi possivel realizar o saque, saldo insuficiente.")

                else:
    
                    print(f"Saque no valor de R${valor_saque} feito com sucesso!")

                    extrato += f"Saque: R${valor_saque:.2f}"
                    
                    break
        
            saldo -= valor_saque
        
            print(f"Você ainda tem R${saldo} para sacar")
            print(f"Voce só pode sacar 3 vezes ao dia, você so pode sacar mais {limite_saques}")
            
        else:

            print("Limite de saque diario atingido, Tente novamente amanhã.")

    elif opcao == 2:

        print("================== EXTRATO ==================")
        print("Nào foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=============================================")
    
    elif opcao == 0:

        print("Voce escolheu a opcao de saida, Agradecemos por usar nosso banco! Volte sempre.")
        print("Saindo", end = "...")
        
        break;



        