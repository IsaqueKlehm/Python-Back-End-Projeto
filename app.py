from Modelos.restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato
from Modelos.Cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 4.50, 'Grande')
bebida_suco.aplicar_desconto

prato_paozinho = Prato('Paozinho', 1, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto

sobremesa_praca = Sobremesa('Pudim', 7, 'Entrada', 'Pequeno', 'Um pudim pequeno')
sobremesa_praca.aplicar_desconto

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_praca)

def main():
    restaurante_praca.exibir_cardapio
    
if  __name__ == '__main__':
    main()