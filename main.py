import os
import time
import cx_Oracle
from crud import * # MUDAR SO PARA PUXAR AS FUNCOES QUE USA MESMO

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

if __name__ == '__main__':
    menu()
