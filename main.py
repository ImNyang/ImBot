#라이브러리 안쓰는거 같지만 다 씀

import discord
from discord.ext import commands
import random, platform, psutil, asyncio, jishaku, os, json

#함수 설정

bot = commands.Bot(command_prefix='냥 ',)
bot.remove_command('help')
bot.load_extension('jishaku')

#event 처리

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    user = await bot.fetch_user("909353223901569035")
    await user.send("<:neko_party:943083727901302834>ㅣ봇이 준비되었습니다!")

@bot.event
async def on_command_error(ctx, error):
    embed=discord.Embed(title="Error!", description="어... 이게 무슨 상황인지 개발자에게 알려주세요!")
    embed.add_field(name="오류 내용", value=f"`{str(error)}`", inline=True)
    embed.set_footer(text="Dm : ImNyang#9009")
    await ctx.send(embed=embed)

# 음악 오류로 안넘어가게 패치

@bot.command(name="재생", description="음악을 재생합니다.", aliases=["play", "p", "ㅔ", "대기", "queue", "q", "ㅂ"])
async def play(self, ctx, *, url):
    pass

@bot.command(name='루프', description="재생중인 음악을 무한 반복하거나 무한 반복을 해제합니다.", aliases=["무한반복", "loop", "repeat"])
async def music_loop(self, ctx):
    pass

@bot.command(name="셔플", description="대기 리스트에서 음악을 무작위로 재생합니다.", aliases=["랜덤", "random", "shuffle", "sf", "ㄶ", "ㄴㅎ"])
async def shuffle(self, ctx):
    pass

@bot.command(name="스킵", description="재생중인 음악을 스킵합니다.", aliases=["s", "skip", "ㄴ"])
async def skip(self, ctx):
    pass

@bot.command(name="정지", description="음악 재생을 멈춥니다.", aliases=["stop", "ㄴ새ㅔ"])
async def stop(self, ctx):
    pass

@bot.command(name="일시정지", description="음악을 일시정지합니다.", aliases=["pause", "ps", "ㅔㄴ"])
async def pause(self, ctx):
    pass

@bot.command(name="계속재생", description="음악 일시정지를 해제합니다.", aliases=["resume", "r", "ㄱ"])
async def resume(self, ctx):
    pass

@bot.command(name="강제연결해제", description="봇 오류로 음악 재생에 문제가 발생했을 때 강제로 접속을 해제합니다.", aliases=["나가", "제발나가", "quit", 'leave', 'l', "ㅣ", "dc"])
async def force_quit(self, ctx):
    pass

@bot.command(name="볼륨", description="음악의 볼륨을 조절합니다.", aliases=["volume", "vol", "v", "패ㅣㅕㅡㄷ", "ㅍ"])
async def volume(self, ctx, vol: int = None):
    pass

@bot.command(name="대기리스트", description="현재 대기 리스트를 보여줍니다.", aliases=["대기열", "재생리스트", "pl", "ql", "queuelist", "playlist", "비", "ㅔㅣ"])
async def queue_list(self, ctx):
    pass

#아래부터 찐 코드

@bot.command(aliases=['핑', 'pong', '퐁'])
async def ping(ctx):
    embed=discord.Embed(title="🏓ㅣ퐁!")
    embed.add_field(name=f"{round(round(bot.latency, 4)*1000)}", value="ms", inline=True)
    await ctx.reply(embed=embed)

@bot.command(aliases=['도움', '도움말', '명령어'])
async def help(ctx):
    embed=discord.Embed(title="❔ㅣ도움말", description="Prefix : `냥 `")
    embed.add_field(name="`핑`, `퐁`, `ping`, `pong`", value="퐁!", inline=True)
    embed.add_field(name="`청소`, `지워`, `삭제`, `clean`, `clear`", value="챗을 정리합니다. (최대 갯수 없음 하지만 렉으로 인한 봇이 죽을 가능성 있음)", inline=True)
    embed.add_field(name="`밴`, `죽어라`, `ven`, `ban`", value="유저를 ven합니다!", inline=True)
    embed.add_field(name="`언밴`, `살어라`, `unven`, `unban`", value="유저를 unven합니다!", inline=True)
    embed.add_field(name="`킥`, `kick`", value="유저를 킥합니다!", inline=True)
    embed.add_field(name="`가위바위보`, `rockscissorspaper`", value="가위바위보 가위, 바위, 보", inline=True)
    embed.add_field(name="`주사위`, `dice`", value="데구루르!", inline=True)
    embed.add_field(name="`동전`, `동전던지기`, `coin`", value="데구루르! 틱!", inline=True)
    embed.add_field(name="`음악_도움말`, `음악_도움`", value="음악", inline=True)
    await ctx.reply(embed=embed)

@bot.command(aliases=['Hi','hi','Hello', 'hello', '안녕하세요'])
async def 안녕(ctx):
    await ctx.reply("반갑습니다 {}님! 저는 ImBot입니다! 궁금한점이 있다면 `냥 help`를 입력해주세요!".format(
        ctx.author.name))

@bot.command(aliases=['테스트'])
async def test(ctx):
   msg = await ctx.reply(f"📡ㅣ{round(round(bot.latency, 4)*1000)}ms 테스트 완료! 이 메시지는 3초 뒤에 삭제됩니다.")
   await msg.delete(delay=3)

@commands.has_permissions(kick_members=True)
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
    """ command to unban user. check !help unban """
    await ctx.guild.unban(discord.Object(id=member_id))
    await ctx.reply(f"`sudo unven {member_id}`")

@commands.has_permissions(kick_members=True)
@bot.command(aliases=['킥'])
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    await user.kick(reason=reason)
    await ctx.channel.send(f"`sudo kick {user.name} && reason {reason}`")
    await user.send(f"`sudo kick {user.name} && reason {reason}`")

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

@bot.command(aliases=['정보'])
async def info(ctx):
    embed=discord.Embed(title="정보", description="railway.app으로 호스팅 중")
    embed.add_field(name="운영체제", value="OS" + platform.system() + " : " + platform.version(), inline=False)
    embed.add_field(name="CPU", value=platform.processor(), inline=False)
    embed.add_field(name="Ram", value=str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)", inline=False)
    embed.set_footer(text="Railway.app")
    await ctx.send(embed=embed)

@bot.command()
async def remember(ctx, m=None, *, n=None):
    if m == None or n == None:
        raise commands.CommandNotFound
    elif m == None and n == None:
        raise commands.CommandNotFound
    with open('text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data['str']:
            embed = discord.Embed(color=discord.Colour.red())
            embed.set_author(name=f'{m}은 이미 존재하는 단어입니다.')
            await ctx.reply(embed=embed)
            return False
    data['str'][f'{m}'] = str(n)

    with open('text.json', 'w', encoding='utf-8') as ff:
        json.dump(data,ff,ensure_ascii=False,indent='\t')
    
    embed = discord.Embed(color=discord.Colour.random())
    embed.set_author(name=f'{m}은(는) {n}이라구요? 알려주셔서 감사해요! 익명으로 표시될거지만 심한 말들은 제제되어 삭제될 수 있어요.')
    await ctx.reply(embed=embed)

@bot.command()
async def talk(ctx, q=None):
    try:
        with open('text.json', 'r') as f:
            json_data = json.load(f)
            embed=discord.Embed(color=discord.Colour.random())
            embed.set_author(name=json_data['str'][str(q)])
            await ctx.reply(embed=embed)
    except KeyError:
        await ctx.reply("앗 알아듣지 못했어요!")

bot.run(os.environ["DISCORD_TOKEN"])