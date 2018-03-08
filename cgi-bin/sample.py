#!/usr/local/bin/python3
from cgitb import enable 
from code import *
from createDict import *
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
import re

cgitb.enable()
form = cgi.FieldStorage()
cursor = getCursor()

non_decimal = re.compile(r'[^\d.,]+')
sampleData = "No data"

print("Content-Type: text/html")
print()
#print(idCode(4))
#print(form.getvalue('search'), form.getvalue('dbID'),form.getvalue('sampleID'))

sampleObjectName = ""
sampleObjectData = ""

functions = [('Average Loss', 'averageLoss'), ('Similar Match', 'similarMatch'), ('Machine Learning 1', 'machineL1')]
yAxes = []
images = []
formCode = 'No data to predict.'

imageCode = ''
completed = False

dataID = form.getvalue('dbID')
sampleID = form.getvalue('sampleID')

print(dataID, sampleID)

if (dataID != None and sampleID != None):
#if form.getvalue('search'):
  #print("Hello Worlds, you are so many, each so beautiful and each with tradgey ")
  #cleanDic = getClea
  cleanDic = getCleanDictionary(dataID)
  rawDic = getRawDictionary(dataID)
  if int(sampleID) in rawDic.keys():
    sample = cleanSample(strToArray(rawDic[int(sampleID)]))

    sampleObject = sampleObject(dataID, sampleID, sample[0], sample[1])
    imageName = createGraph(sampleObject.getAlteredAxes(), sampleObject.getName())
    
    imageCode = genImageHTML(imageName)
    sampleObjectData = sampleObject.getTableHTML()
    sampleObjectName = sampleObject.getName()
    completed = sampleObject.isComplete()


  else:
    sampleData = "Error"

else:
  print(sampleID, dataID)



def getFuntionsIndex(name):
  #index =0
  for i in range(len(functions)):
    if functions[i][1] == name:
      return i
  return 0


def databaseForm(selectedVal = 'None'):
  
  selected = str(selectedVal)
  formCode = ""

  formCode = """<h1>Select Prediction Method: </h1><form action="sample.py" method="post" target="_self"> <select name="predictMethod">"""

  if selected != 'None':
    formCode += """<option selected="selected" value="%s">%s</option>""" % (selected, selected)
    for function in functions:
      if function[1] != selected:
        formCode += """<option selected="selected" value="%s">%s</option>""" % (function[1], function[0])

  else:
    for function in functions:
      formCode += """<option selected="selected" value="%s">%s</option>""" % (function[1], function[0])


  formCode += "</select>"
  formCode += ("""<input type="hidden" name="search" value="%s" />"""%(form.getvalue('search')))
  formCode += ("""<input type="hidden" name="dbID" value="%s" />"""%(form.getvalue('dbID')))
  formCode += ("""<input type="hidden" name="sampleID" value="%s" />"""%(form.getvalue('sampleID')))
  formCode += ("""<input type = "submit" value = "Go" /></form>""")

  return formCode




###********************* Ignore *************************
    
  # else:
  #   #This whole else statement is the uploading code.
  #   #Ignore this for now, move to a different page later?

  #   #if all data is available:
  #   # check data
  #   #   upload data
  #   # data not proper
  #   #data not available
  #   if form.getvalue('textcontent') and form.getvalue('dbID'):
  #     #check data
  #     text_content = non_decimal.sub('', form.getvalue('textcontent'))
  #      #It goes in as a string like 1,2,3,,4,,,5 -this has to be really strict, so probably read from a CSV idk
  #      #add the text content to the database
  #      #refresh the dataframe
  #   else:
  #      text_content = "Not entered"

  #   if form.getvalue('dbID'):
  #      dataID = form.getvalue('dbID')
  #   else:
  #      dataID = "Not entered"

  #   x2 = 'initial'
  #   try:
  #     s = ("""select max(sampleID) from fypDB where dataID = '%s'"""%dataID)
  #     print(s)
  #     cursor.execute(s)
  #     sampleID =  (cursor.fetchall()[0]['max(sampleID)']) + 1
  #     uploadData(cursor, dataID, sampleID, text_content)
  #     sampleData = str(getData(cursor, dataID, sampleID))[1:]



  #   except (db.Error, IOError) as e:
  #       print(e)
  #       #result = """<p>Sorry, we are experiencing database problems! People get on to Brian 0</p>"""

##*******************************************************




if not completed:

  if form.getvalue('predictMethod'):
    formCode = databaseForm(form.getvalue('predictMethod'))
  else:
    formCode = databaseForm()

  if form.getvalue('predictMethod'):
    yAxes += [generateYaxis(sampleData, method = form.getvalue('predictMethod'), n = -1)]
    

    #print('X1')
    #loss = createGraph(sampleData, 'image', form.getvalue('predictMethod'))
    #loss = createGraph(sampleData, 'image', form.getvalue('prediciton'))
  else:
    pass
    # yAxes += [generateYaxis(sampleData, method = 'default', n = -1)]
    # images += [createGraph('image', [yAxes[0]])]

    #print('X2')
    ##graph : 
    #loss = createGraph(sampleData, 'image')


yAxString = ''
for yAx in yAxes:
  yAxString += str(yAx)












body = ("""
<!DOCTYPE html>
<html>
<title>Sample %s</title>
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
<div class="w3-top">
  <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()"><i class="fa fa-bars"></i></a>
   <a href="home.py" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Home</a>
    <a href="upload.py" class="w3-bar-item w3-button w3-hide-small w3-hover-white">Upload</a>
    <a href="#" class="w3-bar-item w3-button w3-theme-l1" >Sample</a>

  </div>
</div>

<!-- Sidebar -->
<nav class="w3-sidebar w3-bar-block w3-collapse w3-large w3-theme-l5 w3-animate-left" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-right w3-xlarge w3-padding-large w3-hover-black w3-hide-large" title="Close Menu">
    <i class="fa fa-remove"></i>
  </a>
  <h4 class="w3-bar-item"><b>Menu</b></h4>
  <a class="w3-bar-item w3-button w3-hover-black" href="#">Update Sample</a>
</nav>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- Main content: shift it to the right by 250 pixels when the sidebar is visible -->
<div class="w3-main" style="margin-left:250px">

  <div class="w3-row w3-padding-64">
    <div class="w3-twothird w3-container">
      <h1 class="w3-text-teal">Sample: %s</h1>
        %s 
        %s
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
</html>"""%(sampleObjectName, sampleObjectName, sampleObjectData, imageCode, formCode))


print(body)
