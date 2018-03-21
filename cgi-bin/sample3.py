#!/usr/local/bin/python3
from cgitb import enable 
from code import *
from sampleObject import *
enable()
import cgitb
import cgi
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
import pymysql as db
from os import environ
import re

cgitb.enable()
form = cgi.FieldStorage()
cursor = getCursor()

print("Content-Type: text/html")
print()

so = sampleObject('x', 1, '5000000,4000,2000,5,4,,2,')


print(so.getAdjustedArray(True))

