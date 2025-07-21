a = set([1,2,3,1,3,4]) #{1,2,3,4}
b = set("abacaxi") #{b, a, c, x, i}
c = set(("palio", "gol", "celta", "palio"))

# print(a)
# print(b)
# print(c)

for indice, carro in enumerate(c):
    print(f"{indice}: {carro}")

    