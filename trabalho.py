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


def inserirForma(formando, comissao):
    cursor = connection.cursor()
    
    statement = 'INSERT INTO FORMA(FORMANDO, COMISSAO) \
                 VALUES(:cpf, :comissao)'
    cursor.execute(statement, {'cpf': formando, 'comissao': comissao})

    cursor.close()


def inserirComissao():
    cursor = connection.cursor()
    
    nome = raw_input("Digite o nome: ")
    tel = raw_input("Digite o telefone: ")
    email = raw_input("Digite o e-mail: ")

    statement = 'INSERT INTO COMISSAO(NOME, TELEFONE, EMAIL) \
                 VALUES(:nome, :tel, :email)'
    cursor.execute(statement, {'nome': nome, 'tel': tel, 'email': email})

    cursor.close()

    return nome


def inserirNoivo(CPF):
    cursor = connection.cursor()
    
    tel = raw_input("Digite o telefone: ")

    statement = 'INSERT INTO NOIVO(CPF, TELEFONE) \
                 VALUES(:CPF, :tel)'
    cursor.execute(statement, {'tel': tel, 'CPF': CPF})

    cursor.close()


def inserirFormando(CPF):
    cursor = connection.cursor()
    
    curso = raw_input("Digite o curso: ")
    inst = raw_input("Digite a insituicao: ")

    statement = 'INSERT INTO FORMANDO(CPF, CURSO, INSTITUICAO) \
                 VALUES(:CPF, :curso, :inst)'
    cursor.execute(statement, {'curso': curso, 'inst': inst, 'CPF': CPF})

    cursor.close()

    c = raw_input('Deseja associar o formando a uma comissao?: (Digite: Sim)')
    if(c.upper()=='SIM'):
        c = input('Deseja criar uma nova comissao (1) ou assiar a uma existente (2)?: (Digite: 1 ou 2)')
        if(c == 1):
            nome = inserirComissao()
            inserirForma(CPF, nome)
        elif(c == 2):
            nome = raw_input("Digite o nome da comissao: ")
            inserirForma(CPF, nome)


def inserirFuncionario(CPF):
    cursor = connection.cursor()
    
    cargo = raw_input("Digite o cargo: ")
    end = raw_input("Digite o endereco: ")
    ct = raw_input("Digite o numero da carteira de trabalho: ")
    salario = raw_input("Digite o salario: ")
    ord_serv = raw_input("Digite a ordem de servico: ")

    statement = 'INSERT INTO FUNCIONARIO(CPF, CARGO, ENDERECO, CT, SALARIO, ORDEM_SERVICO) \
                 VALUES(:CPF, :cargo, :end, :ct, :salario, :ord_serv)'
    cursor.execute(statement, {'CPF': CPF, 'cargo':cargo, 'end':end, 'ct':ct, 'salario':salario, 'ord_serv':ord_serv})
    
    cursor.close()


def inserirPessoa():
    cursor = connection.cursor()

    CPF = raw_input("Insira o CPF (xxx.xxx.xxx-xx): ")
    nome = raw_input("Insira o nome: ")
    tipo = raw_input("Insira o tipo (Noivo, Formando ou Funcionario): ")

    statement = 'INSERT INTO PESSOA(CPF, NOME, TIPO) \
                 VALUES(:CPF, :nome, :tipo)'
    cursor.execute(statement, {'CPF': CPF, 'nome': nome, 'tipo': tipo})

    cursor.close()

    if(tipo.upper() == 'NOIVO'):
        inserirNoivo(CPF)
    elif(tipo.upper() == 'FORMANDO'):
        inserirFormando(CPF)
    elif(tipo.upper() == 'FUNCIONARIO'):
        inserirFuncionario(CPF)


def main():
    inserirPessoa()
    connection.commit()


if __name__ == '__main__':
    dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
    connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)
    
    main()
    
    connection.close()



