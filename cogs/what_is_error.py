import discord
from discord.ext import commands


class WhatIsError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.event
    async def on_command_error(ctx, error):
        embed=discord.Embed(title="Error!", description="어... 이게 무슨 상황인지 개발자에게 알려주세요!")
        embed.add_field(name="오류 내용", value=f"`{str(error)}`", inline=True)
        embed.set_footer(text="Dm : ImNyang#9009")
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(WhatIsError(bot))
