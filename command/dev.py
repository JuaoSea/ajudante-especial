import discord
from discord.ext import commands
from decouple import config


class Dev(commands.Cog):
    """Comandos de desenvolvedor"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):

        latency = round(self.bot.latency * 1000)

        await ctx.send(f'Bot ping: {latency} ms')

    @commands.command(name="manager")
    @commands.has_permissions(administrator=True)
    async def manager(self, ctx):
        LINK1 = config("link1")
        LINK2 = config("link2")

        nn = ctx.author.mention

        embed_man = discord.Embed(title="Manager", description=f"*{nn}, tá ai os links de manutenção*",
                                  colour=7064575)

        embed_man.set_author(name="Ajudante Especial")
        embed_man.set_thumbnail(url='https://c.tenor.com/zWnTBUB0_kUAAAAC/michael-scott-the-manager.gif')
        embed_man.add_field(name="Links:", value="**Autorizar bot no server:** {}"
                                                 "\n"
                                                 "\n **Discord developer portal:** {}".format(LINK1, LINK2),
                            inline=False)

        await ctx.send(embed=embed_man)

    @commands.command(aliases=['purge'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=10):
        if amount > 101:
            await ctx.send(f'{ctx.author.mention} desculpe, não posso deletar mais que 10 mensagens')
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'{ctx.author.mention} Feito! 🧹😉')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{ctx.author.mention}, o membro: {member.mention} foi kickado pra casa do baralho 🃏!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{ctx.author.mention}, o membro: {member.mention} foi banido pra casa do baralho 🃏!')


def setup(bot):
    bot.add_cog(Dev(bot))
