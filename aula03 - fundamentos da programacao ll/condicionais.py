# condicionais

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
