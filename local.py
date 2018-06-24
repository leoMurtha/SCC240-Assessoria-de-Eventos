from crud import *

def gerenciarLocal():
    os.system('clear')
    #mostra as opcoes disponiveis
    print('[MENU DE LOCAIS] Selecione o numero da opcao de desejada:')
    print('1) Cadastrar novo local') # Inserts
    print('2) Consultar locais cadastrados') # Selects
    print('3) Alterar locais cadastrados') # Updates
    print('4) Remover locais cadastrados') # Removes
    print('5) Voltar')
    opcaoL = input()
    
    os.system('clear')

    if(opcaoL == 1):
        cadastrarLocal()

    elif(opcaoL == 2):
        consultasLocal()

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
        connection.commit()

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

def consultasLocal():
    os.system('clear')
    print('[CONSULTAS DE LOCAIS] Selecione o numero da opcao de desejada:')
    print('1)Consultar local por nome') 
    print('2)Consultar locais por aluguel') 
    print('3)Consultar locais por lotacao')
    print('4)Consultar locais por aluguel e lotacao') 
    print('5)Consultar locais disponiveis em uma data') 
    print('6) Voltar')
    opcao = input()
    os.system('clear')

    if(opcao == 1):
        consultarLocal()
    elif(opcao == 2):
        consultarAluguel()
    elif(opcao == 3):
        consultarLotacao()
    elif(opcao == 4):
        consultarAluguelLotacao()
    elif(opcao == 5):
        consultarDisponiveis()


def consultarLocal():
    print('Insira o nome do lugar a ser consultado:')
def consultarAluguel():
    print('Insira o nome do lugar a ser consultado:')

def consultarLotacao():
    print('Insira o nome do lugar a ser consultado:')

def consultarAluguelLotacao():
    print('Insira o nome do lugar a ser consultado:')

def consultarDisponiveis():
    print('Insira a data a ser consultada:')
    data = raw_input()
    locais = selecionarLocal(data = data)
    printLocais(locais)
    print('Finalizar consulta:')
    raw_input()
 
def selecionarLocal(data):
    """
        Retorna o local escolhido de acordo com locais disponiveis na data
    """
    cursor = connection.cursor()
    statement = "SELECT L.NFANTASIA, L.ALUGUEL, L.AREA FROM LOCAL L\
                    WHERE L.NFANTASIA NOT IN\
                    (SELECT L.NFANTASIA FROM LOCAL L\
                    INNER JOIN EVENTO E ON E.LOCAL = L.NFANTASIA\
                    WHERE E.DATA = to_date(:data, 'yyyy/mm/dd'))"
    try:
        cursor.execute(statement, {'data': data})
        responses = cursor.fetchall()
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao: Valores inseridos invalidos')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    return responses

def printLocais(local):
    print('Locais disponiveis')
    print('Nome, Locacao e Aluguel')
    for i in xrange(len(local)):
        print("{}) {}".format(i,local[i]))
