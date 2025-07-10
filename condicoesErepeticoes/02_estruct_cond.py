import sys

# saldo = 2000
# opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

# if opcao == 1:
#     valor = float(input("informe o valor do saque:"))
#     if valor<=saldo:
#         print("Saque realizado com sucesso.")
#     else:
#         print("Saldo insuficiente, seusaldo é de: ", saldo)

# elif opcao == 2:
#     print("Exibindo op estrato ...")

# else:
#     sys.exit("Opção inválida")

# maior_idade = 18
# idade_especial = 17

# idade = int(input("informe sua idade: "))

# if idade >= maior_idade:
#     print("Maior idade, pode tirar a cnh.")
# elif idade == idade_especial:
#     print("pode fazer aulas teoricas")
# else:
#     print("nao pode fazer nada")

# texto = input("informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# else:
#     print()

# for numero in range(0, 11):
#     print(numero, end=" ")

# for numero in range(0, 100, 5):
#     print(numero, end=" ")


# WHILE
# opcao = -1
# while opcao != 0:
#     opcao = int(input("1 sacar 2 extrato 3 sair"))

#     if opcao ==1:
#         print("saque realizado")
#     elif opcao == 2:
#         print("puxando extrato")
#     else:
#         sys.exit("Opção inválida")

while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        print("voce informou o numero secreto: ", numero, "SISTEMA PARANDO")
        break
    else:
        print(numero)
    