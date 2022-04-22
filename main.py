import os
from discord_components import ComponentsBot
from decouple import config

bot = ComponentsBot(">")


def load_cogs(init):

    init.load_extension("manager")

    for file in os.listdir("command"):
        if file.endswith(".py"):
            cog = file[:-3]
            init.load_extension(f"command.{cog}")


load_cogs(bot)

TOKEN = config("secret_token")
bot.run(TOKEN)
