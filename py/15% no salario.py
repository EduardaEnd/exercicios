#aumento do salario em 15%

nome = input(' Digite o nome do funcionario: ').title()
salario = float(input(' Agora digite o valor de seu salário: R$'))

print(f' O(A) funcionario(a) {nome} teve um aumento de 15%, resultando em R${salario + (salario * 0.15):.2f}')