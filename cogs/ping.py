import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['핑', 'pong', '퐁'])
    async def ping(self, ctx):
        embed=discord.Embed(title="🏓ㅣ퐁!")
        embed.add_field(name=f"{round(round(self.bot.latency, 4)*1000)}", value="ms", inline=True)
        await ctx.reply(embed=embed)
    

def setup(bot):
    bot.add_cog(Ping(bot))
