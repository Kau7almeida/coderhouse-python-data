# 'NumPy' é uma abreviação de 'Numeric Python'

# no terminal digite 'pip install numpy'
# import numpy as np

# O NumPy é ótimo para armazenar e manipular ddos numéricos em matrizes.

import numpy as np

# Joana está pensando em abrir uma confeitaria e precisará começar a comprar todo o seu leite, ovos, açúcar, farinha e manteiga a granel.

# Ajude ela a descobrir quanto precisa comprar usando matrizes NumPy que descrevem suas receitas.

# Por exemplo, sua receita de cupcake pede:

# Farinha	 - 2 xícaras
# Açúcar - 0,75 xícaras	
# Ovos - 2 ovos	
# Leite - 1 xícaras
# Manteiga - 0,5 xícaras

# Crie um array NumPy que represente esses dados. Cada elemento deve ser um número (por exemplo, 2para "2 xícaras"). Salve esse array como `cupcakes`.

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
cupcakes

recipes = np.genfromtxt( 'recipes.csv', delimiter = ',' )
recipes

eggs = recipes[:, 2]
eggs

one_eggs = eggs[ eggs == 1 ]
one_eggs

cookies = recipes[2]
cookies

double_batch = cupcakes * 2
double_batch

grocery_list = cookies + double_batch
grocery_list = np.array([cookies, double_batch])
grocery_list