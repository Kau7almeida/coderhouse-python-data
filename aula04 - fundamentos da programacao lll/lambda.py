# uma função anonima, como uma arrow function

def quadrado(x):
    return x**2

print(quadrado(5))

quadrado_lambda = lambda x: x ** 2

print(quadrado_lambda(5))
print(quadrado_lambda(7))

# dado uma lista de numeros, quais são pares

numeros = [1,2,3,4,5,6,7,8,9,10]

eh_par_lambda = lambda x: x % 2 == 0

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)

# poderiamos mapear resultados em lista, otimizando a escrita para saida de dados

lista_quadrados = list(map(lambda x: x ** 2, numeros))
print(lista_quadrados)

# ainda é possivel fazer ordenações em uma lista de maneira simples

produtos = [
    {
        "nome": "notebook",
        "preco": 2499,
        "desconto": 0.15
    },
    {
        "nome": "celular",
        "preco": 899,
        "desconto": 0.17
    },
    {
        "nome": "tablet",
        "preco": 2899,
        "desconto": 0.12
    },
]