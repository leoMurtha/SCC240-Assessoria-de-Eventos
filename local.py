import os
import time
import cx_Oracle

dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)

def readNotNullAttribute(varName):
        notCompleted = True
        while(notCompleted):
            print('Informe '+varName+' (NAO PODE SER NULO):')
            varValue = raw_input()
            if varValue.strip():
                notCompleted = False    
        return varValue
     
def readAttribute(varName):
        print('Informe '+varName+' :')
        varValue = raw_input()
        return varValue


def gerenciarLocal():
    os.system('clear')
    #mostra as opcoes disponiveis
    print('[MENU DE LOCAIS] Selecione o numero da opcao de desejada:')
    print('1) Cadastrar novo local') # CRUD de pessoas (clientes e funcionarios)
    print('2) Consultar e Alterar locais cadastrados') # Select, update, remove
    print('3) Voltar')
    opcaoL = input()
    
    os.system('clear')

    if(opcaoL == 1):
        cadastrarLocal()

    elif(opcaoL == 2):
        menu()

    elif(opcaoL == 3):
        menu()   

    else:
        print('Opcao invalida. Selecione uma nova opcao.')      

def cadastrarLocal():
        os.system('clear')
        #mostra as opcoes disponiveis
        print('[CADASTRO DE LOCAL] Preencha os valores abaixo:')

        # lendo atributos da tabela local
        nFant = readNotNullAttribute('Nome Fantasia')
        area  = readNotNullAttribute('Area em metros quadrados')
        lot   = readAttribute('Lotacao')
        alug  = readNotNullAttribute('Aluguel')
        end   = readNotNullAttribute('Endereco')
        tel   = readAttribute('Telefone')
        nProp = readNotNullAttribute('Nome Proprietario')

        # insercao no banco de dados
        inserirLocal(nFant,area,lot,alug,end,tel,nProp)

        print("Local Cadastrado com Sucesso!")

def inserirLocal(nomeFantasia,area,lotacao,aluguel,endereco,telefone,nomeProprietario):
    cursor = connection.cursor()
    
    statement = 'INSERT INTO LOCAL \
                 VALUES(:nFant, :area, :lot, :alug, :end, :tel, :nProp)'
    
    try:
        cursor.execute(statement, {'nFant' : nomeFantasia, 'area' : area, 'lot' : lotacao, 'alug' : aluguel, 'end' : endereco, 'tel' : telefone, 'nProp' : nomeProprietario})
    
    except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- nomeFantasia invalido ou ja existente")
            print("\t- Valores de outros atributos invalidos")
            return False
    except cx_Oracle.Error:
            print(cx_Oracle.Error.message)
            return False
    
    cursor.close()
    return True    

