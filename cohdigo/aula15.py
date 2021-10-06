print('Digite um número natural \n')
num = int(input('>> '))
while num < 0:
    print('{} não é um número natural, tente mais uma vez:'.format(num))
    num = int(input('>> '))
    if num == 0:
        print('\nEu não tenho certeza se 0 é natural')
        break
if num != 0:
    print('\nParabéns! {} é um número naturl'.format(num))
