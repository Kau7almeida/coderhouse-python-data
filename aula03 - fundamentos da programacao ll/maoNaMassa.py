numero = int(input("digite um número:"))

if numero % 2 == 0 :
    print("Par")
else :
    print("Ímpar")


frase = input("digite uma frase... ")
lista_palavras = frase.split(" ")

for i in range(len(lista_palavras)) :
    print(f"A palavra {lista_palavras[i]} tem {len(lista_palavras[i])} letras")


senha_correta = "1234"
senha = input("digite a senha: ")

while senha_correta != senha :
    senha = input("senha incorreta, digite novamente: ")

print("bem vindo")
