import discord
import json
import requests
from discord.ext import commands
from decouple import config


API_KEY = config("api_key")

key_features = {
    'temp': 'Temperatura',
    'feels_like': 'Sensação térmica',
    'temp_min': 'Temperatura miníma',
    'temp_max': 'Temperatura máxima'
}


def parse_data(data):
    data = data['main']
    del data['humidity']
    del data['pressure']
    return data


def weather_message(data, location):
    location = location.title()
    weather_embed = discord.Embed(
        title=f'{location} Weather',
        description=f'Aqui está o clima de {location}',
        color=12732972
    )
    weather_embed.set_thumbnail(url="https://i.pinimg.com/originals/0e/f3/bb/0ef3bb66d9216fffcea9022628f7bb26.gif")

    for key in data:
        weather_embed.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=False
        )

    return weather_embed


class Weather(commands.Cog):
    """Weather Info"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user and message.content.startswith('>tempo'):
            location = message.content.replace(">tempo", "").lower()
            if len(location) >= 1:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
                try:
                    data = json.loads(requests.get(url).content)
                    data = parse_data(data)
                    await message.reply(embed=weather_message(data, location))
                except KeyError:
                    await message.reply('Erro desconhecido! Tente outra cidade')


def setup(bot):
    bot.add_cog(Weather(bot))
