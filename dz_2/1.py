import re

text = '''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
    <head>
        <meta charset="UTF-8">
        <title>Хуй, говно и муравей</title>
    </head>
    <body>
        <h1><font color="blue">Хуй, говно и муравей</font></h1>
        <h5><font color="#696969">Трек – Александр Алексеевич Лаэртский
</font></h5>
        <div><font color="red">Текст песни</font></div>
        <p>Хуй, говно и муравей x3</p>
        <p>Хуй, говно да муравей</p>
        <h1> оп оп </h1>
    </body>
</html>'''
div = re.search('<div>', text, True)
if div:
    print('div ok')
p = re.search('<p>', text, True)
if p:
    print('p ok')
h1 = re.search('<h1>', text, True)
if h1:
    print('h1 ok')
