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
import code

# needs to check if info is already in before inserting

def getCursor():
    try:
      connection = db.connect('cs1.ucc.ie', 'bgl1', 'maGhii6o', '2018_bgl1')
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

url = ""
body = ""
print('Content-Type: text/html')
print()

  

cursor = getCursor()
form = FieldStorage()

def databaseForm(cursor):

  selectDB = """<h1>Select Database: </h1> <select name="dbID">"""
  try:
    cursor.execute("""select distinct dataID from fypDB""")
    # lst = []
    for row in cursor.fetchall():
        # lst+=[row['dataID']]
      selectDB += """<option value="%s">%s</option>""" % (row['dataID'], row['dataID'])

    selectDB += "</select>"
    formCode = ("""<form action = "home.py" method = "post" target = "_self">%s
      <input type = "submit" value = "Go" /></form>""" % (selectDB))
    return formCode
  except (db.Error, IOError) as e:
    print(e)
    return('databaseForm Error')

if form.getvalue('dbID'):

  try:
    formCode = databaseForm(cursor)
    databaseID = form.getvalue('dbID')
    selectSample = "<select name='sampleID'>"
    cursor.execute("""select distinct sampleID from fypDB where dataID = %s""" % (databaseID))
    # lst = []
    for row in cursor.fetchall():
          # lst+=[row['dataID']]
      selectSample += """<option value="%s">%s</option>""" % (row['sampleID'], row['sampleID'])

    selectSample += "</select>"
    formCode += ("""<h1?Database: %s Select Sample</h1><form action = "sample.py" method = "post" target = "_self">%s
        <input type="hidden" value="true" name="search" />
        <input type="hidden" value="%s" name="dbID" /><input type = "submit" value = "Go" /></form>""" % (databaseID, selectSample,databaseID))
  except (db.Error, IOError) as e:
    print(e)

else:
  formCode = databaseForm(cursor)

  


body = ("""
<!DOCTYPE html>
<html>
<title>Search</title>
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
    <a href="upload.py" class="w3-bar-item w3-button w3-theme-l1" >Upload</a>

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
</html>""" % (formCode))

print(body)