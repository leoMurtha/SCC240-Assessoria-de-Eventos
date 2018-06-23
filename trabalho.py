import os
import time
import cx_Oracle

#loop para mostrar o menu
def menu():
	while (True):
		#limpa a tela toda vez que entrar no menu
		os.system('clear')
		#mostra as opcoes disponiveis
		print('Selecione uma opcao:')
		print('1) Inserir Pessoa')
		print('2) ')
		print('3) ')
		print('4) ')
		print('5) ')
		print('6) Sair')
		#le a opcao desejada
		opcao = input()
		#limpa a tela
		os.system('clear')

		if (opcao == 1):
			inserirPessoa()

		elif (opcao == 2):
			print (opcao)

		elif (opcao == 3):
			print (opcao)

		elif (opcao == 4):
			print (opcao)

		elif (opcao == 5):
			print (opcao)

		elif (opcao == 6):
			print (opcao)
			exit()
		else:
			print('Opcao invalida. Selecione uma nova opcao.')
			time.sleep(2)


def inserirPessoa():
    print (cx_Oracle.clientversion())
    cursor = connection.cursor()

    print('Insira o CPF (xxx.xxx.xxx-xx): ')
    CPF = raw_input()
    print('Insira o telefone: ')
    nome = raw_input()
    print('Insira o tipo (Noivo, Formando ou Funcionario): ')
    tipo = raw_input()

    statament = 'INSERT INTO Pessoa \
                 VALUES(:CPF, :nome, :tipo)'
    cursor.execute(statament, {'CPF': CPF, 'nome': nome, 'tipo': tipo})



    cursor.close()


def main():
    inserirPessoa()


if __name__ == '__main__':
    dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
    connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)
    main()



