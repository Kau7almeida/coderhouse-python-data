nomes = [
    "joao carlos",
    "maria eduarda",
    "ana rute",
    "pedro andre"
    ]

def primeiro_nome(nome):
    nomes = nome.split(" ")
    return nomes[0]

lista_primeiros_nomes = list(map(primeiro_nome, nomes))

print(lista_primeiros_nomes)