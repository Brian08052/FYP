from cgitb import enable 
from code import *
from clean import *
from searchCode import *
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


"""

Jobs:

Move the code from the search funciton somewhere where it can be used in the prediction stuff in code

Do a generic function for the page

Fix the search predict function


"""
xB = 11112

def removeFirstN(arrayString, n):
  print("Removing for" , arrayString, n)
  index = -1
  for i in range(n):
      index = arrayString.find(",")
      if index >= 0:
        arrayString = arrayString[index+1:]
  print(arrayString)
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

def averageLoss(array, length):
  #handle bad length, bad arrays

  predictedArray = []

  if(len(array)) < 2:
    predictedArray = array[0]
    for i in range(1, length):
      predictedArray[i] = predictedArray[i-1]/2


  else:
    percentLosses = []
    
    predictedArray += [array[0], array[1]]

    for i in range(2, len(array)):
      if(array[i] == 0):
        predictedArray += [0]

      else:
        loss = array[i-2] - array[i-1]
        if array[i-2] == 0:
          percentLosses += [0]
        else:
          percentLosses += [loss/array[i-2]]

        averageLoss = sum(percentLosses)/len(percentLosses)
        predictedArray += [array[i-1]*averageLoss]

  return predictedArray

def searchSimilar(array, length, dataID = 'CancerMolar'):
  print('Here lad')

  predictedArray = [array[0]]
  dic = getCleanDic(dataID)
  for i in range(1, len(array)):
    num = array[i]
    x = search(strToArray(str(num)), dic)
    print(x)
    predictedArray += [x[3]]

  return predictedArray

def generatePrediction(method, array, length):
  print("Here2", method)
  predictedArray = []

  if method == 'averageLoss':
    predictedArray = averageLoss(array, length)

  if method == 'similarMatch':
    print("SS")
    predictedArray = searchSimilar(array, length)
    #pass

  if method == 'machineL1':
    predictedArray = averageLoss(array, length)

  #for i in range(len(length)):
    #generate the next number


  return predictedArray

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

def createGraph(imageName, yAxes):
  longestArray, biggestValue = getGraphLimits(yAxes)
  
  xAx = []

  print('Length of longest Array: ', max(yAxes,key=len))

  for i in range(len(max(yAxes,key=len))):
    xAx += [i]
  
  for yAx in yAxes:
    print(len(yAx))
    if len(yAx) < len(max(yAxes,key=len)):
      for i in range(len(max(yAxes,key=len)) - len(yAx)):
        yAx.append(0)
    plt.scatter(xAx, yAx, 25, 'blue')
    #plt.plot(xAx, yAx, linewidth=2.0)
  #plt.plot(xAx2, yAx2, linewidth=2.0)

  plt.xlim(0, longestArray + 1)
  plt.ylim(0, biggestValue * 1.1)
  plt.draw()
  plt.savefig('image')

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


# def createGraph( arrayString, imageName, predictionName = 'averageLoss'):#, methodType, lossFunction = 'x'):
#   #createGraph()



#   #Accepts clean array
#   arrayString = arrayString[1:len(arrayString)-1] #For some reason there were quotation marks at the start and end breaking it.
#   #print('\n\n Array String:', arrayString, '\n\n',)
#   array1 = arrayString
#   array2 = []
#   xAx = []
#   yAx = []

#   #if methodType == x:
#   s2 = arrayString.split(',')
#   #print('\ns2: ', s2)
#   xAx = []
#   yAx = []
#   i = 0

#   for n in s2:
#     if n != '':
#         xAx += [i]
#         yAx += [int(n)]
#     i += 1

#   yAx2 = generatePrediction(predictionName, yAx, len(yAx))#what is this?

#   print(xAx, yAx, yAx2)
#   #return xAx, yAx
#   plt.plot(xAx, yAx, linewidth=2.0)
#   plt.plot(xAx, yAx2, linewidth=2.0)
#   #plt.plot(xAx2, yAx2, linewidth=2.0)

#   plt.draw()
#   plt.savefig('image')

#   losses = []

#   for i in range(2, len(xAx)):
#     losses += [(yAx[i]-yAx2[i])**2]


#   if len(losses) == 0:
#     return 0 

#   else:
#     return (sum(losses)/len(losses))


#*********************************** All should be deleted/imported***************************************************************


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
  pages = [("home.py", "Home"), ("upload.py", "Upload"), ("search.py", "Search")]

  string = """
  <div class="w3-top">
      <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
        <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()"><i class="fa fa-bars"></i></a>"""
  for i in range(len(pages)):
    if i == avtivePage:
      string += """<a href="%s" class="w3-bar-item w3-button w3-hide-small w3-hover-white" >%s</a>"""%(pages[i][0], pages[i][1])

    else:
      string += """<a href="%s" class="w3-bar-item w3-button w3-theme-l1">%s</a>"""%(pages[i][0], pages[i][1])

  if additional != None:
    string += """<a href="#" class="w3-bar-item w3-button w3-theme-l1">%s</a>"""%(additional)


  string += """</div></div>"""

  return string

def generateHTMLbody(activePage, title, body, additionNav = None):
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
          <h1 class="w3-text-teal">Search</h1>
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
    </script>


    </body>
    </html>""" %(title, genHeadDiv(activePage, additionalNav), body))
