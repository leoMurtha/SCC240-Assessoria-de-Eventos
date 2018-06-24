from localConsulta import *
from localCadastro import *
from localAlteracao import *

def gerenciarLocal():
    exitL = False
    while(not exitL):
        os.system('clear')
        #mostra as opcoes disponiveis
        print('[MENU DE LOCAIS] Selecione o numero da opcao de desejada:')
        print('1) Cadastrar novo local') # Inserts
        print('2) Consultar locais cadastrados') # Selects
        print('3) Alterar locais cadastrados') # Updates
        print('4) Descadatrar local') # Deletes
        print('5) Voltar')
        opcaoL = input()
    
        os.system('clear')

        if(opcaoL == 1):
            cadastrarLocal()
        elif(opcaoL == 2):
            consultasLocal()
        elif(opcaoL == 3):
            alterarLocal()
        elif(opcaoL == 4):
            descadastrarLocal()
        elif(opcaoL == 5):
            exitL = True
        else:
            print('Opcao invalida. Selecione uma nova opcao.')      

def descadastrarLocal():
    nome = readAttribute('Nome do local')
    deletarLocal(nome)
    connection.commit()

def deletarLocal(nome):
    cursor = connection.cursor()
    statement = "DELETE FROM LOCAL WHERE NFANTASIA = :nome"
    try:
        cursor.execute(statement, {'nome' : nome})
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao')
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False

    cursor.close()
    return True
