# EXEMPLO 1

num1 = int(input('1º Número: '))
num2 = int(input('2º Número: '))
soma = num1 + num2
# print(num1, ' + ', num2, ' = ', soma)  # Funciona, mas dá para fazer melhor.
print('{0} + {1} = {2}'.format(num1, num2, soma))  # Os números podem ser omitidos.

# DESAFIO 003

# sem tempo irmão.

# DESAFIO 004

coisa = input('Digite uma coisa: ')
print('É um número: {}'.format(coisa.isnumeric()))  # Verifica se numérico.
print('É uma letra: {}'.format(coisa.isalpha()))  # Verifica se alpha.
print(type(coisa))  # Verifica o tipo primitivo.
