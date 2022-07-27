frutas = {
    'Banana': 1.50,
    'Manga': 2.00,
    'Goiaba': 3.00,
    'Maçã': 1.55,
    'Abacaxi': 5.00,
    'Morango': 4.00,
    'Laranja': 2.50,
    'Amora': 1.00,
    'Acerola': 3.10,
    'Kiwi': 7.00
}

for i in frutas:
    escolha_fruta = input('Digite a fruta desejada: ').title()
    if escolha_fruta in frutas:
        peso = input('Digite o peso desejado: ')
        soma = float(peso) * float(frutas[escolha_fruta])
        print(f'Obrigada, o valor total da fruta {escolha_fruta} é R$ {soma}')
    else:
        print(f'Sorry, infelizmente não temos a fruta desejada. \n'
              f' Segue nossa lista de frutas disponíveis {frutas}')

