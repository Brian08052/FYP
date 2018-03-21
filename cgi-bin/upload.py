#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db
from os import environ
from sense import *
from code import generateHTMLbody
#c = getCursor()

#needs to check if info is already in before inserting 



print('Content-Type: text/html')
print()

url = ""
body = ""



def getUploadForm():
  select = """<select name="dbID">"""
  lst = []
  try:
    connection = db.connect('cs1.ucc.ie', 'bgl1', SQLP, '2018_bgl1')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""select distinct dataID from fypDB""")
  except (db.Error, IOError) as e:
      print(e)
      #result = """<p>Sorry, we are experiencing database problems! People get on to Brian 0</p>"""
      
  if cursor.rowcount == 0:
      dbresult = '<p>You have no data</p>'

  else:
      for row in cursor.fetchall():
          lst+=[row['dataID']]
          select +="""<option value="%s">%s</option>"""%(row['dataID'],row['dataID'])
  select += "</select>"


  form = ("""<form action = "sample2.py" method = "post" target = "_blank">%s
    <textarea name = "text" cols = "40" rows = "2"> "1000, 900..."
    </textarea>
    <input type = "submit" value = "Submit" />
    </form>"""%(select))
  return form



form = getUploadForm()
body = generateHTMLbody(1, "Upload", form);


print(body)
