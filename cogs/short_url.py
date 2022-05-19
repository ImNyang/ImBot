import discord
from discord.ext import commands
import pyshorteners as ps

class ShortUrl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['url', 'url단축', 'short', 'shorturl', '링크', '링크단축'])
    async def link(ctx, url:str):
        sh = ps.Shortener()
        short_url = (sh.tinyurl.short(url))
        await ctx.reply(short_url)

def setup(bot):
    bot.add_cog(ShortUrl(bot))
