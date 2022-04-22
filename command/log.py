import datetime
from datetime import timedelta
from discord.ext import commands


class Register(commands.Cog):
    """Registro do bot de música"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "!play" in message.content:
            canal = self.bot.get_channel(929643631437025291)

            now2 = datetime.datetime.now()
            yy = timedelta(hours=3)
            yyy = timedelta(minutes=1)
            now2 = now2 - yy + yyy
            now2 = now2.strftime("%H:%M do dia: %d/%m/%Y")

            print(now2)

            await canal.send(f'User: {message.author.name}, utilizou o bot de música às: {now2}')


def setup(bot):
    bot.add_cog(Register(bot))
