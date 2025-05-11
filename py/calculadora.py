#solicitar dois numeros e perguntar qual operador usar

def calculadora():

num1 = float(input('Digite um numero: '))
num2 = float(input(' Digite o outro numero: '))

    #escolha do operador
opera = input(' Qual operador ira usar? (+, -, *, /) ')

if opera == '+':
    print(f'A soma dos numeros foi de {num1 + num2:}')

elif opera == '-':
    print(f'A subtração da conta foi de {num1 - num2} ')

elif opera == '*':
    print(f' O numero {num1} multiplicado por {num2} resulta em {num2 * num1:.2}')

elif opera == '/':
    result =
    if num2 != 0:
        print(f'A divisao dos numeros foi de {num1 / num2:.2}')

