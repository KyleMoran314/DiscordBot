import os
import json
import requests
from datetime import datetime, date
import calendar
import discord

class Game:
    def __init__(self, name):
        self.name = name
        self.platforms=[]
        self.gamedate=[]

    def addPlatform(self,platform):
        self.platforms.append(platform)
        
    def addHuman(self,human):
        self.gamedate.append(human)

currentTime=datetime.now()

d = datetime(currentTime.year,currentTime.month,currentTime.day,0,0)

timestamp=calendar.timegm(d.timetuple())

URL ="https://api-v3.igdb.com/release_dates"
hdrs = {'user-key': 'YOUR IGDB KEY HERE'}
payload='fields game.name, platform.name,human; where date='+str(timestamp)+';'

r=requests.post(url=URL, headers=hdrs, data=payload)
data=r.json
resp=r.text

resp_string = json.loads(resp)

games=[]

for i in resp_string:
    games.append(i["game"]["name"])

game=list(set(games))

temp=[]
for i in range(len(game)):
    temp.append(Game(game[i]))
    for j in resp_string:
        if game[i]==j["game"]["name"]:
            temp[i].addPlatform(j["platform"]["name"])
            temp[i].addHuman(j["human"])
    
for i in range(len(temp)):
    print(temp[i].name)
    print(temp[i].platforms)
    print(temp[i].gamedate)
    print("")
