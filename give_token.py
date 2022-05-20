import json
import os

token = ""

with open('config.json') as f:
    data = json.load(f)
    token = data['TOKEN']

if token == "in railway":
    token = os.environ["DISCORD_TOKEN"]
else:
    pass
