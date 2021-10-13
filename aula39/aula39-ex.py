carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 40))
carrinho.append(('Produto 3', 90))
carrinho.append(('Produto 4', 10))
carrinho.append(('Produto 5', 20))

total = sum(([float(v) for x, v in carrinho]))

print(f'O valor total do carrinho é de R$ {total:.2f}')
