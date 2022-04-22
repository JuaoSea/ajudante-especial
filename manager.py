import discord
import datetime
from datetime import timedelta
from discord.ext import commands
from decouple import config

now = datetime.datetime.now()
y = timedelta(hours=3)
y2 = timedelta(minutes=1)
now = now - y + y2
now = now.strftime("%H:%M do dia: %d/%m/%Y")


class Manager(commands.Cog):
    """Manager"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        atividade = discord.Game(name="v4.4.1 ✅")
        await self.bot.change_presence(status=discord.Status.online, activity=atividade)

        mt_dono = config("user_dono")
        dn = f'{mt_dono}'

        cc = self.bot.get_channel(929643631437025291)
        await cc.send(f'{dn} o deploy foi feito às: {now}')

        pingdeploy = round(self.bot.latency * 1000)
        print(f'Deploy pronto! Conectado como: {self.bot.user} com {pingdeploy} de ping às {now}')


def setup(bot):
    bot.add_cog(Manager(bot))
