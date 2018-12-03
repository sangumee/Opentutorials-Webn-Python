#!C:\Users\super\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
import os

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

# Redirection
print("Location: index.py")
print()
