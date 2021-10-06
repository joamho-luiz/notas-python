"""
nome = input('Nome: ')

if nome == 'ana':
    print('ANA')
elif nome == 'paulo':
    print('PAULO')
elif nome == 'paulo':
    print('DAVI')
else:
    print('Não conheço')
"""

# DESAFIO 37

print('--CONVERSOR DE NÚMERO--')
num = int(input('Digite um número intiro: '))
print('Qual base você deseja:')
sol = input('(B)inário - (O)ctal - (H)exadecimal: ')
print('\n')

if sol == 'B':
    print('{} em binário é: {}'.format(num, bin(num)[2:]))
elif sol == 'O':
    print('{} em octal é: {}'.format(num, oct(num)[2:]))
elif sol == 'H':
    print('{} em hexadecimal é : {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
