from crud import *
from local import *
from pessoa import *

def inserirEvento(tipo):
    cursor = connection.cursor()
    
    # Gerando o id do evento
    cursor.execute('select COUNT(NRO) from EVENTO')
    nro = cursor.fetchone()[0] + 1
        
    while True:
        print('Insira informacoes sobre ' + tipo)
        
        tema = readAttribute('tema')
        descricao = readAttribute('descricao')
        data = readNotNullAttribute('data (yyyy/mm/dd)')
        locais = selecionarLocalData(data)
        
        printLocais(locais,'Nome, Locacao e Aluguel')
        local = locais[int(input('Digite o numero do local escolhido: '))][0]
        
        
        statament = "INSERT INTO EVENTO (NRO,TEMA,DATA,DESCRICAO,LOCAL,TIPO)\
                    VALUES(:nro, :tema, to_date(:data, 'yyyy/mm/dd'), :descricao, :local, :tipo)"
        
        statament_2 = ''
        if(tipo == 'FESTAFORMATURA'):
            statament_2 = "INSERT INTO FESTA_FORMATURA (NRO) VALUES(:nro)"    
        elif(tipo == 'COLACAO'):
            statament_2 = "INSERT INTO COLACAO (NRO) VALUES(:nro)"

        try:
            cursor = connection.cursor()
            cursor.execute(statament, {'nro':nro, 'tema':tema, 'data':data, 'descricao':descricao, 'local':local, 'tipo':tipo})    
            cursor.execute(statament_2, {'nro':nro})    
            cursor.close()
            connection.commit()
            return nro
        except (cx_Oracle.IntegrityError):
            print('Erro de restricao, possiveis erros:\n-Local Invalido\n-Data I')
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)

def acharComissao(nome):
    statament = "SELECT C.NOME FROM COMISSAO C WHERE UPPER(NOME) = UPPER(:nome)"

    try:
        cursor = connection.cursor()
        cursor.execute(statament, {'nome':nome})
        if(cursor.fetchone() != None):
            return False
        else:
            return True
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        cursor.close()
        return True
      
def inserirFormatura(comissao, festa, colacao):
    cursor = connection.cursor()
    statament_formatura = "INSERT INTO FORMATURA (COMISSAO, FESTA, COLACAO)\
                VALUES(:comissao, :festa, :colacao)"

    try:
        cursor = connection.cursor()
        cursor.execute(statament_formatura, {'comissao': comissao, 'festa': festa, 'colacao': colacao})    
        cursor.close()
        connection.commit()
        print('Formatura Inserida...')
    except (cx_Oracle.IntegrityError):
        print(cx_Oracle.IntegrityError.message)
        print('Erro de restricao, possiveis erros:\n-Comissao invalida\n-Festa invalida')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
    
def cadastrarFormatura():
    cursor = connection.cursor()
    festa = inserirEvento('FESTAFORMATURA')
    c = input('Deseja criar uma nova comissao para a formatura (1) ou associa-la a uma existente (2)?: (Digite: 1 ou 2): ')
    if(c == 1):
            comissao = inserirComissao()
    elif (c == 2):
        comissao = raw_input('Insira o nome da comissao existente: ')
        while acharComissao(comissao): 
            comissao = raw_input('Formatura nao foi encontrada, digite novamente: ')
        print('Comissao encontrada associando-a com a formatura')
            
    if(raw_input('A formatura tera colacao? (s/n)\n') == 's'):
        colacao = inserirEvento('COLACAO')
    else:
        colacao = 'NULL'
            
    inserirFormatura(comissao, festa,colacao)

    raw_input('Pressione enter para voltar ao menu')
            
    cursor.close()

def consultarPorComissao():
    comissao = readNotNullAttribute('nome da comissao existente: ')
    while acharComissao(comissao): 
        comissao = raw_input('Formatura nao foi encontrada, digite novamente: ')
    
    cursor = connection.cursor()
    statement = "SELECT E1.TEMA, E1.DESCRICAO, E1.DATA, E2.TEMA, E2.DESCRICAO, E2.DATA FROM FORMATURA F\
                    INNER JOIN EVENTO E1 ON E1.NRO = F.FESTA\
                    LEFT JOIN EVENTO E2 ON E2.NRO = F.COLACAO\
                    WHERE UPPER(F.COMISSAO) = UPPER(:comissao)"
    try:
        cursor.execute(statement, {'comissao': comissao})
        responses = cursor.fetchall()
        print('Formaturas pela comissao: ' + comissao)
        for res in responses:
            print(res)

    except (cx_Oracle.IntegrityError):
        print('Erro de restricao')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()
    
    raw_input('Pressione enter para voltar')
        
def consultarPorLocal():
    local = readNotNullAttribute('local')

    cursor = connection.cursor()
    statement = "SELECT F.FESTA, F.COLACAO, F.COMISSAO FROM FORMATURA F\
                    INNER JOIN EVENTO E ON E.NRO = F.FESTA\
                    WHERE UPPER(E.LOCAL) = UPPER(:local)"
    try:
        cursor.execute(statement, {'local': local})
        responses = cursor.fetchall()
        
        print('Formaturas no local : ' + local)
        for res in responses:
            print(res)

        
    except (cx_Oracle.IntegrityError):
        print('Erro de restricao: Valores inseridos invalidos')
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)

    cursor.close()

    raw_input('Pressione enter para voltar')

def consultarPorData():
    data = readNotNullAttribute('data (yyyy/mm/dd)')

    cursor = connection.cursor()
    statement = "SELECT E1.TEMA, E1.DESCRICAO, E1.DATA FROM FORMATURA F\
                    INNER JOIN EVENTO E1 ON E1.NRO = F.FESTA\
                    WHERE E1.DATA = TO_DATE(:data, 'yyyy/mm/dd')"
    try:
        cursor.execute(statement, {'data': data})
        responses = cursor.fetchall()
    
        print('Formaturas na data : ' + data)
        for res in responses:
            print(res)

    except cx_Oracle.Error:
        print(cx_Oracle.Error)

    cursor.close()

    raw_input('Pressione enter para voltar')
        
def consultasFormatura():
    os.system('clear')
    print('[CONSULTAS DE LOCAIS] Selecione o numero da opcao de desejada:')
    print('1)Consultar formaturas por comissao') 
    print('2)Consultar formaturas por local') 
    print('3)Consultar formaturas data')
    print('4) Voltar')
    opcao = input()
    os.system('clear')

    if(opcao == 1):
        consultarPorComissao()
    elif(opcao == 2):
        consultarPorLocal()
    elif(opcao == 3):
        consultarPorData()

def gerenciarEvento():
    exitL = False
    while(not exitL):
        os.system('clear')
        #mostra as opcoes disponiveis
        print('[MENU DE EVENTOS] Selecione o numero da opcao de desejada:')
        print('1) Cadastrar formatura') # Inserts
        print('2) Consultas formatura') # Selects
        print('3) Voltar')
        opcaoE = input()
        
        os.system('clear')

        if(opcaoE == 1):
            cadastrarFormatura()
        elif(opcaoE == 2):
            consultasFormatura()
        elif(opcaoE == 3):
            exitL = True
        else:
            print('Opcao invalida. Selecione uma nova opcao.')