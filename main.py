class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

    def exibir(self):
        print(f'Nome: {self.nome} - Preço: {self.preco}')

produto = Produto('Massa de pizza', 5, 400)
produto.exibir()
quantidade = int(input('Informe a quantidade: '))
print(f'O valor total é: R$ {quantidade * produto.preco}')
