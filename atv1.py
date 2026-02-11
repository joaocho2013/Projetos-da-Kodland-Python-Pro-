for i in range(1, 6):
    print("*" * i)

nome = "escreva o seu nome: "
print("*" * (len(nome) + 4))
print("*", nome, "*")
print("*" * (len(nome) + 4))

n = int(input("escreva um numero: "))
soma = 0

for i in range(1, n+1):
    soma += i

print("A soma de 1 até", n, "é:", soma)
