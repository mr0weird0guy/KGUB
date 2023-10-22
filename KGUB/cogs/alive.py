from discord.ext import commands


class Alive(commands.Cog):
    # innitialization of the Alive class
    def __init__(self, bot):
        self.bot = bot

# the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # ctx should be of type commands.Context
    async def alive(self, ctx: commands.Context):
        # waits for the fuction ot respond with data in right format
        await ctx.send("Hey {0.author.mention}! How are you?".format(ctx.message))


# this funtion runs as the command is executed
# Client should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the Alive Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await Client.add_cog(Alive(Client))
