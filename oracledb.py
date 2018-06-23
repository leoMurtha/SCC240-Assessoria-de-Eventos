#!/usr/bin/env python
import os
import time
import cx_Oracle


# loop para mostrar o menu
def menu():
    while (True):
        # limpa a tela toda vez que entrar no menu
        os.system('clear')
        # mostra as opcoes disponiveis
        print('Selecione uma opcao:')
        print('1) ')
        print('2) ')
        print('3) ')
        print('4) ')
        print('5) ')
        print('6) Sair')
        # le a opcao desejada
        opcao = input()
        # limpa a tela
        os.system('clear')

        if (opcao == 1):
            print(opcao)

        elif (opcao == 2):
            print(opcao)

        elif (opcao == 3):
            print(opcao)

        elif (opcao == 4):
            print(opcao)

        elif (opcao == 5):
            print(opcao)

        elif (opcao == 6):
            print(opcao)
            exit()
        else:
            print('Opcao invalida. Selecione uma nova opcao.')
            time.sleep(2)


def connect():
	dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
	
	connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)

	print(cx_Oracle.clientversion())
	print('Connected to oracle DB...\n')
	

	return connection

def main():
    
	conn = connect()
	
	cursor = conn.cursor()

	# Select 1
	statament = 'select * from time'
	cursor.execute(statament)
	
	time = {i[0]: [] for i in (cursor.description)}
	
	response = cursor.fetchall()
	for i in response:
		print(i)
		time['NOME'].append(i[0])
		time['ESTADO'].append(i[1])
		time['TIPO'].append(i[2])
		time['SALDO_GOLS'].append(i[3])
	
	
	
	conn.close()

if __name__ == '__main__':
    main()
