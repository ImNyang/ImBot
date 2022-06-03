#라이브러리 안쓰는거 같지만 다 씀

import discord, jishaku, os, json, platform, random, psutil
from discord.ext import commands
import pyshorteners as ps
from discord_together import DiscordTogether

#import give_token as to                오류가 너무 많이남

#함수 설정

what_is_prefix = ""

with open('config.json') as f:
    data = json.load(f)
    what_is_prefix = data["PREFIX"]
    turn_jsk = data["JSK"]# 왜 Prefix로 해두고 있었지
    
bot = commands.Bot(command_prefix=f'{what_is_prefix}', help_command=None)

if turn_jsk == "True":
    bot.load_extension('jishaku')
elif turn_jsk == "False":
    pass

#event
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    user = await bot.fetch_user("909353223901569035")
    await user.send("<:neko_party:943083727901302834>ㅣ봇이 준비되었습니다!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="냥 도움말"))

@bot.event
async def on_command_error(ctx, error):
    embed=discord.Embed(title="Error!", description="어... 이게 무슨 상황인지 개발자에게 알려주세요!")
    embed.add_field(name="오류 내용", value=f"`{str(error)}`", inline=True)
    embed.set_footer(text="Dm : ImNyang#9009")
    await ctx.send(embed=embed)

#help

@bot.command(pass_context=True, aliases=['도움', '도움말', '명령어'])
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
    embed.add_field(name="`내_유저`, `내_유저_정보`, `my_profile`, `my_user_info`", value="자신의 유저의 정보를 알려줍니다.", inline=True)
    embed.add_field(name="`유튜브`, `유튭`, `youtube`", value="음성채널에 들어가서 쓰면 유튜브를 볼 수 있습니다.", inline=True)
    embed.add_field(name="`url`, `short`, `shorturl`, `link`, `url단축`, `링크`, `링크단축`", value="", inline=True)
    await ctx.reply(embed=embed)

#admin command

@commands.has_permissions(administrator=True)
@bot.command(aliases=['청소','clean','지워','삭제'])
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    msg = await ctx.send("<:neko_candy:943083727985180722>ㅣ완료되었습니다! 이 메시지도 곧 삭제됩니다.")
    await msg.delete(delay=3)

@bot.command(aliases=['밴','ven','죽어라'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.ban(reason=reason)
    await ctx.channel.send(f"`sudo ven {user.name} && reason {reason}`")
    await user.send(f"`sudo ven {user.name} && reason {reason}`")

@bot.command(aliases=['언밴','unven','살아라'])
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member_id: int):
    await ctx.guild.unban(discord.Object(id=member_id))
    await ctx.reply(f"`sudo unven {member_id}`")

@commands.has_permissions(kick_members=True)
@bot.command(aliases=['킥'])
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.kick(reason=reason)
    await ctx.channel.send(f"`sudo kick {user.name} && reason {reason}`")
    await user.send(f"`sudo kick {user.name} && reason {reason}`")

#bot-server command

@bot.command(aliases=['정보'])
async def info(ctx):
    embed=discord.Embed(title="정보", description="railway.app으로 호스팅 중")
    embed.add_field(name="운영체제", value="OS" + platform.system() + " : " + platform.version(), inline=False)
    embed.add_field(name="CPU", value=platform.processor(), inline=False)
    embed.add_field(name="Ram", value=str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)", inline=False)
    embed.set_footer(text="Railway.app")
    await ctx.send(embed=embed)

@bot.command(aliases=['핑', 'pong', '퐁'])
async def ping(self, ctx):
    embed=discord.Embed(title="🏓ㅣ퐁!")
    embed.add_field(name=f"{round(round(bot.latency, 4)*1000)}", value="ms", inline=True)
    await ctx.reply(embed=embed)

#game

@bot.command(aliases=['가위바위보'])
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

@bot.command(aliases=['주사위'])
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

@bot.command(aliases=['동전', '동전던지기'])
async def coin(ctx):
    randomNum = random.randrange(1, 3)
    print(randomNum)
    if randomNum == 1:
        await ctx.reply(embed=discord.Embed(title="🪙ㅣ동전 던지기", description='뒷면!'))
    if randomNum == 2:
        await ctx.reply(embed=discord.Embed(title="🪙ㅣ동전 던지기", description='앞면!'))

#utility command

@bot.command(aliases=['url', 'url단축', 'short', 'shorturl', '링크', '링크단축'])
async def link(ctx, url:str):
    sh = ps.Shortener()
    short_url = (sh.tinyurl.short(url))
    await ctx.reply(short_url)

@bot.command(aliases=['내_유저', '내_유저_정보','my_user_info'])
async def my_profile(ctx):
    name = ctx.author.name
    displayname = ctx.author.display_name
    areyoubot = ctx.author.bot
    Id = ctx.author.id
    avatar = ctx.author.avatar_url
    created_at = ctx.author.created_at
    imgisgif = ctx.author.is_avatar_animated()

    embed=discord.Embed()
    embed.set_author(name=f"ㅣ사용자 {name}의 정보", icon_url=avatar)
    embed.add_field(name="🏷ㅣ이름", value=f"{name}", inline=False)
    embed.add_field(name="🏷ㅣ서버에서 쓰는 이름", value=f"{displayname}", inline=False)
    embed.add_field(name="🤖ㅣ봇 여부", value=f"{areyoubot}", inline=False)
    embed.add_field(name="🖼ㅣ프로필 사진 GIF 여부", value=f"{imgisgif}", inline=False)
    embed.add_field(name="🪪ㅣUser ID", value=f"{Id}", inline=False)
    embed.add_field(name="📆ㅣ계정 만든 날 (UTC 기준)", value=f"{created_at}", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['유튜브','유튭'])
async def youtube(self, ctx):
    link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.reply(f"아래 링크를 클릭하세요!\n{link}")

#test_command
@bot.command(aliases=['Hi','hi','Hello', 'hello', '안녕하세요'])
async def 안녕(ctx):
    await ctx.reply("반갑습니다 {}님! 저는 ImBot입니다! 궁금한점이 있다면 `냥 help`를 입력해주세요!".format(
        ctx.author.name))

@bot.command(aliases=['테스트'])
async def test(self, ctx):
    msg = await ctx.reply(f"📡ㅣ{round(round(bot.latency, 4)*1000)}ms 테스트 완료! 이 메시지는 3초 뒤에 삭제됩니다.")
    await msg.delete(delay=3)

bot.run(os.environ.get("DISCORD_TOKEN"))
#bot.run("token")