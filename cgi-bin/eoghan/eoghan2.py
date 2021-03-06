#!/usr/local/bin/python3
from code import *
from cgitb import enable 
enable()
print('Content-Type: text/html')
print()
body = """<!DOCTYPE html>
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
  <div class="w3-row-padding w3-padding-16 w3-center" id="food">
  
    <div class="w3-quarter"; box-shadow: 10px 10px 5px #888888;>
      <img src="http://liamgallagher.com/assets/img/site/liam-gallagher-photo.jpg" alt="Liam" style="width:100%">
      <h3>Liam Gallagher</h3><a href="http://example.com">
      <p color = "red">From €75</p></a>
    </div>
    <div class="w3-quarter">
      <img src="https://media.vanityfair.com/photos/589a59c7d1af756e234791ca/master/w_768,c_limit/beyonce-grammys-style-ss17.jpg" alt="Beyonce" style="width:100%">
      <h3>Beyoncé</h3><a href="http://example.com">
      <p color = "red">From €35</p></a>
    </div>
    <div class="w3-quarter">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyizRq31vSP4bAIlQFvzeU8xvNLQFOpHuPXCdI0m2fM8a8rmVydQ" alt="Hozier" style="width:100%">
      <h3>Hozier</h3><a href="http://example.com">
      <p color = "red">From €125</p></a>
    </div>
    <div class="w3-quarter">
      <img src="https://static01.nyt.com/images/2016/11/20/arts/20CARAMANICA/20CARAMANICA-articleLarge.jpg" alt="Soak" style="width:100%">
      <h3>Frank Ocean</h3><a href="http://example.com">
      <p color = "red">From €40</p></a>
    </div>
  </div>
  
  <!-- Second Photo Grid-->
  <div class="w3-row-padding w3-padding-16 w3-center">
    <div class="w3-quarter">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7xBD4cAdStO3_bItQ_rAS8rCVKhZzV2ZBpUtZhiR7gRJVX_-nWg" alt="Lorde" style="width:100%">
      <h3>Lorde</h3><a href="http://example.com">
      <p color = "red">From €75</p></a>
    </div>
    <div class="w3-quarter">
      <img src="https://i.imgur.com/Ig12bLS.jpg?1" alt="Salmon" style="width:100%">
      <h3>Ed Sheeran</h3><a href="http://example.com">
      <p color = "red">From €90</p></a>
    </div>
    <div class="w3-quarter">
      <img src="http://www.billboard.com/files/media/haim-studio-style-bb37-style-2015-billboard-embed.jpg" alt="Sandwich" style="width:100%">
      <h3>Haim</h3><a href="http://example.com">
      <p color = "red">From €15</p></a>
    </div>
    <div class="w3-quarter">
      <img src="http://ladygunn.com/files/2016/11/LADYGUNN-catfish-9805.jpg" alt="Croissant" style="width:100%">
      <h3>Catfish and the Bottlemen</h3><a href="http://example.com">
      <p color = "red">From €35</p></a>
    </div>
  </div>

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
s = u' '.join((body)).encode('utf-8').strip()
print(s)
