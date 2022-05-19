#라이브러리 안쓰는거 같지만 다 씀

import discord
from discord.ext import commands
import jishaku, os

#함수 설정

bot = commands.Bot(command_prefix='냥 ',)
bot.remove_command('help')
bot.load_extension('jishaku')

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

bot.run(os.environ["DISCORD_TOKEN"])