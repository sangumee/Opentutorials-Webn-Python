#!C:\Users\super\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os
import view
import html_sanitizer

sanitizer = html_sanitizer.Sanitizer()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value

    description = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)

    update_link = '<a href="update.py?id={}">Update</a>'.format(pageId)
    delete_action = '''
        <form action="delete_process.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
    description = 'Hello, Web'
    update_link = ''
    delete_action = ''

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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(
    title=pageId,
    desc=description,
      listStr=view.getList(),
      update_link=update_link,
      delete_action=delete_action))
