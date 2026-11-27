    # Apresenta o relatório geral
    print("==========================================")
    print(f"RELATÓRIO DE VENDAS - {configuracao['empresa']}")
    print(f"Período: {configuracao['periodo']}")
    print("==========================================")
    print(f"Número de registros de venda: {total_registros}")
    print(f"Quantidade total de unidades vendidas: {total_unidades}")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Média de faturamento por registro: R$ {media_por_venda:.2f}")
    print(f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)")
    print("------------------------------------------")

    # Apresenta o faturamento e a quantidade de cada produto
    print("VENDAS POR PRODUTO:")
    for produto, dados in vendas_por_produto.items():
        print(f"{produto}: {dados['quantidade']} unidades | Faturamento: R$ {dados['faturamento']:.2f}")
    print("------------------------------------------")

    # Compara o faturamento com a meta definida no JSON
    meta = configuracao["meta_faturamento"]
    diferenca = faturamento_total - meta

    print(f"Meta de faturamento: R$ {meta:.2f}")
    if faturamento_total >= meta:
        print(f"Status: Meta atingida! Superou a meta em R$ {diferenca:.2f}.")
    else:
        print(f"Status: Meta não atingida. Faltaram R$ {abs(diferenca):.2f}.")

    # Analisa o orçamento de despesas, caso exista no JSON
    if "orcamento_despesas" in configuracao:
        print(f"Orçamento previsto para despesas: R$ {configuracao['orcamento_despesas']:.2f}")

    print("==========================================")


if __name__ == "__main__":
    main()
