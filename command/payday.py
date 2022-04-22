import discord
from discord.ext import commands
from discord_components import Select, SelectOption
from decouple import config

user_id = config("user_id")
owner_id = config("owner_id")


class Payday(commands.Cog):
    """DM's PayDay 2"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="payday")
    @commands.has_permissions(administrator=True)
    async def payday(self, ctx):
        target = await self.bot.fetch_user(user_id)
        target2 = await self.bot.fetch_user(owner_id)

        embed_msg = discord.Embed(title="PayDay gameplay",
                                  description=f"*Olá caro Bianchini! FLK JuaoSea te chama para uma jogatina de peidei,"
                                              f" aceitas?* \n \n "
                                              f"**Entre na call:  [🎮 NOBREZA 🎮](https://discord.gg/e6GV8wk75D)**",
                                  colour=3649240)

        embed_msg.set_author(name="Convite de FLK JuaoSea")
        embed_msg.set_image(url="https://c.tenor.com/XD1WB0-kjVgAAAAC/chains-houston.gif")
        embed_msg.set_thumbnail(url="https://i.pinimg.com/474x/9b/6f/eb/9b6febb56e5dcbec6c447d0d3b899f6c.jpg")

        await ctx.send(f'{ctx.author.mention}! Convite de noitada enviado com sucesso')
        await ctx.message.delete()
        await target.send(embed=embed_msg, components=[Select(
            placeholder='Aceitas jogar? Responda ⬇️',
            options=[
                SelectOption(label='Com certeza ✅', value='1'),
                SelectOption(label='Nem fudendo ❌', value='2'),
                SelectOption(label='Daqui a algumas horinhas 🕑', value='3')
            ],
            custom_id='SelectTesting'
        )])
        interaction = await self.bot.wait_for(
            'select_option', check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
        res = interaction.values[0]

        if res == '1':
            embed_1 = discord.Embed(title="Payday 2 noitada",
                                    description=f"**Entre na call:  [🎮 NOBREZA 🎮](https://discord.gg/e6GV8wk75D)**",
                                    colour=3649240)
            await interaction.send('Confirmado ✅')
            await target.send(embed=embed_1)
            await target2.send(f'{target2.mention}, Bianchini aceitou o convite (Payday) ✅')
        elif res == '2':
            await interaction.send('Okay, vai tomar no seu cu então porra 👌')
            await target2.send(f'{target2.mention}, Bianchini não aceitou o convite (Payday) ❌')
        elif res == '3':
            embed_2 = discord.Embed(title="Payday 2 noitada",
                                    description=f"**Agilizando o trabalho:"
                                                f"  [🎮 NOBREZA 🎮](https://discord.gg/e6GV8wk75D)**",
                                    colour=3649240)
            await interaction.send('Confirmado ✅')
            await target.send(embed=embed_2)
            await target2.send(f'{target2.mention}, Bianchini aceitou o convite daqui a algumas horas (Payday) 🕑')


def setup(bot):
    bot.add_cog(Payday(bot))
