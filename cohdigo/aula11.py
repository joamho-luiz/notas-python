import random

print('texto controle')

num = random.randint(1, 10)

if 5 > num:
    print('\033[7;43m Amarelaço \033[m')
else:
    print('\033[1;31m Vermelhão')

"""
print('{:20}'.format('joão sempre testa para ver o que acontece.'), end='')
print('agora')
"""
