import discord
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['유저', '유저_정보','user_info'])
    async def profile(ctx):
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
    

def setup(bot):
    bot.add_cog(UserInfo(bot))
