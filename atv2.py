import random

numero_secreto = random.randint(1, 20)
tentativas = 5

for i in range(tentativas):
    chute = int(input("fale um numero entre 1 e 20: "))
    
    if chute == numero_secreto:
        print("parabens voce acertou")
        break
    elif chute < numero_secreto:
        print("o numero secreto e maior")
    else:
        print("o numero secreto e menor")
else:
    print("suas tentativas acabaram o numero era:", numero_secreto)
