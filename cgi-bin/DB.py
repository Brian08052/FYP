#!/usr/local/bin/python3
from code import *
from cgitb import enable 
enable()
import math
import numpy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
from pylab import *
#from sklearn.pipeline import Pipeline
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.model_selection import validation_curve
# from sklearn.model_selection import learning_curve
# from sklearn.model_selection import cross_validate


print('Content-Type: text/html')
print()

tempData = "[['452119,4657,822,,,,15,,,,,1,,,,1,1,1,1,1,,,,,,,,,,,232,1644,8537,,,'], ['171471,,3029,,3617,5654,5090,4369,2679,885,249,30,3,0,0,0,0,0,0,0,0,0,6294,,,,,,,,,0,,,,'], ['257926,,2734,862,426,264,146,70,63,62,,29,,,,18,3,4,3,3,1,1,,,,,,,,,,,,,,'], ['439986,11597,3664,1250,357,154,72,26,13,7,4,3,,,,2,1,1,1,1,1,,,,,,,,,,,,,,,'], ['111581,2400,469,236,290,88,34,11,5,3,2,,,,,0,0,0,0,,,,,,,,,,,,,,,,,'], ['178594,1783,248,56,17,8,4,2,0,,,,,,,0,0,0,,,,,,,,,,,,,,,,,,'], ['488811,11959,1525,713,424,499,728,,81,88,25,5,2,,,,0,0,0,0,0,0,0,,,,,,,,,,,,,'], ['69,24,8,4,0,0,0,0,0,,0,,,,,0,0,0,,,,,,,,,,,,,,,,,,'], ['19,12,7,5,3,2,2,0,,,,0,,,,0,0,0,0,0,,,,,,,,,,,,,,,,'], ['5407,,52,12,4,3,2,0,,,,0,,0,0,,,,,,,,,,,0,,,,,,,,,,'], ['274392,3010,579,163,63,33,17,11,6,4,3,,,,0,,0,0,0,0,0,0,,,,,,,,,,,,,,'], ['242245,3414,614,295,213,,107,75,63,31,17,14,8,4,5,2,0,0,0,15,0,0,0,,,,,,,,,,,,,'], ['565701,342265,16360,1979,504,182,82,,,12,8,5,,3,,,2,2,0,0,0,0,0,0,0,0,0,0,,,,,,,,'], ['36450,,79997,20798,1943,252,58,19,8,5,3,2,0,0,0,0,0,0,0,0,,,,,,,,,,,,,,,,'], ['1669,1914,4434,5839,,,,32,8,,2,0,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,,'], ['151911,48969,16261,,388,113,38,,22,,29,33,45,,13,5,2,0,0,0,0,0,0,0,,,,,,,,,,,,'], ['19991,5551,3709,3568,722,110,48,,24,18,15,8,5,,5,,0,0,0,0,0,0,0,0,,,,,,,,,,,,'], ['20727,19468,,15922,676,145,39,18,8,5,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,782,6,0,0,,,,,'], ['121768,218972,8754,3980,3327,1729,1159,612,366,197,7,0,0,0,0,0,0,0,0,35,,,,,,,383,829,,,,,,,,'], ['108018,6104,2792,394,30,12,5,2,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,,,,,,'], ['40428,32460,4612,2106,821,652,507,436,473,408,227,201,184,196,,23,4,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,'], ['96884,4041,1644,620,6,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,'], ['29455,2376,112,34,26,11,9,5,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,'], ['7189,15822,,20778,9412,969,62,,3,0,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,,,,'], ['14365,,251,,53,,2,,0,,,,,0,,,,,,,,,,,,,,,,,,,,,,'], ['73320,1336,145,43,18,6,3,0,0,0,,,,0,,,0,0,0,0,,,,,,,,,,,,,,,,'], ['166859,176230,37749,1425,223,65,28,11,6,3,0,,,,,0,0,,,,,,,,,,,,,,,,,,,'], ['17876,,74,,14,4,,,,0,,,,0,,,0,0,,,,,,,,,,,,,,,,,,'], ['631112,18516,4243,1026,313,199,204,209,153,38,,2,,,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,,'], ['11964,450,49,10,0,,,0,,,,0,,,,0,0,,,,,,,,,,,,,,,,,,,'], ['773545,6607,1104,264,99,55,,,41,8,,,,,0,,0,,,0,,,,,,,,,,,,,,,,'], ['3438,,,790,,325,,8,0,0,,,0,,,,0,0,,,,,,,,,,,,,,,,,,'], ['358977,407433,76489,2796,644,192,87,49,27,16,9,6,3,2,0,0,0,0,0,160,3,0,0,0,,,,,,,,,,,,']]"

url = ""
body = ""
cursor = getCursor()
form = FieldStorage()

dbHTML = "Hello World"

def strToArray(s):
  s = s[1:len(s)-1]
  arrays = s.split(',')

  s2 = [line.split() for line in f.readlines()]
  #turns a string line into an array
  arr = s.split(',')
  arr2 = []
  for s in arr:
      if s == '':
          arr2 += [None]
      else:
          #error checking
          arr2 += [int(s)]
  return arr2

def stringToArr(fullSet):
    #Converts a text file into a an array of arrays
    #gets rid of the bit of string at the top of the txt file
    fullSet[0][0] = fullSet[0][0]#[3:]
    
    #make a new arr that will hold all our new arrays
    out = []
    for l in fullSet:
        #makes an array out of each string
        arr = strToArray(l[0])
        out += [arr]
    return out

###################################################################################################

def cleanSet(fullArray):
    cleanArray = []
    for sample in fullArray:
        fillZeroForNone(sample)
        clearRecurrence(sample)
        if not tooManyBlanks(sample):
            cleanArray += [replaceNones(sample)]
    
    return cleanArray


def cleanDict(d):
    cleanD = {}
    for key in d:
        sample = d[key].copy()
        fillZeroForNone(sample)
        clearRecurrence(sample)
        if not tooManyBlanks(sample):
            cleanD[key] = replaceNones(sample)
            #cleanD[key] = sample
    
    return cleanD
            


    
#************************************* Helper Functions *********************************
        
        
def fillZeroForNone(sample):
    #recursive function that replaces Nones with 0 if the next value in the array is 0.
    #clear recurrence handles nones that come after
    for i in range(len(sample)):
        if sample[i] == 0:
            if sample[i-1] == None:
                sample[i-1] = 0
                sample = fillZeroForNone(sample)
    return sample

def clearRecurrence(sample):
    #We're not interested in the cases where the cancer comes back.
    #If the number gets low enoguh, everything that comes after is set to zero.
    
    #if the sample gets low enough, everything after is set to zero.
    #this is to learn the general sequence of decay without reoccurance 
    flag = False
    for i in range(len(sample)):
        if flag == True:
            sample[i] = 0
        if sample[i] != None and sample[i] <= 3:
            flag = True

    return sample

def tooManyBlanks(sample):###
    #Checks if the sample has 3 Nones in a row.
    
    #Must be clearRecurrence() sample first!
    i = 0
    counter = 0
    while i < len(sample):
        if sample[i] == None:
            counter+=1
        else:
            counter = 0
        if counter == 3:
            return True
        i+= 1
    return False

def replaceNones(sample):
    #Data needs to be checked first that first element isnt none
    #if sample[0] is None: return None
    #if there's 3 Nones, toss it I'd say.
    
    tempArr = []
    
    for i in range(len(sample)):
        if sample[i] == None:
            if sample[i+1] != None:
                value = (sample[i-1] + sample[i+1])/2 
                sample[i] = value
            else:
                difference = sample[i-1] - sample[i+2]
                sample[i] = round(sample[i-1] - difference/3)
                sample[i + 1] = round(sample[i] - difference/3)
                
    return sample
                
            
    
#     tempArr = []
#     for i in range(len(sample)):
#         if sample[i] == None:
#             tempArr +=[sample[i-1] , sample[i], sample[i+1]]
#             if sample[i+1] == None:
#                 tempArr += [sample[i+2]]
#             tempArr = fillInNones(tempArr)
#             for j in range(len(tempArr)):
#                 sample[i+j] = tempArr[j]
#     return sample
            
            #So now you have a temp array with either one or two Nones in the middle.
        
def fillInNones(tempArray):
    #Helper Fuction for replace Nones!
    #print(tempArray)
    #Assumes the middle is entirely Nones
    if len(tempArray) <= 2:
        return False
   
    first = tempArray[0]
    last = tempArray[len(tempArray) - 1]
    gap = (first - last)

    average = gap/(len(tempArray)-1)
    
    for i in range(len(tempArray)-2):#so if four, goes 1, 2
        tempArray[i+1] = int(round(first - (average * (i +1))))
    return tempArray
    

        
        
        
        
        ################################## Set statistics ###############################
        
def highestValuesInEachSample(dataSet):
    arr = []
    for d in dataSet:
        arr += [max(d)]
    return arr

def graphSample(sampleNumber):
    return
    #plot line

def updateDataframe():
    return
    #connect to DB
    #

    ##########################################################################################################
def getDBdata(dbID):
  return tempData
  data = tempData
  data = stringToArr(data)
  dic = {}
  for i in range(len(data)):
      dic[i] = data[i]
  dic2 = cleanDict(dic)

  return dic2



def genDBhtml(dbID):

  data = getDBdata(dbID)
  return data
  data = getDBdata(dbID)
  string = ""
  for key in data:
    string += data[key]

  return string


def databaseForm(cursor):

  selectDB = """<h1>Select Database: </h1> <select name="dbID">"""
  try:
    cursor.execute("""select distinct dataID from fypDB""")
    # lst = []
    if form.getvalue('dbID'):
      for row in cursor.fetchall():
        if row['dataID'] == form.getvalue('dbID'):
          selectDB += """<option selected="selected" value="%s">%s</option>""" % (row['dataID'], row['dataID'])
        else:
          selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])
    else:
      for row in cursor.fetchall():
        selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])

    selectDB += "</select>"
    formCode = ("""<form action = "DB.py" method = "post" target = "_self">%s
      <input type = "submit" value = "Go" /></form>""" % (selectDB))
    return formCode
  except (db.Error, IOError) as e:
    print(e)
    return('databaseForm Error')

if form.getvalue('dbID'):
  formCode = databaseForm(cursor)
  dbID = form.getvalue('dbID')
  dbHTML = """<img src="overall.png" alt="graph"><img src="week1week2.png" alt="graph"><img src="Percentage Decrease.png" alt="graph">"""
  #dbHTML = getDBdata(dbID) 

else:
  formCode = databaseForm(cursor)



body = ("""
  <!DOCTYPE html>
  <html>
  <title>Database</title>
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
      <a href="upload.py" class="w3-bar-item w3-button w3-hide-small w3-hover-white" >Upload</a>
      <a href="DB.py" class="w3-bar-item w3-button w3-theme-l1" >Database</a>

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
        <h1 class="w3-text-teal">Search</h1>
        %s
      </div>
      <div>
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
</html>""" % (formCode, dbHTML))

print(body)