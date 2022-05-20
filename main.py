#라이브러리 안쓰는거 같지만 다 씀

import discord
from discord.ext import commands
import jishaku, os, json
import give_token

#함수 설정

what_is_prefix = ""

with open('config.json') as f:
    data = json.load(f)
    what_is_prefix = data["PREFIX"]
    turn_jsk = data["JSK"]# 왜 Prefix로 해두고 있었지

bot = commands.Bot(command_prefix=what_is_prefix)

if turn_jsk == "True":
    bot.load_extension('jishaku')
elif turn_jsk == "False":
    pass
else:
    pass

#cog

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

bot.run(give_token.token())
