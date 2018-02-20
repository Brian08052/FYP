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
from sense import *
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

xB = 11112

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass
  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass
  return False

def prepSearchString(string):
  s = string.split(',')
  for i in s:
    if not is_number(i):
      return False
  return True

def fill0s(i, l):
  retString = ''
  si = str(i)
  if len(si)<l:
    for i in range(len(si)-l):
      retString += '0'

  retString += str(i)
  return(retString)


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
    	connection = db.connect('cs1.ucc.ie', 'bgl1', SQLP, '2018_bgl1')
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

def generateAltY(yAx):
  print(yAx)
  percentLosses = []
  yAx2 = []
  yAx2 += [yAx[0]]
  yAx2 += [yAx[1]]

  for i in range(2, len(yAx)):
    print(yAx[i])
    if(yAx[i] == 0):
      yAx2 += [0]
    else:
      loss = yAx[i-2] - yAx[i-1]

      percentLosses += [loss/yAx[i-2]]
      averageLoss = sum(percentLosses)/len(percentLosses)
      print('i:', i)
      yAx2 += [yAx[i-1]*averageLoss]
  return yAx2



def createGraph(arrayString, imageName):#, methodType, lossFunction = 'x'):
  #Accepts clean array
  arrayString = arrayString[1:len(arrayString)-1] #For some reason there were quotation marks at the start and end breaking it.
  #print('\n\n Array String:', arrayString, '\n\n',)
  array1 = arrayString
  array2 = []
  xAx = []
  yAx = []

  #if methodType == x:
  s2 = arrayString.split(',')
  #print('\ns2: ', s2)
  xAx = []
  yAx = []
  i = 0

  for n in s2:
    if n != '':
        xAx += [i]
        yAx += [int(n)]
    i += 1

  yAx2 = generateAltY(yAx)


  #return xAx, yAx
  plt.plot(xAx, yAx, linewidth=2.0)
  plt.plot(xAx, yAx2, linewidth=2.0)
  #plt.plot(xAx2, yAx2, linewidth=2.0)

  plt.draw()
  plt.savefig('image')

  losses = []

  for i in range(2, len(xAx)):
    losses += [(yAx[i]-yAx2[i])**2]



  return sum(losses)/len(losses)

    
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

def createDictionary(dataID):
    d = {}
    cursor = getCursor()
    string = ("""select * from fypDB where dataID = '%s'"""%(dataID))
    cursor.execute(string)
    for row in cursor.fetchall():
        d[row['sampleID']] = row['sampleData']
        #print(row['sampleID'])
    return d

def getLastUpdate(dataID):
  #returns the the datetime of the last entry to the table
  #returns None if table doesnt exist
  #Note: date time doesn't refect if something has been deleted
    cursor = getCursor()
    string = ("""select max(created) from fypDB where dataID = '%s'"""%(dataID))
    cursor.execute(string)
    for row in cursor.fetchall():
        s = row['max(created)']
    return s

def getFileName(dataID):
  return str(dataID) + 'Dic' 

def createPickle(dataID):
  d = createDictionary(dataID)
  fileName = getFileName(dataID)
  file = open(fileName, 'w+')
  pickle.dump(d, afile)

def getDicFromPickle(dataID):
  fileName = getFileName(dataID)
  file2 = open(fileName, 'rb')
  new_d = pickle.load(file2)
  file2.close()
  return new_d

  

