## Considerando c como o conjunto de probabilidade das letras
## do alfabeto em um canal X, qual a informação média do canal X?

import numpy as np
c = [0.1, 0.1, 0.1, 0.1, 0.07, 0.07, 0.07, 0.07, 0.07, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
print(- np.sum((np.array(c) * np.log2(c))))
