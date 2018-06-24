import os
import time
import cx_Oracle

dsn = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
connection = cx_Oracle.connect(user='L4182085', password='041097l$', dsn=dsn)
   
def readNotNullAttribute(varName):
        notCompleted = True
        while(notCompleted):
            print('Informe '+varName+' (NAO PODE SER NULO):')
            varValue = raw_input()
            if varValue.strip():
                notCompleted = False    
        return varValue
     
def readAttribute(varName):
        print('Informe '+varName+' :')
        varValue = raw_input()
        if varValue.strip():
                varValue = 'NULL'
        return varValue
