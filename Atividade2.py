#region EXIGÊNCIA DE CÓDIGO 1 de 8
print("Bem-vindos à loja de Marmitas do Gustavo de jesus de Oliveira")  
#endregion

#region Função para exibir o menu # Menu para escolha dos sabores e tamanhos
_Menu = """

--------------------------CARDÁPIO-------------------------
-----------------------------------------------------------
--| TAMANHO | BA (Bife Acebolado) | FF (Filé de Frango) |--
--|    P    |       R$ 16.00      |       R$ 15.00      |--
--|    M    |       R$ 18.00      |       R$ 17.00      |--
--|    G    |       R$ 22.00      |       R$ 21.00      |--
-----------------------------------------------------------

"""

#endregion

#region inicialização do acumulador
total = 0  # Inicializando o acumulador #[EXIGÊNCIA DE CÓDIGO 2 de 8]
#endregion

print( _Menu)
#region loop para repetição dos pedidos
while True:
    
    
    #region solicitação e verificação do sabor
    sabor = input("\nDigite o sabor da marmita (BA/FF): ").upper()
    if sabor not in ['BA', 'FF']:
        print(f"Sabor inválido. Tente novamente.")
        continue
    #endregion
    
    #region Solicitação e verificação do tamanho
    tamanho = input("Digite o tamanho da marmita (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue
    #endregion

    #region Cálculo do preço baseado em sabor e tamanho #[EXIGÊNCIA DE CÓDIGO 4 de 8]
    if sabor == 'BA':
        saborNome = "Bife Acebolado"
        if tamanho == 'P':
            preco = 16
        elif tamanho == 'M':
            preco = 18
        else:  # tamanho == 'G'
            preco = 22
    elif sabor == 'FF':
        saborNome = "Filé de Frango"
        if tamanho == 'P':
            preco = 15
        elif tamanho == 'M':
            preco = 17
        else:  # tamanho == 'G'
            preco = 21
    #endregion

    #region Informa pedido
    mensagemPedido = "Você pediu uma marmita de {saborNome} no tamanho {tamanho}: R${preco:.2f}".format(
        saborNome=saborNome, tamanho=tamanho, preco=preco
    )
    print(mensagemPedido)
    #endregion

    #region Acumulando o valor do pedido
    total += preco #[EXIGÊNCIA DE CÓDIGO 5 de 8]
    #endregion
    
    #region Pergunta se o cliente deseja mais alguma coisa #[EXIGÊNCIA DE CÓDIGO 6 de 8]
    mais_alguma_coisa = input("\nDeseja pedir mais alguma coisa? (S/N): ").upper()
    if mais_alguma_coisa == 'N':
        break
    #endregion
#endregion

#region Exibindo o total do pedido
print(f"\nO total do seu pedido é: R$ {total:.2f}") 
#endregion
