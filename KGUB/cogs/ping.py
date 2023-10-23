import time
from discord.ext import commands


class Ping(commands.Cog):
    # innitialization of the Ping class
    def __init__(self, bot):
        self.bot = bot

# the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # parameters:
    # 1st as bot,
    # 2nd as the context
    async def ping(self: commands.Bot, ctx: commands.Context):
        # take the time of the call of the command
        start_time = time.time()
        # sends a text to the server channel
        message = await ctx.send("Pinging...")
        # takes the time of ending of the command call
        end_time = time.time()
        # Takes the difference which is the ping time of the command/bot
        ping_time = round((end_time - start_time) * 1000, 3)
        # chaneges the text and update to the time duration of command call and its execution
        await message.edit(content="PONG: {}ms".format(ping_time))

# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(bot: commands.Bot):
    # Calls the Ping Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await bot.add_cog(Ping(bot))
