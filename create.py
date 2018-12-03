#!C:\Users\super\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os
print("Content-Type: text/html")
print()


def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + \
            '<li><a href="index.py?id={name}">{name}</a></li>'.format(
                name=item)
    return listStr


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
    <form action="create_process.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="6" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"><p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=getList()))
