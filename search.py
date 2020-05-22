#!/usr/bin/python3

with open('test.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

nome = input('Set name:')

for linha in conteudo:
    print(linha)
    if nome in linha.split(','):
        print('===================')
        print(linha.split(',')[0])
        print(linha.split(',')[1])
        print(linha.split(',')[2])
        print(linha.split(',')[3])
        break
else:
    print('Nao encontrado')

exit()

