# Faça um programa que crie uma lista com 5 frutas e permita que o usuário digite o nome de uma fruta. Se for uma fruta repetida deverá ser desconsiderada.

lista = {"banana", "abacaxi", "maça", "kiwi"}

fruta = input("digite uma fruta...")

lista.add(fruta)

print(lista)

# Faça um programa que peça ao usuário para digitar uma frase e substitua todas as vogais por asteriscos (*).

frase = input("digite uma ffrase qualquer...")

nova_frase = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")

print(nova_frase)