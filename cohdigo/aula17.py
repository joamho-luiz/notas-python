pessoas = list()
dados = list()

for c in range(0, 3):
    dados.append(str(input('NOME: ')))
    dados.append(int(input('IDADE: ')))
    pessoas.append(dados[:])
    dados.clear()

print(f'\n {pessoas}')
