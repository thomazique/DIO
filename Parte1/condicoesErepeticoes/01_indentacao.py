saldo = 500

def sacar(valor):
    if saldo >= valor:
        print("valor sacado!")
    else:
        print("Saldo insuficiente, seu saldo é de: ", saldo)

sacar(1000)

print (saldo)