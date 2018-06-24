from crud import *
from local import *
from pessoa import *

def inserirColacao():
    while True:
        print('Insira informacoes a respeito da colacao')
        cursor = connection.cursor()
        # Gerando o id do evento
        cursor.execute('select COUNT(NRO) from EVENTO')
        nro = cursor.fetchone()[0] + 1
        tema = raw_input('Insira o tema da colacao:\n')
        descricao = raw_input('Insira a descricao:\n')
        data = raw_input('Insira a data (yyyy/mm/dd):\n')
        local = selecionarLocal(data)
        
        tipo = 'COLACAO'

        statament_colacao = "INSERT INTO EVENTO (NRO,TEMA,DATA,DESCRICAO,LOCAL,TIPO)\
                    VALUES(:nro, :tema, to_date(:data, 'yyyy/mm/dd'), :descricao, :local, :tipo)"
        
        try:
            cursor.execute(statament_colacao, {'nro':nro, 'tema':tema, 'data':data, 'descricao':descricao, 'local':local, 'tipo':tipo})    
            cursor.close()
            connection.commit()
            break
        except (cx_Oracle.IntegrityError):
            print('Erro de restricao: con')
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)
        
def inserirFestaFormatura():
    while True:
        print('Insira informacoes a respeito da festa de formatura')
        cursor = connection.cursor()
        # Gerando o id do evento
        cursor.execute('select COUNT(NRO) from EVENTO')
        nro = cursor.fetchone()[0] + 1
        
        tema = raw_input('Insira o tema:\n')
        descricao = raw_input('Insira a descricao:\n')
        data = raw_input('Insira a data (yyyy/mm/dd):\n')
        local = selecionarLocal(data)

        tipo = 'FESTAFORMATURA'

        statament_formatura = "INSERT INTO EVENTO (NRO,TEMA,DATA,DESCRICAO,LOCAL,TIPO)\
                    VALUES(:nro, :tema, to_date(:data, 'yyyy/mm/dd'), :descricao, :local, :tipo)"

        try:
            cursor = connection.cursor()
            cursor.execute(statament_formatura, {'nro':nro, 'tema':tema, 'data':data, 'descricao':descricao, 'local':local, 'tipo':tipo})    
            cursor.close()
            connection.commit()
            break
        except (cx_Oracle.IntegrityError):
            print('Nro de evento ja existe ou local nao existe')
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)

def acharComissao(nome):
    statament = "SELECT C.NOME FROM COMISSAO C WHERE UPPER(NOME) = UPPER(:nome)"

    try:
        cursor = connection.cursor()
        cursor.execute(statament, {'nome':nome})
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        cursor.close()
        return True
    
    for res in cursor.fetchone():
        if res:
            cursor.close()
            return False
        else:
            cursor.close()
            return True

def inserirFormatura(festa, comissao, colacao):
    pass

def cadastrarEvento():
    print (cx_Oracle.clientversion())
    cursor = connection.cursor()
    if(raw_input('Deseja registrar um novo evento? (s/n)\n') == 's'):
        if(raw_input('Evento sera uma formatura ou casamento? (f/c)\n') == 'f'):
                inserirFestaFormatura()
                c = input('Deseja criar uma nova comissao para a formatura (1) ou associa-la a uma existente (2)?: (Digite: 1 ou 2): ')
                if(c == 1):
                    nome = inserirComissao()
                elif (c == 2):
                    nome = raw_input('Insira o nome da comissao existente: ')
                    while acharComissao(nome): 
                        nome = raw_input('Formatura nao foi encontrada, digite novamente: ')
                    print('Comissao encontrada associando-a com a formatura')
                if(raw_input('A formatura tera colacao? (s/n)\n') == 's'):
                    pass
                    # PEGAR A COLACAO PRA LINKAR COM FORMATURA
                    #colacao = inserirColacao()

            

        raw_input('Pressione enter para voltar ao menu')
            
    cursor.close()