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
        print('2) Registrar Evento')
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
            cadastrarEvento()

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

def selecionarLocal(data):
    """
        Retorna o local escolhido de acordo com locais disponiveis na data
    """
    cursor = connection.cursor()
    print(data)
    statement = "SELECT L2.NFANTASIA,L2.LOTACAO,L2.ALUGUEL\
                        FROM LOCAL L2 \
                        JOIN EVENTO E\
                        ON E.LOCAL = L2.NFANTASIA\
                        WHERE E.DATA = TO_DATE('2019/02/20', 'yyyy/mm/dd')"
    cursor.execute(statement)
    responses = cursor.fetchall()
    print('Locais disponiveis')
    print('Nome, Locao e Aluguel')
    for res in responses:
        print(res)
    
    local = raw_input('Selecione o local')

    cursor.close()

    return local

def inserirColacao():
    while True:
        print('Insira informacoes a respeito da colacao')
        nro = _NRO
        print(nro)
        tema = raw_input('Insira o tema:\n')
        descricao = raw_input('Insira a descricao:\n')
        data = raw_input('Insira a data (yyyy/mm/dd):\n')
        local = selecionarLocal(data)
        
        tipo = 'COLACAO'

        statament_colacao = "INSERT INTO EVENTO (NRO,TEMA,DATA,DESCRICAO,LOCAL,TIPO)\
                    VALUES(:nro, :tema, to_date(:data, 'yyyy/mm/dd'), :descricao, :local, :tipo)"
        
        try:
            cursor.execute(statament_colacao, {'nro':nro, 'tema':tema, 'data':data, 'descricao':descricao, 'local':local, 'tipo':tipo})    
            break
        except (cx_Oracle.IntegrityError):
            print('Erro de restricao: con')
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)
        
def inserirFestaFormatura():
    while True:
        print('Insira informacoes a respeito da festa de formatura')
        nro = _NRO
        print(nro)
        tema = raw_input('Insira o tema:\n')
        descricao = raw_input('Insira a descricao:\n')
        data = raw_input('Insira a data (yyyy/mm/dd):\n')
        local = selecionarLocal(data)

        tipo = 'FESTAFORMATURA'

        statament_formatura = "INSERT INTO EVENTO (NRO,TEMA,DATA,DESCRICAO,LOCAL,TIPO)\
                    VALUES(:nro, :tema, to_date(:data, 'yyyy/mm/dd'), :descricao, :local, :tipo)"

        try:
            cursor.execute(statament_formatura, {'nro':nro, 'tema':tema, 'data':data, 'descricao':descricao, 'local':local, 'tipo':tipo})    
            break
        except (cx_Oracle.IntegrityError):
            print('Nro de evento ja existe ou local nao existe')
        except cx_Oracle.Error:
            print(cx_Oracle.Error.message)
        

def cadastrarEvento():
    print (cx_Oracle.clientversion())
    cursor = connection.cursor()
    if(raw_input('Deseja registrar um novo evento? (s/n)\n') == 's'):
        if(raw_input('Evento sera uma formatura ou casamento? (f/c)\n') == 'f'):
                inserirFestaFormatura()
                if(raw_input('A formatura tera colacao? (s/n)\n') == 's'):
                    inserirColacao()

            

        raw_input('Pressione enter para voltar ao menu')
        connection.commit()
            
    cursor.close()

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
    menu()


if __name__ == '__main__':
    dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
    connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)
    # Pegando numero de eventos para gerar os ids do evento
    cursor = connection.cursor()
    cursor.execute('select COUNT(NRO) from EVENTO')
    _NRO = cursor.fetchone()[0] + 1
     
    main()