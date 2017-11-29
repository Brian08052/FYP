#!/usr/local/bin/python3
 
print("Content-Type: text/html")
print()
 
import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()
print("Hi from test.py")