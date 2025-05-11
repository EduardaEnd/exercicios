# Classe bancaria base
class contaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} foi realizado com sucesso.')

    def sacar(self, valor):  # Correção: usar 'valor' consistentemente
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')

    def verSaldo(self):
        print(f'O valor do seu saldo é: R${self.saldo:.2f}')


# Classe contaCorrente (herda de contaBancaria):
class contaCorrente(contaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso (usando limite).')
        else:
            print('Saldo e limite insuficientes.')


# Classe contaPoupanca (herda de contaBancaria):
class contaPoupanca(contaBancaria):
    def calcular_rendimento(self):
        rendimento = self.saldo * 0.02  # 2% de aumento do rendimento
        self.saldo += rendimento
        print(f'Rendimento de R${rendimento:.2f} aplicado com sucesso.')


# Função principal do menu
def menu():
    contas = []

    while True:
        print('*' * 38)
        print('Sistema Bancário'.center(38))
        print('=' * 38)
        print('| (1) Criar conta Corrente')
        print('| (2) Criar conta Poupança')
        print('| (3) Depositar')
        print('| (4) Sacar')
        print('| (5) Ver saldo')
        print('| (6) Calcular Rendimento (Poupança)')
        print('| (0) Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite seu nome: ')
            conta = contaCorrente(nome)
            contas.append(conta)
            print('Conta corrente adicionada com sucesso!')

        elif opcao == '2':
            nome = input('Digite seu nome: ')
            conta = contaPoupanca(nome)
            contas.append(conta)
            print('Conta poupança adicionada com sucesso!')

        elif opcao == '3':
            nome = input('Nome do titular da conta: ')
            valor = float(input('Qual o valor a depositar? R$'))
            for conta in contas:
                if conta.titular == nome:
                    conta.depositar(valor)
                    break
            else:
                print('Conta não encontrada.')

        elif opcao == '4':
            nome = input('Nome do titular da conta: ')
            valor = float(input('Qual o valor a sacar? R$'))
            for conta in contas:
                if conta.titular == nome:
                    conta.sacar(valor)
                    break
            else:
                print('Conta não encontrada.')

        elif opcao == '5':
            nome = input('Nome do titular da conta: ')
            for conta in contas:
                if conta.titular == nome:
                    conta.verSaldo()
                    break
            else:
                print('Conta não encontrada.')

        elif opcao == '6':
            nome = input('Nome do titular da conta poupança: ')
            for conta in contas:
                if conta.titular == nome and isinstance(conta, contaPoupanca):
                    conta.calcular_rendimento()
                    break
            else:
                print('Conta poupança não encontrada.')

        elif opcao == '0':
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Tente novamente.')
