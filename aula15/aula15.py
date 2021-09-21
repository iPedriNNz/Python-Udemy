"""
Manipulando stirngs
* String indices
* Fatiamento de string
* Funções built-in len, abs, type, print, etc...
"""
texto = 'Python s2'
url = 'www.google.com.br/'
# positivos [123456789]
print(texto[0])  # print 'P'
print(texto[-1])  # print '2'
print(url[:-1])  # print www.google.com.br
nova_string = texto[2:6]  # Nova string recebe 'thon'
#  nova_string = texto[:6] / nova_string = texto[-9:-3] # Nova string recebe 'Python'
#  nova_string = texto[:6:2]  # recebe Pto pula de 2 em 2
