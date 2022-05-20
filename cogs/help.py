from discord.ext import commands
import discord
import json

what_is_prefix = ""

class helpCog:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.remove_command('help')
    
    with open('config.json') as f:
        data = json.load(f)
        what_is_prefix = data["PREFIX"]

    @commands.command(pass_context=True, aliases=['도움', '도움말', '명령어'])
    async def help(ctx):
        embed=discord.Embed(title="❔ㅣ도움말", description=f"Prefix : `{what_is_prefix}`")
        embed.add_field(name="`핑`, `퐁`, `ping`, `pong`", value="퐁!", inline=True)
        embed.add_field(name="`청소`, `지워`, `삭제`, `clean`, `clear`", value="챗을 정리합니다. (최대 갯수 없음 하지만 렉으로 인한 봇이 죽을 가능성 있음)", inline=True)
        embed.add_field(name="`밴`, `죽어라`, `ven`, `ban`", value="유저를 ven합니다!", inline=True)
        embed.add_field(name="`언밴`, `살어라`, `unven`, `unban`", value="유저를 unven합니다!", inline=True)
        embed.add_field(name="`킥`, `kick`", value="유저를 킥합니다!", inline=True)
        embed.add_field(name="`가위바위보`, `rockscissorspaper`", value="가위바위보 가위, 바위, 보", inline=True)
        embed.add_field(name="`주사위`, `dice`", value="데구루르!", inline=True)
        embed.add_field(name="`동전`, `동전던지기`, `coin`", value="데구루르! 틱!", inline=True)
        embed.add_field(name="`정보`, `info`", value="이 봇의 서버 정보입니다,", inline=True)
        embed.add_field(name="`유저`, `유저_정보`, `profile`, `user_info`", value="유저의 정보를 알려줍니다.", inline=True)
        embed.add_field(name="`유튜브`, `유튭`, `youtube`", value="음성채널에 들어가서 쓰면 유튜브를 볼 수 있습니다.", inline=True)
        embed.add_field(name="`url`, `short`, `shorturl`, `link`, `url단축`, `링크`, `링크단축`", value="", inline=True)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(helpCog(bot))