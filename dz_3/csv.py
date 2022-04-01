import csv

class User():
    def __init__(self, color, message, music, community, news):
        color.self = color
        message.self = message
        music.self = music
        community.self = community
        news.self = news

    def message(self):
        with open("message.csv", "w") as file:
            writer = csv.writer(file)


