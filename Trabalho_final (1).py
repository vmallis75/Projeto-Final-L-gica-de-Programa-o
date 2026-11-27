    # Calcula os valores e reúne os dados por produto
    for venda in vendas:
        quantidade = int(venda["quantidade"])
        preco_unitario = float(venda["preco_unitario"])
        produto = venda["produto"]

        total_venda = quantidade * preco_unitario
        valores_vendas.append(total_venda)
        quantidades_vendas.append(quantidade)

        if produto not in vendas_por_produto:
            vendas_por_produto[produto] = {"quantidade": 0, "faturamento": 0}

        vendas_por_produto[produto]["quantidade"] += quantidade
        vendas_por_produto[produto]["faturamento"] += total_venda

    faturamento_total = calcular_total(valores_vendas)
    total_unidades = calcular_total(quantidades_vendas)
    total_registros = len(vendas)
    media_por_venda = faturamento_total / total_registros if total_registros else 0

    # Identifica o produto com maior quantidade total vendida
    if vendas_por_produto:
        produto_mais_vendido = max(
            vendas_por_produto,
            key=lambda produto: vendas_por_produto[produto]["quantidade"]
        )
        maior_quantidade = vendas_por_produto[produto_mais_vendido]["quantidade"]
    else:
        produto_mais_vendido = "Nenhum"
        maior_quantidade = 0