from cgitb import enable 
from code import *
enable()
import cgitb
import cgi
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db
from os import environ

def idCode(sampleID):
  s = ''
  for i in range (4 - len(str(sampleID))):
    s += '0'
  return(s + str(sampleID))
  

def dataCheck(data):
  if(False):
    return('bad data because')
  else:
    return('ok')

def getCursor():
    try:
    	connection = db.connect('cs1.ucc.ie', 'bgl1', 'maGhii6o', '2018_bgl1')
    	cursor = connection.cursor(db.cursors.DictCursor)
    	return cursor
    except (db.Error, IOError) as e:
    	print("Database error in code.py")
    	print(e)
    	return e

def getData(cursor, dataID, sampleID):
  try:
  	statement = """select * from fypDB where dataID = '{0}' and sampleID = '{1}'""".format(dataID, sampleID)
  	cursor.execute(statement)
  	for row in cursor.fetchall():
  		return(row['sampleData'])
  except (db.Error, IOError) as e:
  	print("Database error in getData code.py")
  	print(e)

def getDatabaseNames(cursor):
  try:
    connection = db.connect('cs1.ucc.ie', 'bgl1', 'maGhii6o', '2018_bgl1')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""select distinct dataID from fypDB""")
  except (db.Error, IOError) as e:
      print(e)

  return cursor.fetchall()


def uploadData(cursor, dataID, sampleID, text_content):
  insert = """insert into fypDB (dataID, sampleID, sampleData, created, lastUpdated) values('%s', %s, '%s', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"""%(dataID, sampleID, text_content)
  cursor.execute(insert)
  cursor.execute('COMMIT')
    
"""

def updateDataframe(dataID):
	#This means you need a set number of weeks, or have it as a constant in the database
	lst = []
  return
	#for each row in the dataframe if the row isnt in the DB 
	#if its not delete it?
	#for each fow in the fetchall[data]:
		#check if the ID is in the dataframe already

		#if not add it?
		#split on ','
		#df = df.append(pd.DataFrame(list, columns=['col1','col2']),ignore_index=True)
		#something better than having each column name surely 
		#then i think it should be ok to just add them to a dataframe?
		#one by one?
"""