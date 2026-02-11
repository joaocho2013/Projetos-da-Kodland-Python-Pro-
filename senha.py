import random

carc = "112+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = int(input("escreva o tamanho da senha: "))
senha = ""  
for i in range(a):
    senha += random.choice(carc)
print("sua senha é: ", senha)
