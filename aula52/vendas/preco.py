from aula52.vendas.formata import formataa

def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * porcentagem / 100)
    if formata:
        return formataa.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * porcentagem / 100)
    if formata:
        return formataa.real(r)
    else:
        return r
