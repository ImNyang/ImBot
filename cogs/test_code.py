import discord
from discord.ext import commands


class TestCode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Hi','hi','Hello', 'hello', '안녕하세요'])
    async def 안녕(ctx):
        await ctx.reply("반갑습니다 {}님! 저는 ImBot입니다! 궁금한점이 있다면 `냥 help`를 입력해주세요!".format(
            ctx.author.name))

    @commands.command(aliases=['테스트'])
    async def test(self, ctx):
        msg = await ctx.reply(f"📡ㅣ{round(round(self.bot.latency, 4)*1000)}ms 테스트 완료! 이 메시지는 3초 뒤에 삭제됩니다.")
        await msg.delete(delay=3)

def setup(bot):
    bot.add_cog(TestCode(bot))
