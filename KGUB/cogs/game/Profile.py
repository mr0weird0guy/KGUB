import discord
from discord.ext import commands

class Profile(commands.Cogs):
    # innitialization of the Attendance class
    def __init__(self, bot):
        self.bot = bot

    # the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # parameters:
    # 1st as bot,
    # 2nd as the context, and
    # Everything after them as String
    async def generalprofile(self: commands.Bot, ctx: commands.Context, args: str = None):
        await ctx.send("User Profile")

# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the Attendance Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await Client.add_cog(Profile(Client))
