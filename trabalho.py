import os
import time
import cx_Oracle

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
            print("\t- Nome de comissao ivalido")
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
        salario = input("Digite o salario: ")
        ord_serv = input("Digite a ordem de servico: ")

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
            print("\t- Ordem de servico invalido")
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


def updateFormando(CPF):
    cursor = connection.cursor()

    resp = raw_input("Deseja alterar o curso? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            curso = raw_input("Digite o novo curso: ")

            statement = 'UPDATE FORMANDO \
                         SET CURSO = :curso \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'curso':curso, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Curso muito longo")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)
    

    resp = raw_input("Deseja alterar a instituicao? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            inst = raw_input("Digite a nova instituicao: ")

            statement = 'UPDATE FORMANDO \
                         SET INSTITUICAO = :inst \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'inst':inst, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Instituicao muito longa")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)
        
    cursor.close()


def updateFuncionario(CPF):
    cursor = connection.cursor()

    resp = raw_input("Deseja alterar o cargo? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            cargo = raw_input("Digite o novo cargo: ")

            statement = 'UPDATE FUNCIONARIO \
                         SET CARGO = :cargo \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'cargo':cargo, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Cargo muito longo")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)
    
    resp = raw_input("Deseja alterar o endereco? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            end = raw_input("Digite o novo endereco: ")

            statement = 'UPDATE FUNCIONARIO \
                         SET ENDERECO = :end \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'end':end, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Endereco muito longo")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)
    
    resp = raw_input("Deseja alterar a carteira de trabalho? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            ct = raw_input("Digite a nova carteira de trabalho: ")

            statement = 'UPDATE FUNCIONARIO \
                         SET CT = :ct \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'ct':ct, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Carteira de trabalho invalida")
            except cx_Oracle.Error:
                print(cx_Oracle.Error.message)

    resp = raw_input("Deseja alterar o salario? (Se sim, digite: S)")
    if(resp.upper() == 'S'):

        while(True):
            salario = raw_input("Digite o novo salario: ")

            statement = 'UPDATE FUNCIONARIO \
                         SET SALARIO = :salario \
                         WHERE CPF = :CPF'

            try:
                cursor.execute(statement, {'salario':salario, 'CPF':CPF})
                break
            except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- Carteira de trabalho invalida")
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
        updateNoivo(CPF)
    elif(response.upper() == 'FORMANDO'):
        updateFormando(CPF)
    elif(response.upper() == 'FUNCIONARIO'):
        updateFuncionario(CPF)


def main():
    inserirPessoa()
    connection.commit()


if __name__ == '__main__':
    dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
    connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)
    
    #main()

    c = raw_input()
    print type(c)
    print c
    
    d = int(c)
    print type(d)
    print d

    connection.close()



