#!/usr/local/bin/python3
from cgitb import enable 
enable()
from cgi import FieldStorage, escape
form = FieldStorage()

import pymysql as db
import re

from code import *
#from createDict import *
from sampleObject import *
# from cgi import FieldStorage, escape
# from hashlib import sha256
# from time import time
# from shelve import open
# from http.cookies import SimpleCookie
# import pymysql as db
# from os import environ
# from sense import *
#c = getCursor()

#needs to check if info is already in before inserting 


#************************ FUNCTIONS ******************************#
myForm = 'blank'
def getInput(dataID, sampleID, data):
  myForm = """<form action = "update.py" method = "post">
      <input type="hidden" value="%s" name="dataID" />
      <input type="hidden" value="%s" name="sampleID" />
      <input type="hidden" value="%s" name="originalData" />
      <input type="hidden" value="True" name="input" />
      <textarea name = "newData" cols = "40" rows = "4">%s</textarea>
      <input type = "submit" value = "Update" /></form>"""%(dataID, sampleID, data, data)

  return myForm

def inputReceived(dataID, sampleID, newData, originalData):

  so = sampleObject(dataID, sampleID, newData)

  if so.cleanDataAvailable():
    myForm = """Data Entered: %s <br>
      <form action = "sample.py" method = "post" target = "_blank">
      <input type="hidden" value="%s" name="dataID" />
      <input type="hidden" value="%s" name="sampleID" />
      <input type="hidden" value="%s" name="data" />
      <input type="hidden" value="True" name="update" />
      <input type = "submit" value = "Update" /></form>"""%(newData, dataID, sampleID, newData)


  else:
    myForm = 'Data Entered: %s <br> Too many blank values, please try again.'%(newData)

  return myForm

#*****************************************************************#

print('Content-Type: text/html')
print()

if form.getvalue("update"):

  myForm = getInput(form.getvalue("dataID"), form.getvalue("sampleID"), form.getvalue("data"))

elif form.getvalue("input"):

  myForm = inputReceived(form.getvalue("dataID"), form.getvalue("sampleID"), form.getvalue("newData"), form.getvalue("originalData"))


#print(form.getvalue("dataID"), form.getvalue("sampleID"), form.getvalue("newData"), form.getvalue("originalData"))

print(generateHTMLbody(15, 'Update', myForm, additionalNav = 'Update', additionalScript = ''))



