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
  	print("Statement: '{0}".format(statement))
  	cursor.execute(statement)
  	print("x")
  	for row in cursor.fetchall():
  		print("x2")
  		print("Row: ", row)
  		return(row)
  except (db.Error, IOError) as e:
  	print(e)
