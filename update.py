#!C:\Users\super\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os
import view
print("Content-Type: text/html")
print()


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value

    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, Web'

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">Create</a>
    <form action="update_process.py" method="post">
    <input type="hidden" name="pageId" value="{form_default_title}">
    <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
    <p><textarea rows="6" name="description" placeholder="description">{form_default_description}</textarea></p>
    <p><input type="submit"><p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_default_description=description))
