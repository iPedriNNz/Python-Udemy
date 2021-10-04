"""
sets em python (conjuntos)
add (adiciona), uptdate (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão no dois sets, mas não em ambos)
"""

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.discard(2)
print(s1)
