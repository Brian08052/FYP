#!/usr/local/bin/python3
from code import *
from cgitb import enable 
enable()
print('Content-Type: text/html')
print()

url = ""
body = ""
cursor = getCursor()
form = FieldStorage()
COUNT = 8


def genPreview(artistName, description, photo):
  print(artistName, description, photo)
  s = ("""<div class='w3-quarter'; box-shadow: 10px 10px 5px #888888;>
      <img src='ticketsPhotos/%s' alt='%s' style='width:100%%'>
      <h3>%s</h3><a href='http://example.com'>
      <p color = 'red'>%s</p></a>
    </div>"""%(photo, artistName, artistName, description))
  return s



def fillPreviews():
  previews = []
  try:
    cursor.execute("""select * from ticketsDB where ranking between 1 and %s"""%(COUNT))
    # lst = []
    for row in cursor.fetchall():
        priceString = '€'
        priceString += str(row['price'])
        previews += [genPreview(row['name'], priceString, row["photo"] )]

    return previews

  except (db.Error, IOError) as e:
    print(e)
    return('databaseForm Error')

previews = fillPreviews()

print(len(previews))



#preview1 = ""
#...
#preview8 = ""
#previews = [preview1, ... ,preview8]
#select * from db where ranking between 1 and 8
#for i in range(len(row in fetchall))
#row = fetchall[i]
#pricestring = '€'
#pricestring += genPerview['price']
#preview = genPerview(row['name'], priceString, row[""] )




body = """


<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="mycss.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karma">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Karma", sans-serif}
.w3-bar-block .w3-bar-item {padding:20px}
</style>
<body>

<!-- Sidebar (hidden by default) -->
<nav class="w3-sidebar w3-bar-block w3-card w3-top w3-xlarge w3-animate-left" style="display:none;z-index:2;width:40%;min-width:300px" id="mySidebar">
  <a href="javascript:void(0)" onclick="w3_close()"
  class="w3-bar-item w3-button">Close Menu</a>
  <a href="#food" onclick="w3_close()" class="w3-bar-item w3-button">What's Hot</a>
  <a href="#about" onclick="w3_close()" class="w3-bar-item w3-button">Concerts</a>
  <a href="#about" onclick="w3_close()" class="w3-bar-item w3-button">Sports</a>
  <a href="#about" onclick="w3_close()" class="w3-bar-item w3-button">Festivals</a>
</nav>

<!-- Top menu -->
<div class="w3-top">
  <div class="w3-white w3-xlarge" style="max-width:1200px;margin:auto">
    <div class="w3-button w3-padding-16 w3-left" onclick="w3_open()">☰</div>
    <div class="w3-right w3-padding-16">Mail</div>
    <div class="w3-center w3-padding-16">Clearview Tickets</div>
  </div>
</div>
  
<!-- !PAGE CONTENT! -->
<div class="w3-main w3-content w3-padding" style="max-width:1200px;margin-top:100px">

  <!-- First Photo Grid-->
  <div class="w3-row-padding w3-padding-16 w3-center" id="food">"""

for i in range(4):
  body += previews[i]

body += """</div>
  
  <!-- Second Photo Grid-->
  <div class="w3-row-padding w3-padding-16 w3-center">"""

for i in range(4,8):
  body += previews[i]

body += """</div>"""

body += """

  <!-- Pagination -->
  <div class="w3-center w3-padding-32">
    <div class="w3-bar">
      <a href="#" class="w3-bar-item w3-button w3-hover-black">«</a>
      <a href="#" class="w3-bar-item w3-black w3-button">1</a>
      <a href="#" class="w3-bar-item w3-button w3-hover-black">2</a>
      <a href="#" class="w3-bar-item w3-button w3-hover-black">3</a>
      <a href="#" class="w3-bar-item w3-button w3-hover-black">4</a>
      <a href="#" class="w3-bar-item w3-button w3-hover-black">»</a>
    </div>
  </div>
  
  <hr id="about">

  <!-- About Section -->
  <div class="w3-container w3-padding-32 w3-center">  
    <h3>About Us, The Ticket Guys</h3><br>
    <img src="/w3images/chef.jpg" alt="Me" class="w3-image" style="display:block;margin:auto" width="800" height="533">
    <div class="w3-padding-32">
      <h4><b>I am Who I Am!</b></h4>
      <h6><i>With Passion For Real, Good Tickets</i></h6>
      <p>Just me, myself and I, exploring the universe of unknownment. I have a heart of love and an interest of lorem ipsum and mauris neque quam blog. I want to share my world with you. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>
    </div>
  </div>
  <hr>
  
  <!-- Footer -->
  <footer class="w3-row-padding w3-padding-32">
    <div class="w3-third">
      <h3>FOOTER</h3>
      <p>Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>
      <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
    </div>
  
    <div class="w3-third">
      <h3>BLOG POSTS</h3>
      <ul class="w3-ul w3-hoverable">
        <li class="w3-padding-16">
          <img src="/w3images/workshop.jpg" class="w3-left w3-margin-right" style="width:50px">
          <span class="w3-large">Lorem</span><br>
          <span>Sed mattis nunc</span>
        </li>
        <li class="w3-padding-16">
          <img src="/w3images/gondol.jpg" class="w3-left w3-margin-right" style="width:50px">
          <span class="w3-large">Ipsum</span><br>
          <span>Praes tinci sed</span>
        </li> 
      </ul>
    </div>

    <div class="w3-third w3-serif">
      <h3>POPULAR TAGS</h3>
      <p>
        <span class="w3-tag w3-black w3-margin-bottom">Music</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Rock</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">College Gigs</span>
        <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Local artists</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Cork</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">London</span>
        <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Dublin</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Comedy</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">GAA</span>
        <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Rugby</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Pop</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Electronic</span>
        <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Acoustic</span> <span class="w3-tag w3-dark-grey w3-small w3-margin-bottom">Live Musics</span>
      </p>
    </div>
  </footer>

<!-- End page content -->
</div>

<script>
// Script to open and close sidebar
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
}
 
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}
</script>

</body>
</html>"""

print(body)
