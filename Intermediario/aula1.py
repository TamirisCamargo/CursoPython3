"""
Funções - def em Python (Parte 1)
"""

def funcao():
    print('Hello World')

funcao()
funcao()
funcao()

def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao(nome='Tami', msg='Hi')
saudacao()
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Otávio')
saudacao('Olá', 'João')