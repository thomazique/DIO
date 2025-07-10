# 

saldo = 1000
saque = 200
limite = 100
conta_especial = True

verfic_AND = saldo >= saque and saque <= limite
print (verfic_AND)

verfic_OR = saldo >= saque or saque <= limite
print (verfic_OR)

verfic_NOT = saque>saldo
print (verfic_NOT)

verific_PARENTS = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (verific_PARENTS)