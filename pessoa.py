from crud import *

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
        tel = readAttribute("telefone")

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
        curso = readAttribute("curso")
        inst = readAttribute("instituicao")

        statement = 'INSERT INTO FORMANDO(CPF, CURSO, INSTITUICAO) \
                     VALUES(:CPF, :curso, :inst)'
        try:
            cursor.execute(statement, {'curso': curso, 'inst': inst, 'CPF': CPF})
            break
        except cx_Oracle.IntegrityError:
            print("Erro de restricao.")
            print("Possiveis erros: ")
            print("\t- Curso ou Instituicao muito longos")
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
                nome = readAttribute("comissao")
                aux = inserirForma(CPF, nome)


def inserirFuncionario(CPF):
    cursor = connection.cursor()
    
    while(True):
        cargo = readAttribute("cargo")
        end = readAttribute("endereco")
        ct = readAttribute("carteira de trabalho (xxx.xxxxx.xx-x")
        salario = float(readAttribute("salario"))
        ord_serv = int(readAttribute("ordem de servico"))

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
        CPF = readNotNullAttribute("CPF (xxx.xxx.xxx-xx): ")
        nome = readAttribute("nome")
        tipo = readAttribute("tipo (Noivo, Formando ou Funcionario)")

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
            tel = readAttribute("telefone")

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
            curso = readAttribute("curso")

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
            inst = readAttribute("instituicao")

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
            cargo = readAttribute("cargo")

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
            end = readAttribute("endereco")

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
            ct = readAttribute("carteira de trabalho")

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
            salario = readAttribute("salario")

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
        CPF = readNotNullAttribute("CPF da pessoa para modificacao")
        statement = 'SELECT TIPO \
                     FROM PESSOA \
                     WHERE CPF = :CPF'
        try:
            cursor.execute(statement, {'CPF': CPF})
            response = cursor.fetchone()[0]
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
            nome = readAttribute("nome")

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
   
    cursor.close()
    
    if(response.upper() == 'NOIVO'):
        updateNoivo(CPF)
    elif(response.upper() == 'FORMANDO'):
        updateFormando(CPF)
    elif(response.upper() == 'FUNCIONARIO'):
        updateFuncionario(CPF)


def deletePessoa():
    cursor = connection.cursor()

    while(True):
        CPF = readNotNullAttribute("CPF a ser deletado")
        statement = 'DELETE FROM PESSOA \
                     WHERE CPF = :CPF'
  
        try:
            cursor.execute(statement, {'CPF':CPF})
            break
        except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- CPF invalido")
        except cx_Oracle.Error:
                print(cx_Oracle.Error.message)
    
    cursor.close()


"""
    - Select somente a PESSOA
    - Select JOIN com o TIPO dela
    - 
"""
def searchPessoa():
    cursor = connection.cursor()

    while(True):
        CPF = readNotNullAttribute("CPF da pessoa para busca")
        statement = 'SELECT TIPO FROM PESSOA WHERE CPF = :CPF'

        try:
            cursor.execute(statement, {'CPF':CPF})
            response = cursor.fetchone()[0]  
            break
        except cx_Oracle.IntegrityError:
                print("Erro de restricao.")
                print("Possiveis erros: ")
                print("\t- CPF invalido")
        except cx_Oracle.Error:
                print(cx_Oracle.Error.message)

    if(response.upper() == 'NOIVO'):
        updateNoivo(CPF)
    elif(response.upper() == 'FORMANDO'):
        updateFormando(CPF)
    elif(response.upper() == 'FUNCIONARIO'):
        updateFuncionario(CPF)

    cursor.close()

def gerenciarPessoas():
    print('[GERENCIADOR DE PESSOAS] Selecione o numero da opcao desejada:')
    print('1) Cadastrar uma pessoa')
    print('2) Atualizar dados de uma pessoa')
    print('3) Remover uma pessoa')
    print('4) Pesquisar uma pessoa')

    pessoasAux = int(input())

    if (pessoasAux == 1):
        inserirPessoa()
        connection.commit()
        print("Cadastro completo!")
        raw_input("Pressione qualquer tecla para continuar...")
    elif (pessoasAux == 2):
        updatePessoa()
        connection.commit()
        print("Atualizacao completa!")
        raw_input("Pressione qualquer tecla para continuar...")
    elif (pessoasAux == 3):
        deletePessoa()
        connection.commit()
        print("Remocao completa!")
        raw_input("Pressione qualquer tecla para continuar...")
    elif (pessoasAux == 4):
        searchPessoa()
        print("Busca completa!")
        raw_input("Pressione qualquer tecla para continuar...")
    else:
        print("Opcao Invalida")