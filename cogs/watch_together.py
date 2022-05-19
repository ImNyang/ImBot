import discord
from discord.ext import commands
from discord_together import DiscordTogether

class WatchTogether(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['유튜브','유튭'])
    async def youtube(self, ctx):
        link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.reply(f"아래 링크를 클릭하세요!\n{link}")
    

def setup(bot):
    bot.add_cog(WatchTogether(bot))
