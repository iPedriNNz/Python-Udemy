from classes import Escritor, MaquinaDeEscrever, Caneta

escritor = Escritor('Pedro')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
