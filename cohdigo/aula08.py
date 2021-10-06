# Importação geral:
"""
import math
num = int(input('Digite um número: '))
print('A raiz de {} é {:.2f}'.format(num, math.sqrt(num)))
"""


# IMPORTAÇÃO ESPCIFICA:
"""
from math import sqrt, floor

num = int(input('Digite um número: '))
print('A raiz de {} é {}'.format(num, floor(sqrt(num))))
"""

"""
import random
n1 = random.random()
n2 = random.randint(1,10)
print('{} / {} = {}'.format(n1, n2, n1/n2))
"""

"""
import emoji  # Módulo externo
print(emoji.emojize("E aí? :sunglasses:", use_aliases=True))
"""

# DESAFIO 016

"""
import math
ângulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O seno de {} é: {:.2f}'.format(ângulo, seno))
"""
