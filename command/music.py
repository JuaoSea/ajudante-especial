import discord
from discord.ext import commands
from discord.utils import get


class Music(commands.Cog):
    """Music"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)

        else:
            await channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("")

    @commands.command(pass_context=True)
    async def play(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        await voice.play(discord.FFmpegPCMAudio("command/brasil.mp3"))


def setup(bot):
    bot.add_cog(Music(bot))
