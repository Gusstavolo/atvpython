#region EXIGÊNCIA DE CÓDIGO 1 de 7
print("Bem-vindos à Fábrica de Camisetas do Gustavo de jesus de Oliveira")
#endregion

#region Menu
_menu = """
-------------Entre com o modelo desejado-------------
| MCS | - Manga Curta Simples                       |
| MLS | - Manga Longa Simples                       |
| MCE | - Manga Curta Simples Com Estampa           |
| MLE | - Manga Longa Simples Com Estampa           |
-----------------------------------------------------
"""
#endregion

#region Função para escolher o modelo
def escolha_modelo():
    while True:
        print(_menu)
        modelo = input("> ").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Opção inválida. Entre com o modelo novamente.")
#endregion

#region Função para determinar o número de camisetas com desconto
def num_camisetas():
    while True:
        try:
            numero = int(input("\nDigite o número de camisetas: "))
            if numero > 20000:
                print("""
Não aceitamos tantas camisetas de uma vez.
Por favor, entre com o número de camisetas novamente. 
                      
                      """)
            elif numero >= 2000:
                return numero, 0.88  # Desconto de 12%
            elif numero >= 200:
                return numero, 0.93  # Desconto de 7%
            elif numero >= 20:
                return numero, 0.95  # Desconto de 5%
            else:
                return numero, 1  # Sem desconto
        except ValueError:
            print("Entrada inválida. Digite um número.")
#endregion

#region menu do frete
_menuFrete = """
Digite o tipo de frete:
1 - Frete por Transportadora - R$ 100.00
2 - Frete por Sedex - R$ 200.00
0 - Retirar pedido na fábrica - R$ 0.00
"""
#endregion

#region Função para escolher o frete
def frete():
    while True:
        print(_menuFrete)
        opcao = input(">>")
        if opcao == "1":
            return 100
        elif opcao == "2":
            return 200
        elif opcao == "0":
            return 0
        else:
            print("Opção inválida. Tente novamente.")
#endregion

#region cálculo do valor total a pagar
modelo = escolha_modelo()
num, desconto = num_camisetas()
frete_valor = frete()


total = (modelo * num * desconto) + frete_valor

totalCamisaDesconto = int(num * desconto)
#endregion

#region Exibindo o valor total
print(f"Total: R$ {total:.2f} (Modelo: {modelo:.2f} * Quantidade({'Sem Desconto' if desconto == 1 else 'Com Desconto'}): {totalCamisaDesconto:d}) + {frete_valor:.2f}")  #[EXIGÊNCIA DE CÓDIGO 6 de 7]
#endregion
