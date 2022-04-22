import discord
import datetime
from datetime import timedelta
from discord.ext import commands


class Commands(commands.Cog):
    """Comandos de interação"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bibi")
    async def rep1(self, ctx):
        name = ctx.author.mention
        response = f'{name} o Bianchini é um jogador de lol falido'

        await ctx.send(response)

    @commands.command(name="jao")
    async def rep2(self, ctx):
        name = ctx.author.mention

        response = f'{name} o dono desse servidor te come em segredo rsrsrs!'

        await ctx.send(response)

    @commands.command(name="hora")
    async def rep3(self, ctx):
        name = ctx.author.mention

        now1 = datetime.datetime.now()
        x = timedelta(hours=3)
        xx = timedelta(minutes=1)
        now1 = now1 - x + xx
        now1 = now1.strftime("%H:%M do dia: %d/%m/%Y")

        response = f'{name}, a hora certa é: {now1}'

        await ctx.send(response)

    @commands.command(name="convite")
    async def embed(self, ctx):
        nn = ctx.author.mention

        embed_link = discord.Embed(description=f"{nn} é link que você quer??? Então toma sua safada!",
                                   colour=6606329)

        embed_link.set_author(name="Ajudante Especial")
        embed_link.set_thumbnail(url='https://i.gifer.com/XOsX.gif')
        embed_link.add_field(name="Link:", value='https://discord.gg/TrasB5W', inline=False)

        await ctx.send(embed=embed_link)


def setup(bot):
    bot.add_cog(Commands(bot))
