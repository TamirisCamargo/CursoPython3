"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'

# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# for n in range(0, 100, 8):
#     print(n)
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)


