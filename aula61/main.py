from pessoa import Pessoa

p1 = Pessoa('Pedro', 24)
p2 = Pessoa.por_ano_nascimento('Fabio', 34)

print(p1.nome, end=' ')
p1.get_ano_nascimento()
print(p2.nome, p2.idade)
print(p1.gera_id())
