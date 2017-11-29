#!/usr/local/bin/python3
 

print("Content-Type: text/html")
print()
 
import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()


body = """<!DOCTYPE html>
<html>
<body>

<form action="upload2.py">
  First name:<br>
  <input type="text" name="firstname" value="Mickey">
  <br>
  Last name:<br>
  <input type="text" name="lastname" value="Mouse">
  <br><br>
  <input type="submit" value="Submit">
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page</p>

</body>
</html>"""
print(body)