#!/usr/local/bin/python3
import os
 
print("Content-Type: text/html")
print()
 
import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()
print("Hi from test.py")

print("<font size=+1>Environment</font><\br>")
for param in os.environ.keys():
   print("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))