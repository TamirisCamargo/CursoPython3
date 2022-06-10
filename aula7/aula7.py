"""
Formatação de Strings
"""

nome = 'Luiz Otávio'
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
peso = 80
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', int(imc))
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
