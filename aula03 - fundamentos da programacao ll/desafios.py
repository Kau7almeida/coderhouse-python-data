perguntas = ["telefonou para a vitima? ", "esteve no local no crime? ", "mora perto da vitima? ", "devia para a vitima? ", "ja trabalhou para a vitima? "]

resposta_sim = 0

print("responda as perguntas com sim ou não")

for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if resposta != "sim" and resposta != "não":
        break
    if resposta == "sim":
        resposta_sim += 1