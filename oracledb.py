#!/usr/bin/env python
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
		print('1) ')
		print('2) ')
		print('3) ')
		print('4) ')
		print('5) ')
		print('6) Sair')
		#le a opcao desejada
		opcao = input()
		#limpa a tela
		os.system('clear')

		if (opcao == 1):
			print (opcao)

		elif (opcao == 2):
			print (opcao)

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


def get_all_rows(label, data_type='uniforme'):
	#Querry all rows
	cursor = connection.cursor()
	print (cursor)


dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)

print (cx_Oracle.clientversion())

cursor = connection.cursor()


#Select 1
statament = 'select * from time'
cursor.execute(statament)
response = cursor.fetchall()
print (len(response))
for i in response:
    print (i)

print ('-----------------------------')


#Select 2 (Positional)
#saldo_gols = input()
saldo_gols = 20
cursor.execute('SELECT * \
                FROM time \
                WHERE estado = :1 AND saldo_gols> :2', ('SP', saldo_gols))
for i in cursor:
    print (i)


print ('-----------------------------')


#Select 3 (Named)
cursor.execute('SELECT * \
                FROM time \
                WHERE estado= :estado AND saldo_gols>= :saldo', {'estado':'SP', 'saldo':20})
#dict =  {i[0]: None for i in cursor.description}
#print dict
for i in cursor:
    print (i)


print ('---------------------------------')


#Juntando Select 1 com 3
estado = 'SP'
saldo = 20
statament = ('SELECT * \
                FROM time \
                WHERE estado= :estado AND saldo_gols>= :saldo')
cursor.execute(statament, {'estado':estado, 'saldo': saldo})

dict =  {i[0]: [] for i in cursor.description}
print (dict)

response = cursor.fetchall()
print (response)
cursor.close()

connection.close()