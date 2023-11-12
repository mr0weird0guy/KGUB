import sys
from KGUB import LOGGER, Client, TOKEN
from KGUB import cogs
from discord.ext import commands


# when bot is ready (Bot start)
@Client.event
async def on_ready():
    # Loading Cogs commands
    await cogs.alive.setup(Client)
    await cogs.attendance.setup(Client)
    # await cogs.owo.setup(Client)
    await cogs.get_link.setup(Client)
    await cogs.ping.setup(Client)
    await cogs.summup.setup(Client)
    await cogs.popular.setup(Client)
    await cogs.fun.setup(Client)
    # await cogs.welcomer.setup(Client)
    LOGGER.info(f"Bot is Ready and Online as {Client.user.name}")


# this is the first thing that runs when the bot is ready
if __name__ == "__main__":
    try:
        # This takes the token from the KGUB module and runs it
        Client.run(TOKEN)
    # If the user cancels the command(Ctrl+C or Delete), it is handled by the except statement.
    except KeyboardInterrupt:
        LOGGER.info("Bot stopped by the user")
        sys.exit(0)
        # this stops the bot
