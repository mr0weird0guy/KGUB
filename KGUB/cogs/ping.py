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
    async def ping(self,ctx: commands.Context):
        msg_emoji = ":)" 
        emojis = ctx.guild.emojis
        for emoji in emojis:
            if emoji.name == "belucat":
                msg_emoji = emoji
        # gets the latency of the bot in seconds
        ping_time = self.bot.latency * 1000
        # chaneges the text and update to the time duration of command call and its execution
        await ctx.reply(f"Pong! : {round(ping_time)}ms \nApparently, I'm quicker than our server members {msg_emoji}")

# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(bot: commands.Bot):
    # Calls the Ping Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await bot.add_cog(Ping(bot))
