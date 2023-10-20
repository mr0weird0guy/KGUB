from KGUB import LOGGER, Client, TOKEN
from KGUB import cogs
from discord.ext import commands


# when bot is ready (Bot start)
@Client.event
async def on_ready():
    # Loading Cogs
    await cogs.alive.setup(Client)
    await cogs.attendance.setup(Client)
    await cogs.owo.setup(Client)
    LOGGER.info(f"Bot is Ready and Online as {Client.user.name}")


if __name__ == "__main__":
    Client.run(TOKEN)
