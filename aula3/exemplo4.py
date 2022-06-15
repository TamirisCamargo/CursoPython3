"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html
"""

# positivos   [012345678]
texto       = 'Python s2'
# negativos  -[987654321]
print( texto[8])

url = ' www.google.com.br/'

print(url[:-1])

nova_string = texto[2:6]
nova_string = texto[7:]
nova_string = texto[0:6:2]
print(nova_string)
print(len(texto))


