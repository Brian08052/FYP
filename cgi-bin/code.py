from cgitb import enable 
from code import *
from clean import *
from searchCode import *
from variables import *
from prediction import *
#from pickles import *
#from searchCode import *
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
#import pandas as pd


"""

Jobs:

Move the code from the search funciton somewhere where it can be used in the prediction stuff in code

Do a generic function for the page

Fix the search predict function


"""
xB = 11112

# class sampleObject:
#   def __init__(self, dbID, sampleID, data, alteredArray = None):
#     self.dbID = dbID
#     self.sampleID = sampleID
#     self.data = data
#     self.alteredArray = alteredArray

#   def getName(self):
#     return(str(self.dbID) + '-' + str(self.sampleID))

#   def getAlteredAxes(self):
#     if self.alteredArray == None:
#       print("Error, no altered Array")
#     xAx1 = []
#     xAx2 = []
#     yAx1 = []
#     yAx2 = []

#     for i in range(len(self.alteredArray)):
#       if self.alteredArray[i] == 0:
#         xAx1 += [self.data[i]]
#         yAx1 += [i]
#       else:
#         xAx2 += [self.data[i]]
#         yAx2 += [i]
#     return [[xAx1, yAx1], [xAx2, yAx2]]


#   def isComplete(self):
#     return self.data[len(self.data) - 1] < 4





#   def getAxes(self):
#     xAx = []
#     yAx = []
#     modifiedData = self.data[removeFirstValue(self.data):]
#     print(modifiedData)
#     for i in range(len(modifiedData)):
#       if modifiedData[i] != None:
#         xAx += [i]
#         yAx += [modifiedData[i]]
#     return [[yAx, xAx]]

#   def getOriginalAxes(self):
#     xAx = []
#     yAx = []
#     for i in range(len(self.data)):
#       if self.data[i] != None:
#         xAx += [i]
#         yAx += [self.data[i]]
#     return [[yAx, xAx]]


#   def getTableHTML(self):
#     arrayEnd = None
#     table = """<table style = "border: 1px solid black;"><tr>"""
#     for i in range(len(self.data)):
#       if self.alteredArray[i] == 0:
#         table += """<td style = "border: 1px solid black;" >%s</td>"""%(int(self.data[i]))
#       else:
#         table += """"<td style="color:red; border: 1px solid black;">%s</td>"""%(int(self.data[i]))

#     table += "</tr></table>"

#     return table 


def genImageHTML(imageName):
  return """<img src="%s" alt="%s">"""%(imageName, imageName)


def getNextSampleID(dataID):
  cursor = getCursor()
  #s = ("""select max(sampleID) from fypDB where dataID = '%s'"""%dataID)
  #getCursor().execute(s)
  cursor.execute(("""select max(sampleID) from fypDB where dataID = '%s'"""%dataID))
  return (cursor.fetchall()[0]['max(sampleID)']) + 1


def removeFirstValue(array, multiple = 20):
  #ok this should return n
  while array[0] == None:
    array = array[1:]
  value1 = array[0]
  if array[1] == None:
    return 0

  i1 = 1
  while array[i1] == None:
    i1+=1
  
  i2 = i1+1
  while array[i2] == None:
    i2 += 1



  if len(array)>2:
    if array[0] > array[i1]*multiple:
      return i1
    elif array[i1] > array[i2]*multiple:
      return i2
  return 0


def removeFirstN(arrayString, n):
  index = -1
  for i in range(n):
      index = arrayString.find(",")
      if index >= 0:
        arrayString = arrayString[index+1:]
  return arrayString

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

def updateData(cursor, dataID, sampleID, text_content):
  update = """UPDATE fypDB SET sampleData = '%s' WHERE dataID = '%s' AND sampleID = %s;"""%(text_content, dataID, sampleID)
  cursor.execute(update)
  cursor.execute('COMMIT')




#******************************* Graphing *********************************************************8
def getGraphLimits(yAxes):
  longestArray = 0
  biggestValue = 0
  for y in yAxes:
    print("Y: ", y)
    if len(y) > longestArray:
      longestArray = len(y)
    y2 = [x for x in y if x != None]
    if max(y2) > biggestValue:
      biggestValue = max(y2)

  return(longestArray, biggestValue)

def createGraph2(axes, imageName):
  

  xLimit = 0
  yLimit = 0
  xAxes = []
  yAxes = []
  for ax in axes:
    

    values = ax[0]
    index = ax[1]

    if len(ax[1]) > xLimit:
      xLimit = len(ax[1])
    if max(ax[0]) > yLimit:
      yLimit = max(ax[0])
    plt.scatter(ax[0], ax[1], 25)
    yAxes += [ax[1]]
  limits = getGraphLimits(yAxes)
  plt.xlim(0, xLimit + 1)
  plt.ylim(0, yLimit * 1.1)
  plt.draw()
  plt.savefig(imageName)

  return(imageName)#, loss?)

def createGraph(axes, imageName):
  colours = ['green', 'blue' , 'red']
  counter = 0
  #takes in all that you want on the one graph, in teh format
  #[ [values] , [offset], [values], [offset] the value
  xLimit = 0
  yLimit = 0
  xAxes = []
  yAxes = []
  for ax in axes:
    counter += 1
    if counter == len(colours):
      counter = 0
    if len(ax[1]) > xLimit:
      xLimit = len(ax[1])
    if max(ax[0]) > yLimit:
      yLimit = max(ax[0])
    plt.scatter(ax[1], ax[0], 25, colours[counter])
    yAxes += [ax[1]]
  #limits = getGraphLimits(yAxes)
  #plt.xlim(0, xLimit + 1)
  #plt.ylim(0, yLimit * 1.1)
  plt.draw()
  plt.show()
  plt.savefig(imageName)
  plt.close()

  return(imageName)#, loss?)
  return(imageName)#, loss?)


  #for yAx in yAxes:
    #scatter itl

def generateYaxis(array, method = 'default', n = -1):
  if method == 'default':
    return array
  elif method == 'averageLoss':
    pass
  return
    #return averageLoss(array, n)



#*********************************** All should be deleted/imported***************************************************************










#**********************************************************************************************************************************************************

    
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

def genHeadDiv(activePage, additional = None):
  navPages = [("home.py", "Home"), ("upload.py", "Upload"), ("search.py", "Search")]
  pages = navPages

  string = """
  <div class="w3-top">
      <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
        <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()"><i class="fa fa-bars"></i></a>"""
  for i in range(len(pages)):
    if activePage != None and i == activePage:
      string += """<a href="%s" class="w3-bar-item w3-button w3-theme-l1">%s</a>"""%(pages[i][0], pages[i][1])
      

    else:
      string += """<a href="%s" class="w3-bar-item w3-button w3-hide-small w3-hover-white" >%s</a>"""%(pages[i][0], pages[i][1])
      

  if additional != None:
    string += """<a href="#" class="w3-bar-item w3-button w3-theme-l1">%s</a>"""%(additional)


  string += """</div></div>"""

  return string

def generateHTMLbody(activePage, title, body, additionalNav = None, additionalScript = ''):
  string = body = ("""
    <!DOCTYPE html>
    <html>
    <title>%s</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
    .w3-sidebar {
      z-index: 3;
      width: 250px;
      top: 43px;
      bottom: 0;
      height: inherit;
    }
    </style>
    <body>

    <!-- Navbar -->
    %s
    <!-- Sidebar -->
    <nav class="w3-sidebar w3-bar-block w3-collapse w3-large w3-theme-l5 w3-animate-left" id="mySidebar">
      <a href="javascript:void(0)" onclick="w3_close()" class="w3-right w3-xlarge w3-padding-large w3-hover-black w3-hide-large" title="Close Menu">
        <i class="fa fa-remove"></i>
      </a>
      <h4 class="w3-bar-item"><b>Menu</b></h4>
      <a class="w3-bar-item w3-button w3-hover-black" href="#">Info</a>
    </nav>

    <!-- Overlay effect when opening sidebar on small screens -->
    <div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

    <!-- Main content: shift it to the right by 250 pixels when the sidebar is visible -->
    <div class="w3-main" style="margin-left:250px">

      <div class="w3-row w3-padding-64">
        <div class="w3-twothird w3-container">
          
           %s 
        </div>

      </div>





      <!-- Pagination -->




    <!-- END MAIN -->
    </div>

    <script>
    // Get the Sidebar
    var mySidebar = document.getElementById("mySidebar");

    // Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");

    // Toggle between showing and hiding the sidebar, and add overlay effect
    function w3_open() {
        if (mySidebar.style.display === 'block') {
            mySidebar.style.display = 'none';
            overlayBg.style.display = "none";
        } else {
            mySidebar.style.display = 'block';
            overlayBg.style.display = "block";
        }
    }

    // Close the sidebar with the close button
    function w3_close() {
        mySidebar.style.display = "none";
        overlayBg.style.display = "none";
    }
    
      %s
    </script>


    </body>

    </html>""" %(title, genHeadDiv(activePage, additionalNav), body, additionalScript))

  return string

#############****************Prediction.py********************





# def searchSimilar(array, length, dataID = 'CancerMolar'):
#   #maybe make a dictionary of the three results and then search them each time to - NO this makes no sense, you already have all the data dummy
#   #WAIT actually no, you could find the closes 2? and then the next one?
#   #aren't we using the result object for this or something
#   #result object has a predict method
#   #it takes in a number, outputs the loss to the closest match, and the next the number-- take a weighted estimation ?

#   predictedArray = [array[0]]
#   dic = getCleanDic(dataID)
#   for i in range(1, len(array)):
#     num = array[i]
#     x = search(strToArray(str(num)), dic)
#     predictedArray += [x[3]]

#   return predictedArray



