#!/usr/local/bin/python3
from code import *
from clean import *
from searchCode import *
from pickles import *
from cgitb import enable 
enable()
import math
import numpy
import random
from code import *
import pymysql as db
from sense import *
import pickle

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
  return 'Dic' + str(dataID)

def createPickleWithDic(dataID, d):
    fileName = getFileName(dataID)
    file = open(fileName, 'wb+')
    pickle.dump(d, file)
    file.close()
    return
    
def createPickle(dataID):
  d = createDictionary(dataID)
  fileName = getFileName(dataID)
  file = open(fileName, 'wb+')
  pickle.dump(d, file)
  file.close()
  return

def updatePickle(dataID):
    #not sure if this overwrites it, or if you need to clear it first
    createPickle(dataID)

    
def getDicFromPickle(dataID):
  fileName = getFileName(dataID)
  file2 = open(fileName, 'rb')
  new_d = pickle.load(file2)
  file2.close()
  return new_d

def getUpdateDic():
    file2 = open('updates', 'rb')
    new_d = pickle.load(file2)
    file2.close()
    return new_d

def saveUpdateDic(dic):
    file = open('updates', 'wb+')
    pickle.dump(dic, file)
    file.close()


def getCursor():
    try:
    	connection = db.connect('cs1.ucc.ie', 'bgl1', SQLP, '2018_bgl1')
    	cursor = connection.cursor(db.cursors.DictCursor)
    	return cursor
    except (db.Error, IOError) as e:
    	print("Database error in code.py")
    	print(e)
    	return e

def refreshPickles():
    d = getUpdateDic()
    cursor = getCursor()
    string = ("""select distinct dataID, created from fypDB""")
    cursor.execute(string)
    for row in cursor.fetchall():
        if row['dataID'] not in d:
            createPickle(row['dataID'])
        elif d[row['dataID']] != row['created']:
            updatePickle(row['dataID'])
    
#d = createPickle('CancerMolar')
#refreshPickles()

def cleanPickle(dataID):
    d = getDicFromPickle(dataID)
    d = cleanDic(d)
    updatePickle(dataID)


