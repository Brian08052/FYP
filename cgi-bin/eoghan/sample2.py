#!/usr/local/bin/python3
from cgitb import enable 
from code import *
from sampleObject import *
enable()
import cgitb
import cgi
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
import pymysql as db
from os import environ
import re

cgitb.enable()
form = cgi.FieldStorage()
cursor = getCursor()

print("Content-Type: text/html")
print()

print('x')

if form.getvalue('textcontent'):
  so = sampleObject('x', 1, form.getvalue('textcontent'))
  print('<br>')
  if not so.dataOk:
  	print('Data Incomplete. Please ensure data is in the correct format?')
  	data = "Data contains too many blank values. Please try again. <br> Data : %s"%(form.getvalue('textcontent'))
  else:
  	print('Data Ok!')
  	print(form.getvalue('textcontent'))
  	print('<br>')
  	print(so.getCleanArray(True))
  	print(so.data, so.cleanArray)
  	if form.getvalue('dbID'):
  		dataID = form.getvalue('dbID')

  	else:
  		dataID = "Not entered"

  	print(dataID)
  	print("Entered: ",  form.getvalue('textcontent'), '<br>', 'Modified to: ', so.data)
  	
  	sampleID = getNextSampleID(form.getvalue('dbID'))
  	data = ("Data to be uploaded: %s" %(so.data))
  	data += ("<br>Button saying upload. Sends to sample dataID, sampleID, data, upload")
  	data += ("<br>Data is then uploaded, and then the sample page is loaded.")

  	formCode = ""
  	formCode = """<form action="sample.py" method="post" target="_self">"""
  	formCode += ("""<input type="hidden" name="upload" value="True" />""")
  	formCode += ("""<input type="hidden" name="data" value="%s" />"""%(so.dataString))
  	formCode += ("""<input type="hidden" name="dataID" value="%s" />"""%(form.getvalue('dbID')))
  	formCode += ("""<input type="hidden" name="sampleID" value="%s" />"""%(sampleID))
  	formCode += ("""<input type = "submit" value = "Upload" /></form>""")
  	data += ('<br>' + formCode)




html = generateHTMLbody(None, 'Upload Sample', data, additionalNav = 'Upload Sample')
print(html)

