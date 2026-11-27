import csv
import json


def calcular_total(valores):
    return sum(valores)


def main():
    # Carrega os dados de vendas
    with open("vendas.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        vendas = list(leitor)

    # Carrega as informações da empresa
    with open("configuracao.json", "r", encoding="utf-8") as arquivo:
        configuracao = json.load(arquivo)

    valores_vendas = []
    quantidades_vendas = []
    vendas_por_produto = {}