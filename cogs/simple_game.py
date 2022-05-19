import discord
from discord.ext import commands
import random

class SimpleGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['가위바위보'])
    async def rockscissorspaper(ctx, user: str):
        rps_table = ['가위', '바위', '보']
        bot = random.choice(rps_table)
        result = rps_table.index(user) - rps_table.index(bot)
        if result == 0:
            embed=discord.Embed(title="✌️ㅣ가위바위보!", description=f"{user} vs {bot}  비겼습니다.")
            await ctx.reply(embed=embed)
        elif result == 1 or result == -2:
            embed=discord.Embed(title="✌️ㅣ가위바위보!", description=f"{user} vs {bot}  유저가 이겼습니다.")
            await ctx.reply(embed=embed)
        else:
            embed=discord.Embed(title="✌️ㅣ가위바위보!", description=f"{user} vs {bot}  봇이 이겼습니다.")
            await ctx.reply(embed=embed)

    @commands.command(aliases=['주사위'])
    async def dice(ctx):
        randomNum = random.randrange(1, 7)
        print(randomNum)
        if randomNum == 1:
            await ctx.reply(embed=discord.Embed(title="🎲ㅣ주사위", description='🎲'+ '1️⃣'))
        if randomNum == 2:
            await ctx.reply(embed=discord.Embed(title="🎲ㅣ주사위", description='🎲' + '2️⃣'))
        if randomNum ==3:
            await ctx.reply(embed=discord.Embed(title="🎲ㅣ주사위", description='🎲' + '3️⃣'))
        if randomNum ==4:
            await ctx.reply(embed=discord.Embed(title="🎲ㅣ주사위", description='🎲' + '4️⃣'))
        if randomNum ==5:
            await ctx.reply(embed=discord.Embed(title="🎲ㅣ주사위", description='🎲' + '5️⃣'))
        if randomNum ==6:
            await ctx.reply(embed=discord.Embed(title="✌️ㅣ가위바위보!", description='🎲' + '6️⃣'))

    @commands.command(aliases=['동전', '동전던지기'])
    async def coin(ctx):
        randomNum = random.randrange(1, 3)
        print(randomNum)
        if randomNum == 1:
            await ctx.reply(embed=discord.Embed(title="🪙ㅣ동전 던지기", description='뒷면!'))
        if randomNum == 2:
            await ctx.reply(embed=discord.Embed(title="🪙ㅣ동전 던지기", description='앞면!'))


def setup(bot):
    bot.add_cog(SimpleGame(bot))
