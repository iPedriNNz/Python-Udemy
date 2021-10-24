from vendas.preco import aumento, reducao
preco = 49.90

preco_au = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_au)
preco_re = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_re)
