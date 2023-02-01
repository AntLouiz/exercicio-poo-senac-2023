class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

    def exibir(self, indice = 0):
        print(f'{indice} === Nome: {self.nome} - Preço: {self.preco}')

produto_um = Produto('Massa de pizza', 5, 400)
produto_dois = Produto('Tomate', 2, 100)

produtos = [produto_um, produto_dois]
for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)

indice_selecionado = int(input('Selecione o produto: '))
if indice_selecionado > len(produtos) - 1:
    print('Produto inexistente.')
else:
    produto = produtos[indice_selecionado]
    quantidade = int(input('Informe a quantidade: '))
    print(f'O valor total é: R$ {quantidade * produto.preco}')
