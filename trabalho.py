import os
import time
import cx_Oracle
from local import *

#loop para mostrar o menu
def menu():
    while (True):
        #limpa a tela toda vez que entrar no menu
        os.system('clear')
        #mostra as opcoes disponiveis
        print('[MENU INICIAL] Selecione o numero da opcao desejada:')
        print('1) Gerenciar Pessoa') # CRUD de pessoas (clientes e funcionarios)
        print('2) Gerenciar Eventos') # CRUD e todo o processo de cadastro de eventos
        print('3) Gerenciar Locais') # CRUD de Locais
        print('4) Gerenciar Servicos') # Por semantica, soh consulta, update e delete (sem insercao, so faz sentido junto a um evento)
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
            gerenciarLocal()

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

########################################################################
def inserirForma(formando, comissao):
    cursor = connection.cursor()
    
    statement = 'INSERT INTO FORMA(FORMANDO, COMISSAO) \
                 VALUES(:cpf, :comissao)'
    
    try:
        cursor.execute(statement, {'cpf': formando, 'comissao': comissao})
    except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- Formando invalido")
            print("\t- Nome de comissao invalido")
            return False
    except cx_Oracle.Error:
            print(cx_Oracle.Error.message)
            return False
    
    cursor.close()
    return True


def inserirComissao():
    cursor = connection.cursor()
    
    while(True):
        nome = raw_input("Digite o nome: ")
        tel = raw_input("Digite o telefone: ")
        email = raw_input("Digite o e-mail: ")

        statement = 'INSERT INTO COMISSAO(NOME, TELEFONE, EMAIL) \
                     VALUES(:nome, :tel, :email)'
        try:
            cursor.execute(statement, {'nome': nome, 'tel': tel, 'email': email})
        except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- Nome muito longo")
            print("\t- Telefone invalido")
            print("\t- E-mail invalido")
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)

    cursor.close()

    return nome


def inserirNoivo(CPF):
    cursor = connection.cursor()
    
    while(True):
        tel = raw_input("Digite o telefone: ")

        statement = 'INSERT INTO NOIVO(CPF, TELEFONE) \
                 VALUES(:CPF, :tel)'
        try:
            cursor.execute(statement, {'tel': tel, 'CPF': CPF})
            break
        except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- Telefone invalido")
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)

    cursor.close()


def inserirFormando(CPF):
    cursor = connection.cursor()
    
    while(True):
        curso = raw_input("Digite o curso: ")
        inst = raw_input("Digite a insituicao: ")

        statement = 'INSERT INTO FORMANDO(CPF, CURSO, INSTITUICAO) \
                     VALUES(:CPF, :curso, :inst)'
        try:
            cursor.execute(statement, {'curso': curso, 'inst': inst, 'CPF': CPF})
            break
        except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- Cargo ou Endereco muito longo")
            print("\t- Carteira de trabalho invalida")
            print("\t- Servicp invalido invalido")
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)

    cursor.close()

    c = raw_input('Deseja associar o formando a uma comissao?: (Digite: Sim)')
    if(c.upper()=='SIM'):
        c = input('Deseja criar uma nova comissao (1) ou assiar a uma existente (2)?: (Digite: 1 ou 2)')
        if(c == 1):
            nome = inserirComissao()
            inserirForma(CPF, nome)
        elif(c == 2):
            aux = False
            while(not aux):
                nome = raw_input("Digite o nome da comissao: ")
                aux = inserirForma(CPF, nome)


def inserirFuncionario(CPF):
    cursor = connection.cursor()
    
    while(True):
        cargo = raw_input("Digite o cargo: ")
        end = raw_input("Digite o endereco: ")
        ct = raw_input("Digite o numero da carteira de trabalho: ")
        salario = raw_input("Digite o salario: ")
        ord_serv = raw_input("Digite a ordem de servico: ")

        statement = 'INSERT INTO FUNCIONARIO(CPF, CARGO, ENDERECO, CT, SALARIO, ORDEM_SERVICO) \
                     VALUES(:CPF, :cargo, :end, :ct, :salario, :ord_serv)'
        
        try:
            cursor.execute(statement, {'CPF': CPF, 'cargo':cargo, 'end':end, 'ct':ct, 'salario':salario, 'ord_serv':ord_serv})
            break
        except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- Cargo ou Endereco muito longo")
            print("\t- Carteira de trabalho invalida")
            print("\t- Servic invalido invalido")
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)

    cursor.close()


def inserirPessoa():
    cursor = connection.cursor()

    while(True):
        CPF = raw_input("Insira o CPF (xxx.xxx.xxx-xx): ")
        nome = raw_input("Insira o nome: ")
        tipo = raw_input("Insira o tipo (Noivo, Formando ou Funcionario): ")

        statement = 'INSERT INTO PESSOA(CPF, NOME, TIPO) \
                     VALUES(:CPF, :nome, :tipo)'
        try:
            cursor.execute(statement, {'CPF': CPF, 'nome': nome, 'tipo': tipo})
            break
        except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- CPF ivalido")
            print("\t- Nome muito longo")
            print("\t- Tipo incorreto")
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)
    
    cursor.close()

    if(tipo.upper() == 'NOIVO'):
        inserirNoivo(CPF)
    elif(tipo.upper() == 'FORMANDO'):
        inserirFormando(CPF)
    elif(tipo.upper() == 'FUNCIONARIO'):
        inserirFuncionario(CPF)
    
    return CPF

def updateNoivo(CPF):
    cursor = connection.cursor()

    resp = raw_input("Deseja alterar o telefone? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            tel = raw_input("Digite o novo telefone: ")

            statement = 'UPDATE NOIVO \
                         SET TELEFONE = :tel \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'tel':tel, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Telefone invalido")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)
        
    cursor.close()


def updatePessoa():
    cursor = connection.cursor()
    
    while(True):
        CPF = raw_input("Digite o CPF a ser modificado: ")
        statement = 'SELECT * \
                     FROM PESSOA \
                     WHERE CPF = :CPF'
        try:
            cursor.execute(statement, {'cpf': CPF})
            break
        except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- CPF invalido")
        except cx_Oracle.Error:
                print(cx_Oracle.Error.message)

    resp = raw_input("Deseja alterar o nome? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            nome = raw_input("Digite o novo nome: ")

            statement = 'UPDATE PESSOA \
                         SET NOME = :nome \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'nome':nome, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Nome muito longo")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)

    statement = 'SELECT TIPO FROM PESSOA WHERE CPF = :CPF'
    cursor.execute(statement, {'CPF', CPF})
    response = cursor.fetchone()[0]
    
    cursor.close()
    
    if(response.upper() == 'NOIVO'):
        updatePessoa()
    elif(response.upper() == 'FORMANDO'):
        print(response)
    elif(response.upper() == 'FUNCIONARIO'):
        print(response)


def main():
    menu()
    connection.commit()


if __name__ == '__main__':
    main()
    connection.close()



