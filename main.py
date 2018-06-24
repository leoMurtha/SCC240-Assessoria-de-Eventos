import os
import time
import cx_Oracle
from evento import *

#loop para mostrar o menu
def menu():
    while (True):
        #limpa a tela toda vez que entrar no menu
        os.system('clear')
        #mostra as opcoes disponiveis
        print('[MENU INICIAL] Selecione o numero da opcao desejada:')
        print('1) Gerenciar Pessoa') # CRUD de pessoas (clientes e funcionarios)
        print('2) Gerenciar Eventos') # CRUD e todo o processo de cadastro de eventos
        print('3) Gerenciar Locais') # CRUD de Locais
        print('4) Gerenciar Servicos') # Por semantica, soh consulta, update e delete (sem insercao, so faz sentido junto a um evento)
        print('6) Sair')
        #le a opcao desejada
        opcao = int(input())
        #limpa a tela
        os.system('clear')

        if (opcao == 1):
            print('[GERENCIADOR DE PESSOAS] Selecione o numero da opcao desejada:')
            print('1) Cadastrar uma pessoa')
            print('2) Atualizar dados de uma pessoa')
            print('3) Deletar uma pessoa')
            print('4) Pesquisar uma pessoa')

            opcao = int(input())

            if (opcao == 1):
                inserirPessoa()
                connection.commit()
                print("Cadastro completo!")
                raw_input("Pressione qualquer tecla para continuar...")        
            elif (opcao == 2):
                updatePessoa()
                connection.commit()
                print("Atualizacao completa!")
                raw_input("Pressione qualquer tecla para continuar...")        
            elif (opcao == 3):
                print("oi")
            elif (opcao == 4):
                print("oi")
            else:
                print("Opcao Invalida")

            inserirPessoa()

        elif (opcao == 2):
            cadastrarEvento()
            print (opcao)

        elif (opcao == 3):
            gerenciarLocal()

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

if __name__ == '__main__':
    menu()
