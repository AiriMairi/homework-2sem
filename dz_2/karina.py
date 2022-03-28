import re
s = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div>
        <h1>Zagalovok</h1>
        <p>Some paragraph 1</p>
        <p>Some paragraph 2</p>
    </div>
</body>
</html>"""
res1 = re.search("<h1>", s)
res2 = re.search("<p>", s)
res3 = re.search("<div>")