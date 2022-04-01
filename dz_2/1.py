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
    </body>
</html>'''
div = re.search('<div>', text, True)
div1 = re.search('</div>', text, True)
if div and div1:
    print('div ok')
else:
    print('div not ok')
p = re.search('<p>', text, True)
p1 = re.search('</p>', text, True)
if p and p1:
    print('p ok')
else:
    print('p not ok')
h1 = re.search('<h1>', text, True)
h11 = re.search('</h1>', text, True)
if h1 and h11:
    print('h1 ok')
else:
    print('h1 not ok')
