valor_compra = float(input("Digite o valor da compra (R$): "))
idade = int(input("Digite a idade do cliente: "))

if idade >= 65:
    valor_compra = valor_compra * 0.8

print(f"Valor da compra com desconto: R$ {valor_compra:.2f}")