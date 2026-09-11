from Modelos.restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'Grande')
prato_paozinho = Prato('Paozinho', 2, 'O melhor pão da cidade')

restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

def main():
    print(restaurante_praca)
    
if  __name__ == '__main__':
    main()