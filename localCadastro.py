from crud import *

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