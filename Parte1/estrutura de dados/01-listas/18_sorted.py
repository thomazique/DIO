linguagens = ["python", "js", "c", "java", "csharp"]

a=sorted(linguagens, key=lambda x:len(x))

print(a)

b=sorted(linguagens, key=lambda x:len(x), reverse=True)

print(b)

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(numeros)