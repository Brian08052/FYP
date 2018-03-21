#!/usr/local/bin/python3
from code import *
from cgitb import enable 
enable()
import math
import numpy
import random
import scipy
import sklearn
import pandas
from sklearn.linear_model import LinearRegression


print('Content-Type: text/html')
print()

print(xB)

url = ""
body = ""
cursor = getCursor()
form = FieldStorage()

def code(dataID, sampleID):
  r = random.randint(11,99)

  return(str(dataID) + '-001-' + str(r) + str(sampleID))



def databaseForm(cursor):

  selectDB = """<h1>Select Database: </h1> <select name="dataID">"""
  try:
    cursor.execute("""select distinct dataID from fypDB""")
    # lst = []
    if form.getvalue('dataID'):
      for row in cursor.fetchall():
        if row['dataID'] == form.getvalue('dataID'):
          selectDB += """<option selected="selected" value="%s">%s</option>""" % (row['dataID'], row['dataID']) #code(form.getvalue('dataID'),row['dataID'])



        else:
          selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])
    else:
      for row in cursor.fetchall():
        print(row['dataID'])
        if row['dataID'] == 'CancerMolar':
          selectDB += """<option selected value="%s">%s</option>""" % (row['dataID'], row['dataID']) #code(form.getvalue('dataID'),row['dataID'])
        else:
          selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])
    
	
	
	
    

    selectDB += "</select>"
    formCode = ("""<form action = "home.py" method = "post" target = "_self">%s
      <input type = "submit" value = "Go" /></form>""" % (selectDB))
    return formCode
  except (db.Error, IOError) as e:
    print(e)
    return('databaseForm Error')

formCode = databaseForm(cursor)

if form.getvalue('dataID'):
  try:
    databaseID = form.getvalue('dataID')
    selectSample = "<select name='sampleID'>"
    cursor.execute("""select distinct sampleID, dataID, sourceID from fypDB where dataID = '%s'""" % (databaseID))
    # lst = []
    for row in cursor.fetchall():
          # lst+=[row['dataID']]
      string = row['dataID'] + '-' + fill0s(row['sourceID'], 3) + '-' + fill0s(row['sampleID'],4)
      selectSample += """<option value="%s">%s</option>""" % (row['sampleID'], code(databaseID, row['sampleID']))

    selectSample += "</select>"
    formCode += ("""<h1?Database: %s Select Sample</h1><form action = "sample.py" method = "post" target = "_self">%s
        <input type="hidden" value="true" name="search" />
        <input type="hidden" value="%s" name="dataID" /><input type = "submit" value = "Go" /></form>""" % (databaseID, selectSample,databaseID))
  except (db.Error, IOError) as e:
    print(e)


body = """<h1 class="w3-text-teal">Select Sample</h1>%s"""%(formCode)


body2 = generateHTMLbody(0, "Home", body);#activePage, title, body, additionNav = None)

print(body2)
