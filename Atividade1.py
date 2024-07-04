
print("Bem-vindos à loja do Gustavo de jesus de Oliveira")

#region Area para Solicitar o valor do pedido e a quantidade de parcelas
valorDoPedido = float(input("Digite o valor do pedido: "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))
#endregion

#region Area para calcular os juros com base na quantidade de parcelas
if quantidadeParcelas < 4:
    juros = 0
elif 4 <= quantidadeParcelas < 6:
    juros = 0.04
elif 6 <= quantidadeParcelas < 9:
    juros = 0.08
elif 9 <= quantidadeParcelas < 13:
    juros = 0.16
else:  # quantidadeParcelas >= 13
    juros = 0.32
#endregion

#region Area para calcular o valor da parcela e o valor total parcelado
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas
#endregion

#region Exibindo o resultado
print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}")
print(f"O valor total parcelado é de: R$ {valorTotalParcelado:.2f}")
#endregion