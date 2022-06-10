"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Luiz'
print(nome, type(nome))

nome = 'Luiz Otávio'
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
data_1 = True
data_atual = 2019
peso = 80

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(idade * altura)

imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', int(imc))


