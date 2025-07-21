c1 = {1, 2, 3, 4, 5}
c2 = {6, 7, 8, 9}
c3 = {1, 0}

a = c1.intersection(c2)
print(a)

b = c1.difference(c2)
print(b)

c = c1.issuperset(c3)
print(c)


sorteio = {1, 23}

d = sorteio.add(25)

print(sorteio)

numeros = {1,2,3,4,5,6,7,8,9,5,3,2,1,0,3,2}

print(numeros)
numeros.discard(1)
print(numeros)

numeros.pop()
print(numeros)

numeros.remove(2)
print(numeros)