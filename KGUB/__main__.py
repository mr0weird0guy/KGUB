from KGUB import LOGGER, Client, TOKEN
from KGUB import cogs
from discord.ext import commands


# when bot is ready (Bot start)
@Client.event
async def on_ready():
    # Loading Cogs
    await cogs.alive.setup(Client)
    LOGGER.info(f"Bot is Ready and Online as {Client.user.name}")


@Client.event
async def on_message(message):
    # Makes BOT ignores itself
    if message.author == Client.user:
        return
    if message.content == "?start":
        await message.channel.send("BOT is started")


# Not Working
@Client.command("test")
async def test(message):
    await message.channel.send("Hey {0.author.mention}! How are you?".format(message))


if __name__ == "__main__":
    Client.run(TOKEN)
