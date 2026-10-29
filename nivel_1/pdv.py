
compras = []

valor_compra = float(input("Digite o valor da compra (R$) ou 0 para encerrar: "))

while valor_compra != 0:
    if valor_compra < 0:
        print("Valor inválido! Digite um valor positivo.")
        valor_compra = float(input("Digite o valor da compra (R$) ou 0 para encerrar: "))
        continue

    idade = int(input("Digite a idade do cliente: "))

    while idade < 0:
        print("Idade inválida! Digite uma idade válida.")
        idade = int(input("Digite a idade do cliente: "))

    valor_original = valor_compra

    if idade >= 65:
        valor_compra = valor_compra * 0.8

    if valor_compra > 100:
        valor_compra = valor_compra * 0.9

    desconto = valor_original - valor_compra

    compras.append([valor_original, desconto, valor_compra])

    print(f"Valor final: R$ {valor_compra:.2f}")

    valor_compra = float(input("Digite o valor da próxima compra (R$) ou 0 para encerrar: "))

print("\n--- RESUMO DAS COMPRAS ---")

quantidade_compras = len(compras)
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in compras:
    total_bruto = total_bruto + compra[0]
    total_descontos = total_descontos + compra[1]
    total_final = total_final + compra[2]

print(f"Quantidade de compras: {quantidade_compras}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
