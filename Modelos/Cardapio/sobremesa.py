from Modelos.Cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return f'{self._nome}'

    @property
    def aplicar_desconto(self):
        if self._preco >= 5:
            self._preco -= (self._preco * 0.15)
        else:
            pass
