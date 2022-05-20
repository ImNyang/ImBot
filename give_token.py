import json
import os

with open('config.json') as f:
    data = json.load(f)
    token = data['TOKEN']

if token == "in railway":
    token = os.environ.get("DISCORD_TOKEN")
else:
    pass