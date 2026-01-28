meme_dict= {
    "F": "Respeito ou morte",
    "FF": "Desistir",
    "GG": "Good Game/ Bom jogo",
    "RUSHAR": "Ir pra cima",
    "BROKEN": "Algo muito roubado",
}


word = input("Escreva uma palavra da atualidade que voce nao intenda(Escreva tudo em maiusculo): ")

if word in meme_dict.keys(): 
    print(meme_dict[word])
else:
    print("a palavra esta no dicionario")
