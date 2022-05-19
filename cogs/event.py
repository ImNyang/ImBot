import discord
from discord.ext import commands


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.event
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')
        user = await self.bot.fetch_user("909353223901569035")
        await user.send("<:neko_party:943083727901302834>ㅣ봇이 준비되었습니다!")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="냥 도움말"))

    @commands.event
    async def on_command_error(ctx, error):
        embed=discord.Embed(title="Error!", description="어... 이게 무슨 상황인지 개발자에게 알려주세요!")
        embed.add_field(name="오류 내용", value=f"`{str(error)}`", inline=True)
        embed.set_footer(text="Dm : ImNyang#9009")
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Event(bot))
