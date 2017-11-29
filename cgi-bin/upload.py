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
from codetest import *
test()
#c = getCursor()

#needs to check if info is already in before inserting 

url = ""
body = ""

lst = []

select = """<select name="dbID">"""

print('Content-Type: text/html')
print()


try:
  connection = db.connect('cs1.ucc.ie', 'bgl1', 'maGhii6o', '2018_bgl1')
  cursor = connection.cursor(db.cursors.DictCursor)
  cursor.execute("""select distinct dataID from fypDB""")
except (db.Error, IOError) as e:
    print(e)
    #result = """<p>Sorry, we are experiencing database problems! People get on to Brian 0</p>"""
    
if True:
  if cursor.rowcount == 0:
      dbresult = '<p>You have no data</p>'
  else:
      for row in cursor.fetchall():
          lst+=[row['dataID']]
          select +="""<option value="%s">%s</option>"""%(row['dataID'],row['dataID'])
          
select += "</select>"
form = ("""<form action = "sample.py" method = "post" target = "_blank">%s
<textarea name = "textcontent" cols = "40" rows = "4">
Type your text here...
</textarea>
<input type = "submit" value = "Submit" />
</form>"""%(select))


body = ("""
<!DOCTYPE html>
<html>
<title>Upload</title>
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
    <a href="#" class="w3-bar-item w3-button w3-theme-l1" >Upload</a>

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
      <h1 class="w3-text-teal">Upload</h1>
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
</html>"""%(form))

print(body)
