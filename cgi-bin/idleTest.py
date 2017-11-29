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

#needs to check if info is already in before inserting 

result = """
   <p>You do not have permission to access this page.</p>
   <ul>
       <p><a href="register.py">Register</a></p>
       <p><a href="login.py">Login</a></p>
   </ul>"""
dbresult=""
table1=''
table2=''
name=''
giglist=[]
form_data = FieldStorage()
        

print('Content-Type: text/html')
print()


try:
  connection = db.connect('cs1.ucc.ie', 'bgl1', 'maGhii6o', '2018_bgl1')
  cursor = connection.cursor(db.cursors.DictCursor)
  cursor.execute("""select year, country from winners""")

except (db.Error, IOError) as e:
    print(e)
    #result = """<p>Sorry, we are experiencing database problems! People get on to Brian 0</p>"""
    
try:
    cursor.execute("""select year, country from winners""")
    if cursor.rowcount == 0:
      dbresult = '<p>You have no selcted gigs</p>'
    else:
        table1= """<table class='t1'><caption class='caps'>Countries</caption>
                          <tr>
                            <th>Year</th>
                            <th>Country</th>
                          </tr>"""
        for row in cursor.fetchall():
            giglist+=[row['year']]
            table1 +="""
                        <tr id='tro' >
                            <td>%s</td>
                            <td>%s</td>
                            </tr>"""%(row['year'],row['country'])
            table1 += """</table><br><br>"""
except (db.Error, IOError) as e:
    print(e)
    

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Show Gigs</title>
            <meta content="">
            <link rel="stylesheet" href="style.css">
          </head>
        <body>
        <header id="headbanner" class="site-header" role="banner">
            <div class="logo">
                <h1 class="site-title"><a id='alog' href="welcome.py" rel="home">Hello, %s! &#124; WB15</a></h1>
        </header>
            %s            
            %s
            %s
        </body>
    </html>""" % (name, result,table1,table2))
