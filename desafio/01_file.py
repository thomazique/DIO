# Sistema Bancário Simples
def exibir_menu():
    return """
    ========== BANCO DIGITAL ==========
    [1] Realizar Depósito
    [2] Realizar Saque  
    [3] Visualizar Extrato
    [0] Finalizar Sistema
    ===================================
    Escolha uma opção: """

def main():
    conta_saldo = 0
    valor_limite_saque = 500
    historico_transacoes = ""
    contador_saques = 0
    MAX_SAQUES_DIARIOS = 3

    while True:
        escolha = input(exibir_menu())

        match escolha:
            case "1":  # Depósito
                quantia = float(input("Digite a quantia para depósito: R$ "))
                
                if quantia <= 0:
                    print("Erro: Valor deve ser positivo!")
                else:
                    conta_saldo += quantia
                    historico_transacoes += f"Depósito: R$ {quantia:.2f}\n"
                    print(f"Depósito realizado com sucesso!")

            case "2":  # Saque
                quantia = float(input("Digite a quantia para saque: R$ "))
                
                # Validações organizadas
                if quantia <= 0:
                    print("Erro: Valor deve ser positivo!")
                elif contador_saques >= MAX_SAQUES_DIARIOS:
                    print("Limite diário de saques atingido!")
                elif quantia > valor_limite_saque:
                    print(f"Valor excede o limite de R$ {valor_limite_saque:.2f}")
                elif quantia > conta_saldo:
                    print("Saldo insuficiente para esta operação!")
                else:
                    conta_saldo -= quantia
                    historico_transacoes += f"Saque: R$ {quantia:.2f}\n"
                    contador_saques += 1
                    print("Saque realizado com sucesso!")

            case "3":  # Extrato
                print("\n" + "="*40)
                print("           EXTRATO BANCÁRIO")
                print("="*40)
                
                if historico_transacoes:
                    print(historico_transacoes)
                else:
                    print("Nenhuma transação registrada.")
                
                print(f"Saldo atual: R$ {conta_saldo:.2f}")
                print("="*40 + "\n")

            case "0":  # Sair
                print("Obrigado por usar nosso sistema!")
                break

            case _:  # Opção inválida
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()