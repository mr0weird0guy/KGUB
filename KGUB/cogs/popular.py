import discord
from discord.ext import commands


class Popular(commands.Cog):
    # innitialization of the Attendance class
    def __init__(self,bot):
        self.bot = bot

    # the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    def popular(self: commands.bot, ctx: commands.Context, text: str = None):
        # takes the starting message id
        # takes the last message id
        # and all the messages id in between
        # if it is an file(audio, video, image) then count the reactions
        # return a list of text and rank top 3 with message links
        


# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the Popular Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await bot.add_cog(Popular(Client))