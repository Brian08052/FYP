#!/usr/local/bin/python3
from code import *
from cgitb import enable 
enable()
import cgitb
import cgi
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
import pymysql as db
from sense import *
from code import *

print('Content-Type: text/html')
print()

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
  #I have no idea what this is for. Takes in an int i and converts it to a string adding l 0s onto the end.
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




def getEachArraySegment(rawDictionary):
  d = rawDictionary
  arrays = []
  for key in d:

    sample = strToArray(d[key])
    #print('<br><H>', key, '</H><br>')
    #print(sample, '<br><br>')

    localArray = []
    for i in range(len(sample)):
      #print(localArray, '<br>')
      if sample[i] != None:
        if sample[i] > 0:
          #print('Adding ', sample[i])
          localArray += [sample[i]]
      else:
        if len(localArray)>1:
          arrays += [localArray]
          localArray = []


  #print('la: ', len(arrays))
  return arrays



#************************************************************************************************
def getRawDictionary(dbID):
  return createDictionary(dbID)

def getCleanDictionary(dbID):
  d = getRawDictionary(dbID)
  return cleanDict(d)

def getCleanDic(dataID):
    return cleanDict(createDictionary(dataID))

#f = open('txt', 'w+')
def createDictionary(dataID):
    d = {}
    cursor = getCursor()
    string = ("""select * from fypDB where dataID = '%s'"""%(dataID))
    cursor.execute(string)
    for row in cursor.fetchall():
        #print(row['sampleData'])
        d[row['sampleID']] = row['sampleData'].decode("utf-8") 
        #print(row['sampleID'])
    return d


def printData():
  dbID = 'cancerMolar'
  raw = getRawDictionary(dbID)
  clean = getCleanDictionary(dbID)
  dl = [raw, clean]
  for dic in dl:
    for key in dic:
      print(key, '<br>')
      print(dic[key], '<br>')

    print('<br><br>')
  arrays = getEachArraySegment(raw)
  print('<H>ARRAYS</H>')
  for a in arrays:
    print(a, '<br>')

arrays = getEachArraySegment(getRawDictionary('CancerMolar'))
#print('x')

#print(getCleanDic('CancerMolar'))
# cleanD = getCleanDic('CancerMolar')
# for key in cleanD:
#   print(cleanD[key], '<br>')

#rawD = getRawDictionary('CancerMolar')
#print('RD', rawD[8628], '<br>', cleanSample(strToArray(rawD[8628])) )