from crud import *


def alterarLocal():
    exitL = False
    while(not exitL):
        os.system('clear')
        print('Escolha o atributo a ser alterado:')
        print('1) Area') 
        print('2) Lotacao') 
        print('3) Aluguel') 
        print('4) Endereco') 
        print('5) Telefone') 
        print('6) Nome do proprietario') 
        print('7) Voltar')
        opcao = input()
        os.system('clear')

        if(opcao == 1):
            alterarArea()
        elif(opcao == 2):
            alterarLotacao()
        elif(opcao == 3):
            alterarAluguel()
        elif(opcao == 4):
            alterarEndereco()
        elif(opcao == 5):
            alterarTelefone()
        elif(opcao == 6):
            alterarNomeProp()
        elif(opcao == 7):
            exitL = True
        

def alterarArea():
    nome = readNotNullAttribute('Nome do local a ser alterado')
    area = readAttribute('nova Area')
    updateLocalArea(area,nome)
    connection.commit()
    raw_input('Insercao realizada!Continuar? ')

def alterarLotacao():
    nome = readNotNullAttribute('Nome do local a ser alterado')
    lot = readAttribute('nova lotacao')
    updateLocalLotacao(lot,nome)
    connection.commit()
    raw_input('Insercao realizada!Continuar? ')

def alterarAluguel():
    nome = readNotNullAttribute('Nome do local a ser alterado')
    alug = readAttribute('novo aluguel')
    updateLocalAluguel(alug,nome)
    connection.commit()
    raw_input('Insercao realizada!Continuar? ')

def alterarEndereco():
    nome = readNotNullAttribute('Nome do local a ser alterado')
    end = readAttribute('novo endereco')
    updateLocalEndereco(end,nome)
    connection.commit()
    raw_input('Insercao realizada!Continuar? ')

def alterarTelefone():
    nome = readNotNullAttribute('Nome do local a ser alterado')
    tel = readAttribute('novo telefone')
    updateLocalTelefone(tel,nome)
    connection.commit()
    raw_input('Insercao realizada!Continuar? ')

def alterarNomeProp():
    nome = readNotNullAttribute('Nome do local a ser alterado')
    nprop = readAttribute('novo nome proprietario')
    updateLocalNProp(nprop,nome)
    connection.commit()
    raw_input('Insercao realizada! Continuar? ')

def updateLocalArea(newValue,nFant):
    cursor = connection.cursor()
    statement = 'UPDATE LOCAL \
                 SET AREA = :newValue \
                 WHERE NFANTASIA = :nfant'
    
    try:
        cursor.execute(statement, {'newValue' : newValue,'nfant' : nFant})
    except cx_Oracle.IntegrityError:
        print("Erro de restricao: valor de area invalida")
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False
    
    cursor.close()
    return True  

def updateLocalLotacao(newValue,nFant):
    cursor = connection.cursor()
  
    statement = 'UPDATE LOCAL \
                 SET LOTACAO = :newValue \
                 WHERE NFANTASIA = :nfant'
    
    try:
        cursor.execute(statement, {'newValue' : newValue,'nfant' : nFant})
    except cx_Oracle.IntegrityError:
        print("Erro de restricao: valor de lotacao invalida")
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False
    
    cursor.close()
    return True  

def updateLocalAluguel(newValue,nFant):
    cursor = connection.cursor()
  
    statement = 'UPDATE LOCAL \
                 SET ALUGUEL = :newValue \
                 WHERE NFANTASIA = :nfant'
    
    try:
        cursor.execute(statement, {'newValue' : newValue,'nfant' : nFant})
    except cx_Oracle.IntegrityError:
        print("Erro de restricao: valor de aluguel invalida")
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False
    
    cursor.close()
    return True  

def updateLocalEndereco(newValue,nFant):
    cursor = connection.cursor()
    
    statement = 'UPDATE LOCAL \
                 SET ENDERECO = :newValue \
                 WHERE NFANTASIA = :nfant'
    
    try:
        cursor.execute(statement, {'newValue' : newValue,'nfant' : nFant})
    except cx_Oracle.IntegrityError:
        print("Erro de restricao: valor de endereco invalida")
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False
    
    cursor.close()
    return True  

def updateLocalTelefone(newValue,nFant):
    cursor = connection.cursor()
   
    statement = 'UPDATE LOCAL \
                 SET TELEFONE = :newValue \
                 WHERE NFANTASIA = :nfant'
    
    try:
        cursor.execute(statement, {'newValue' : newValue,'nfant' : nFant})
    except cx_Oracle.IntegrityError:
        print("Erro de restricao: valor de telefone invalida")
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False
    
    cursor.close()
    return True 

def updateLocalNProp(newValue,nFant):
    cursor = connection.cursor()
    
    statement = 'UPDATE LOCAL \
                 SET NPROPRIETARIO = :newValue \
                 WHERE NFANTASIA = :nfant'
    
    try:
        cursor.execute(statement, {'newValue' : newValue,'nfant' : nFant})
    except cx_Oracle.IntegrityError:
        print("Erro de restricao: valor do nome do proprietario invalido")
        return False
    except cx_Oracle.Error:
        print(cx_Oracle.Error.message)
        return False
    
    cursor.close()
    return True 