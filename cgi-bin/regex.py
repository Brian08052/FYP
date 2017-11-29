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
  print('x')
  return s



def fillPreviews():
  previews = []
  try:
    cursor.execute("""select * from ticketsDB where ranking between 1 and %s"""%(COUNT))
    # lst = []
    for row in cursor.fetchall():
        priceString = '€'
        priceString += str(row['price'])
        print(row['name'], priceString, row["photo"])
        previews += [genPreview(row['name'], priceString, row["photo"] )]

    return previews

  except (db.Error, IOError) as e:
    print(e)
    return('databaseForm Error')
