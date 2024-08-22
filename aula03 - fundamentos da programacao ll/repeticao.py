# repetição

#caso fosse necessário avaliar a situação de muitos alunos:

controle = int(input("digite 1 para calcular média ou 0 para sair"))

#while, quando não sei onde acaba

while controle != 0 or controle == 1 :
    media_1 = int(input("Digite a media do bimestre 1: "))
    media_2 = int(input("Digite a media do bimestre 2: "))
    media_3 = int(input("Digite a media do bimestre 3: "))
    media_4 = int(input("Digite a media do bimestre 4: "))

    media_final = (media_1 + media_2 + media_3 + media_4) / 4

    if media_final == 10 :
        print("Aprovado com distinção")
    elif media_final >= 7 :
        print("Aprovado")
    elif media_final >= 4 :
        print("Prova final")
    else :
        print("Reprovado")

    controle = int(input("digite 1 para calcular média ou 0 para sair"))

#for, quando eu sei quando acaba

lista_repeticoes = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(lista_repeticoes)) :
    media_1 = int(input("Digite a media do bimestre 1: "))
    media_2 = int(input("Digite a media do bimestre 2: "))
    media_3 = int(input("Digite a media do bimestre 3: "))
    media_4 = int(input("Digite a media do bimestre 4: "))

    media_final = (media_1 + media_2 + media_3 + media_4) / 4

    if media_final == 10 :
        print("Aprovado com distinção")
    elif media_final >= 7 :
        print("Aprovado")
    elif media_final >= 4 :
        print("Prova final")
    else :
        print("Reprovado")