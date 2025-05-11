#solicitar nome e data de nascimento

nome=input("Qual o seu nome?\n ")
dia=int(input("Digite o dia de seu nascimento: "))
mes=input("Digite o nome do mês em qual você nasceu: ")
ano=int(input("Digite o ano em que você nasceu: "))

print("Olá {}, você nasceu em {}/{}/{}, correto?".format(nome,dia,mes,ano))