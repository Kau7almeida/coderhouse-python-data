import numpy as np
import pandas as pd

# exercício 1
ex_1 = np.random.randint( 0, 100, size = (5, 5) )
ex_1.dtype

# exercício 2
ex_2 = np.random.rand(5,5)
print("minimo:  ", ex_2.min())
print("maximo:  ", ex_2.max())
print("media:  ", ex_2.mean())

# exercício 3
ex_3 = np.random.rand(1,10)
ex_3 = ex_3 * 10
ex_3_int = ex_3.astype(int)
ex_3_int

# exercício 4
ex_4 = np.random.randint(0,9, size=(3,3))
ex_4[1, :] = -1

# ecercício 5
feira = np.array([["banana", "maça", "pera"],
                  [7.90, 10.20, 11.80],
                  [12, 3, 4]])
df = pd.DataFrame(feira, columns=["fruta", "preço", "quantidade"])
df