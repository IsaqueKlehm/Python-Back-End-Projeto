class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria, ativo):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'\n{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.status}')

    @property
    def status(self):
        return '🟢 Aberto' if self._ativo else '🔴 Fechado'

    def alternar_estado(self):
        self._ativo = not self._ativo
    

restaurante_praca = Restaurante('praça', 'Gourmet', False)
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana', True)

Restaurante.listar_restaurantes()