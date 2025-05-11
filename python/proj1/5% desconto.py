#ler o preço de um produto e de 5% de desconto

nome = input(' Qual o produto que receberá o desconto?: ').title()
valor = float(input(' Qual o valor do produto em reais?: R$'))

print(f' {nome} recebeu 5% de desconto no valor {valor} e ´passou a ser {valor - (valor * 0.05):.2f}')