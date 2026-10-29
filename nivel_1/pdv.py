
valor_compra = float(input("Digite o valor da compra (R$): "))
idade = int(input("Digite a idade do cliente: "))

if idade >= 65:
    valor_compra = valor_compra * 0.8

if valor_compra > 100:
    valor_compra = valor_compra * 0.9

print(f"Valor final: R$ {valor_compra:.2f}")
