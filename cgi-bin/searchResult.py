#!/usr/local/bin/python3
from code import *
from resultObject import *
from searchCode import *
from mlTest import *
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
functions = [('Average Loss', 'averageLoss'), ('Predict from Similar Samples', 'searchSimilar'), 
('Predicted from Similar Losses', 'searchSimilarLosses'), ('Predict From Machine Learning Losses', 'ml1'),
('Predict from log Linear', 'ml2')]
PREDICTION_ARRAY_LEN = 35
resultObjects = []
dic = None
predictGraphHTML = ""
searchLength = 0



print(form.getvalue('search'), form.getvalue('dbID'),form.getvalue('searchString'),form.getvalue('predictMethod'))
data = "hi"
prediction = ''

imageData = 'No Image'


def getSearchResultArrays(dbID, searchArray):
  #dic should just be given in
  dic2 = {}
  dic = getCleanDic(dbID)


  for k in dic:
    dic2[k] = dic[k][0]

  dic = dic2
  results = searchN(searchArray, dic, 3)

  print('<br>Results: ', results)

  #results += searchN(searchArray, dic, 3, 1)
  resultObjects = []

  for result in results:
    ro = resultObject(dbID, result[0], result[2], result[3], searchArray)
    resultObjects += [ro]

  usefulInformation = []
  for ro in resultObjects:
    info = []
    info += [ro.getName()]
    info += [ro.getMatchingAxes()]
    #info += [ro.getLoss()] 
    usefulInformation += [info, '<br>']

  return resultObjects

def createBody(resultArrays):
  string = ""
  for ro in resultArrays:
    string += createDiv(ro)

  return string

def createDiv(resultObject):
  imageName = createGraph(resultObject.getFullAxes(), resultObject.getName() )
  imageName2 = createGraph(resultObject.getMatchingAxes(), resultObject.getName() + '2')
  
  imageCode, imageCode2 = genImageHTML(imageName), genImageHTML(imageName2)
  divName = resultObject.getName()

  string = """<button onclick="myFunction('%s')">%s</button>
  Total Absolute Loss: %s

  <div id="%s" style="display:none"> %s <br><br>
  %s <br> %s <br>
  </div><br><br><br>"""%(divName,divName, resultObject.getTotalLoss(), divName, resultObject.getTableHTML(), imageCode, imageCode2)

  return string

def databaseForm(selectedVal = 'None'):
  print('SV: ', selectedVal)
  #This needs to be fixed 
  
  selected = str(selectedVal)
  formCode = ""

  formCode = """<h1>Select Prediction Method: </h1><form action="searchResult.py" method="post" target="_self"> <select name="predictMethod">"""

  if selected != 'None':
    #formCode += """<option selected="selected" value="%s">%s</option>""" % (selected, selected)
    for function in functions:
      if function[1] == selected:
        formCode += """<option selected="selected" value="%s">%s</option>""" % (function[1], function[0])
      else:
        formCode += """<option value="%s">%s</option>""" % (function[1], function[0])

  else:
    for function in functions:
      formCode += """<option value="%s">%s</option>""" % (function[1], function[0])


  formCode += "</select>"
  formCode += ("""<input type="hidden" name="search" value="%s" />"""%(form.getvalue('search')))
  formCode += ("""<input type="hidden" name="dbID" value="%s" />"""%(form.getvalue('dbID')))
  formCode += ("""<input type="hidden" name="searchString" value="%s" />"""%(form.getvalue('searchString')))
  formCode += ("""<input type = "submit" value = "Go" /></form>""")

  return formCode

def getGraph(resultArray, searchLength):
  yVals = resultArray
  xVals = [i for i in range(len(yVals))]
  yVals1 = yVals[:searchLength] 
  yVals2 = yVals[searchLength:]
  xVals1 = xVals[:searchLength]
  xVals2 = xVals[searchLength:]
  iName = createGraph([[yVals1, xVals1], [yVals2, xVals2]],'predictedGraph')
  iCode = genImageHTML(iName)
  return iCode


if form.getvalue('dbID'):
  imageData = ''
  dataID = form.getvalue('dbID')
  searchString = form.getvalue('searchString')

  data = ("Database: " + dataID + ", input:" + searchString + "<br>")
  
  searchArray = strToArray(searchString)
  searchLength = len(searchArray)
  resultObjects = getSearchResultArrays(dataID, searchArray)
  bodyHTML = createBody(resultObjects)


else:
  data = "no data"
  
print('PM: ', form.getvalue('predictMethod'))
if form.getvalue('predictMethod'):#and if searchArray has been made!]
  print(form.getvalue('predictMethod'))
  dic = getCleanDic(form.getvalue('dbID'))
  if form.getvalue('predictMethod') == 'searchSimilar':
    print('Here....')
    prediction = searchSimilar(searchArray, PREDICTION_ARRAY_LEN, resultObjects)
  elif form.getvalue('predictMethod') == 'searchSimilarLosses':
    print('Here....')
    prediction = searchSimilarLosses(searchArray, PREDICTION_ARRAY_LEN, resultObjects)

  elif form.getvalue('predictMethod') == 'ml1':
    prediction = predictML(dic, searchArray, PREDICTION_ARRAY_LEN)

  elif form.getvalue('predictMethod') == 'ml2':
    prediction = predicMLlogLoss(dic, searchArray, PREDICTION_ARRAY_LEN)
  elif form.getvalue('predictMethod') == 'averageLoss':
    print('here?')
    prediction = form.getvalue('predictMethod')
    prediction = averageLoss(searchArray, 35)

  predictGraphHTML = getGraph(prediction, searchLength)
else:
  prediction = 'no prediction method selected'




body = ("""

  <!DOCTYPE html>
  <html>
  <title>Search Result</title>
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
  table {
    border-collapse: collapse;
  }

  table, td, th {
      border: 1px solid black;
  }
  </style>
  <body>

  <!-- Navbar -->
  <div class="w3-top">
    <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
      <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()"><i class="fa fa-bars"></i></a>
      <a href="home.py" class="w3-bar-item w3-button w3-hide-small w3-hover-white" >Home</a>
      <a href="upload.py" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Upload</a>
      <a href="search.py" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Search</a>
      <a href="#" class="w3-bar-item w3-button w3-theme-l1">Search Result</a>

    </div>
  </div>

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
        <h1 class="w3-text-teal">Search Results</h1>
         %s <br><br> %s <br><br> %s <br><br> %s <br> %s
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

  function myFunction(id) {
          var x = document.getElementById(id);
          if (x.style.display == "none") {
              x.style.display = "block";
          } else {
              x.style.display = "none";
          }
          //document.write(id);
      }
  </script>


  </body>
  </html>""" % ( imageData, bodyHTML, databaseForm(form.getvalue('predictMethod')), prediction, predictGraphHTML))

print(body)
