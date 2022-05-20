import requests as r
import os

cur = os.getcwd() + "\\users_data\\"

if not os.path.exists(cur):
    os.makedirs(cur)

urla = "https://randomuser.me/api/"
data1 = r.get(urla).json()["data1"]
for i in range(len(data1)):
    new_cur1 = cur + str(data1[i]["id"])
    if not os.path.exist(new_cur1):
        os.makedirs(new_cur1)

    file_dir1 = new_cur1 + "\\user_info.txt"
    name = data1[i][name]
    with open(file_dir1, mode="w") as f:
        f.write("name: {}\nname")

    image = r.get(urla)
    image_dir = new_cur1 + "\\avatar.jpg"
    with open(image_dir, "wb") as f:
        f.write(image.content)

url2 = "https://catfact.ninja/fact"
data2 = r.get(url2).json()["data2"]
for i in range(len(data2)):
    new_cur2 = cur + str(data2[i]["id"])
    if not os.path.exist(new_cur2):
        os.makedirs(new_cur2)

    file_dir2 = new_cur2 + "\\cat_fact.txt"
    fact = data2[i][fact]
    with open(file_dir2, "w") as f:
        f.write("fact: {}\nfact")





