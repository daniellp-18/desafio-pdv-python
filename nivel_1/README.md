# PDV com Descontos

**Autor:** Daniel Lindoso Penha 

## 1. Objetivo

Desenvolver um sistema simples de Ponto de Venda (PDV) em Python para calcular descontos em compras, registrar os valores e apresentar um resumo ao final da execução.

## 2. Regras de negócio

- Clientes com idade igual ou superior a 65 anos recebem 20% de desconto.
- Após esse desconto, se o valor restante for superior a R$ 100,00, aplica-se mais 10% de desconto.
- O sistema permite registrar várias compras.
- Digitar `0` no campo do valor da compra encerra o programa.
- Valores de compra e idades negativos são inválidos e devem ser corrigidos.
- Ao encerrar, o programa apresenta a quantidade de compras, o total bruto, o total de descontos e o total final.

## 3. Como executar

É necessário ter o Python instalado.

Abra o terminal na pasta `nivel_1` e execute:

```bash
python pdv.py
```

Informe o valor da compra e a idade do cliente conforme solicitado. Para encerrar, digite `0` quando o programa pedir o valor de uma nova compra.

## 4. Funcionamento do programa

O programa utiliza estruturas condicionais para aplicar os descontos e um laço de repetição para permitir várias compras. Os dados de cada compra são armazenados em uma lista por meio do método `append()`.

Ao final, o programa percorre a lista para calcular os totais e exibir o resumo das compras.

## 5. Casos de teste

| Caso | Valor da compra | Idade | Resultado esperado |
|---|---:|---:|---:|
| 1 | R$ 50,00 | 30 | R$ 50,00 |
| 2 | R$ 100,00 | 30 | R$ 100,00 |
| 3 | R$ 80,00 | 65 | R$ 64,00 |
| 4 | R$ 100,00 | 70 | R$ 80,00 |
| 5 | R$ 125,00 | 70 | R$ 100,00 |
| 6 | R$ 200,00 | 30 | R$ 180,00 |
| 7 | R$ 101,00 | 30 | R$ 90,90 |
| 8 | R$ 200,00 | 65 | R$ 144,00 |
| 9 | R$ 1.000,00 | 80 | R$ 720,00 |
| 10 | R$ 200,00 | 64 | R$ 180,00 |

## 6. Resultado dos testes

Os dez casos de teste foram executados, e os valores finais corresponderam aos resultados esperados.

O resumo apresentado após as dez compras foi:

- **Quantidade de compras:** 10
- **Total bruto:** R$ 2.156,00
- **Total de descontos:** R$ 447,10
- **Total final:** R$ 1.708,90

## 7. Tecnologias utilizadas

- Python
- Visual Studio Code
- Git
- GitHub
