class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

    def exibir(self):
        print(f'Nome: {self.nome} - Preço: {self.preco}')

produto = Produto('Massa de pizza', 5, 400)
quantidade = int(input('Informe a quantidade: '))
print(quantidade)
