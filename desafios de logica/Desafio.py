
def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario > 1100 and salario <= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15

    return aliquota * salario

valorSalario = float(input("Qual o valor do seu salario?"))
valorBeneficio = float(input("Qual o valor do seu beneficio?"))
valorImposto = calcular_imposto(valorSalario)
saida = valorSalario - valorImposto + valorBeneficio
print(f'{saida:.2f}')