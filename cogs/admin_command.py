import discord
from discord.ext import commands


class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['청소','clean','지워','삭제'])
    async def clear(ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        msg = await ctx.send("<:neko_candy:943083727985180722>ㅣ완료되었습니다! 이 메시지도 곧 삭제됩니다.")
        await msg.delete(delay=3)

    @commands.command(aliases=['밴','ven','죽어라'])
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        await ctx.channel.send(f"`sudo ven {user.name} && reason {reason}`")
        await user.send(f"`sudo ven {user.name} && reason {reason}`")

    @commands.command(aliases=['언밴','unven','살아라'])
    @commands.has_permissions(administrator=True)
    async def unban(ctx, *, member_id: int):
        await ctx.guild.unban(discord.Object(id=member_id))
        await ctx.reply(f"`sudo unven {member_id}`")

    @commands.has_permissions(kick_members=True)
    @commands.command(aliases=['킥'])
    async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        await ctx.channel.send(f"`sudo kick {user.name} && reason {reason}`")
        await user.send(f"`sudo kick {user.name} && reason {reason}`")
    

def setup(bot):
    bot.add_cog(AdminCommand(bot))
