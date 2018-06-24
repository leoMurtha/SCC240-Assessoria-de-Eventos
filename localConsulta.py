from crud import *


def consultasLocal():
    exitL = False
    while(not exitL):
        os.system('clear')
        print('[CONSULTAS DE LOCAIS] Selecione o numero da opcao de desejada:')
        print('1)Consultar todos os locais cadastrados')
        print('2)Consultar local por nome') 
        print('3)Consultar locais por aluguel') 
        print('4)Consultar locais por lotacao')
        print('5)Consultar locais por aluguel e lotacao') 
        print('6)Consultar locais disponiveis em uma data') 
        print('7) Voltar')
        opcao = input()
        os.system('clear')

        if(opcao == 1):
            consultarLocal()
        elif(opcao == 2):
            consultarLocalNome()
        elif(opcao == 3):
            consultarAluguel()
        elif(opcao == 4):
            consultarLotacao()
        elif(opcao == 5):
            consultarAluguelLotacao()
        elif(opcao == 6):
            consultarDisponiveis()
        elif(opcao == 7):
            exitL = True

def consultarLocal():
    print('Esses sao todos os locais cadastrados no sistema atualmente:')
    locais = selecionarLocal()
    printLocais(locais,'Nome Fantasia, Area,Lotacao,Aluguel,Endereco,Telefone,Nome do Proprietario')
    print('Finalizar consulta:')
    raw_input()

def consultarLocalNome():
    nome = readNotNullAttribute('Nome Fantasia do Local')
    locais = selecionarLocalNome(nome)
    printLocais(locais,'Nome Fantasia, Area,Lotacao,Aluguel,Endereco,Telefone,Nome do Proprietario')
    print('Finalizar consulta:')
    raw_input()

def consultarAluguel():
    alug = readAttribute('aluguel a ser consultada')
    locais = selecionarLocalAluguel(alug)
    printLocais(locais,'Nome, Locacao e Aluguel')
    print('Finalizar consulta:')
    raw_input()

def consultarLotacao():
    lot = readAttribute('lotacao a ser consultada')
    locais = selecionarLocalLotacao(lot)
    printLocais(locais,'Nome, Locacao e Aluguel')
    print('Finalizar consulta:')
    raw_input()

def consultarAluguelLotacao():
    alug = readAttribute('aluguel a ser consultada')
    lot = readAttribute('lotacao a ser consultada')
    locais = selecionarLocalAluguelLotacao(alug,lot)
    printLocais(locais,'Nome, Locacao e Aluguel')
    print('Finalizar consulta:')
    raw_input()

def consultarDisponiveis():
    data = readAttribute('data a ser consultada')
    locais = selecionarLocalData(data)
    printLocais(locais,'Nome, Locacao e Aluguel')
    print('Finalizar consulta:')
    raw_input()

def selecionarLocal():
    """
        Retorna todos os locais cadastrados no sistema
    """
    cursor = connection.cursor()
    statement = "SELECT * FROM LOCAL L"
    try:
        cursor.execute(statement)
        responses = cursor.fetchall()
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    return responses

def selecionarLocalNome(nome):
    """
        Retorna valores do local escolhido de acordo com o nome
    """
    cursor = connection.cursor()
    statement = "SELECT NFANTASIA, ALUGUEL, AREA FROM LOCAL\
                    WHERE NFANTASIA = :nome"
    try:
        cursor.execute(statement, {'nome': nome})
        responses = cursor.fetchall()
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao: Nome procurado invalido')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    return responses

def selecionarLocalAluguel(aluguel):
    """
        Retorna valores dos locais de acordo com o aluguel
    """
    cursor = connection.cursor()
    statement = "SELECT NFANTASIA, ALUGUEL, AREA FROM LOCAL\
                    WHERE ALUGUEL = :aluguel"
    try:
        cursor.execute(statement, {'aluguel': aluguel})
        responses = cursor.fetchall()
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao: Aluguel procurado invalido')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    return responses

def selecionarLocalLotacao(lotacao):
    """
        Retorna valores dos locais de acordo com a lotacao
    """
    cursor = connection.cursor()
    statement = "SELECT NFANTASIA, ALUGUEL, AREA FROM LOCAL\
                    WHERE ALUGUEL = :lot"
    try:
        cursor.execute(statement, {'lot': lotacao})
        responses = cursor.fetchall()
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao: Lotacao procurada invalida')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    return responses

def selecionarLocalAluguelLotacao(aluguel,lotacao):
    """
        Retorna valores dos locais de acordo com o aluguel e lotacao
    """
    cursor = connection.cursor()
    statement = "SELECT NFANTASIA, ALUGUEL, AREA FROM LOCAL\
                    WHERE ALUGUEL = :aluguel AND LOTACAO = :lot"
    try:
        cursor.execute(statement, {'aluguel': aluguel,'lot': lotacao})
        responses = cursor.fetchall()
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao: Aluguel ou lotacao procurados invalidos')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    return responses

def selecionarLocalData(data):
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
        print('Erro de restricao: Data procurada invalida')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()
    return responses

def printLocais(local, atributos):
    print('Locais disponiveis')
    print(atributos)
    for i in xrange(len(local)):
        print("{}) {}\n".format(i,local[i]))