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
        print('4) Sair')
        #le a opcao desejada
        opcao = int(input())
        #limpa a tela
        os.system('clear')

        if (opcao == 1):
            gerenciarPessoas()

        elif (opcao == 2):
            gerenciarEvento()
            print (opcao)

        elif (opcao == 3):
            gerenciarLocal()

        elif (opcao == 4):
            print (opcao)
            exit()
        else:
            print('Opcao invalida. Selecione uma nova opcao.')
            time.sleep(2)

if __name__ == '__main__':
    menu()
