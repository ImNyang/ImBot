'''
import json
import os

global 토큰

with open('config.json') as f:
    data = json.load(f)
    temp = data['TOKEN']

if temp == "in railway":
    토큰 = os.environ.get("DISCORD_TOKEN")
else:
    토큰 = str(data['TOKEN'])
'''