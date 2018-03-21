#!/usr/local/bin/python3
from code import *
from cgitb import enable 
enable()
import math
import numpy
import random

print('Content-Type: text/html')
print()

url = ""
body = ""
cursor = getCursor()
form = FieldStorage()

def code(dbID, dataID):
  r = random.randint(11,99)

  return(str(dbID) + '-001-' + str(r) + str(dataID))



def databaseForm(cursor):

  selectDB = """<h1>Select Database: </h1> <select name="dbID">"""
  try:
    cursor.execute("""select distinct dataID from fypDB""")
    # lst = []
    if form.getvalue('dbID'):
      for row in cursor.fetchall():
        if row['dataID'] == form.getvalue('dbID'):
          selectDB += """<option selected="selected" value="%s">%s</option>""" % (row['dataID'], row['dataID']) #code(form.getvalue('dbID'),row['dataID'])
        else:
          selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])
    else:
      for row in cursor.fetchall():
        selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])
    
	
	
	
    

    selectDB +=  """<input type="text" name="searchString" value="100,10,1">"""
    selectDB += "</select>"
    formCode = ("""<form action = "searchResult.py" method = "post" target = "_self">%s
      <input type = "submit" value = "Go" /></form>""" % (selectDB))
    return formCode
  except (db.Error, IOError) as e:
    print(e)
    return('databaseForm Error')

formCode = databaseForm(cursor)

# if form.getvalue('dbID'):
#   try:
#     databaseID = form.getvalue('dbID')
#     selectSample = "<select name='sampleID'>"
#     cursor.execute("""select distinct sampleID, dataID, sourceID from fypDB where dataID = '%s'""" % (databaseID))
#     # lst = []
#     for row in cursor.fetchall():
#           # lst+=[row['dataID']]
#       string = row['dataID'] + '-' + fill0s(row['sourceID'], 3) + '-' + fill0s(row['sampleID'],4)
#       selectSample += """<option value="%s">%s</option>""" % (row['sampleID'], code(databaseID, row['sampleID']))

#     selectSample += "</select>"
#     formCode += ("""<h1?Database: %s Select Sample</h1><form action = "sample.py" method = "post" target = "_self">%s
#         <input type="hidden" value="true" name="search" />
#         <input type="hidden" value="%s" name="dbID" /><input type = "submit" value = "Go" /></form>""" % (databaseID, selectSample,databaseID))
#   except (db.Error, IOError) as e:
#     print(e)

  

body2 = generateHTMLbody(2, "Search", formCode);

print(body2)
