import discord
from discord.ext import commands
import platform, psutil

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['정보'])
    async def info(ctx):
        embed=discord.Embed(title="정보", description="railway.app으로 호스팅 중")
        embed.add_field(name="운영체제", value="OS" + platform.system() + " : " + platform.version(), inline=False)
        embed.add_field(name="CPU", value=platform.processor(), inline=False)
        embed.add_field(name="Ram", value=str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)", inline=False)
        embed.set_footer(text="Railway.app")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
