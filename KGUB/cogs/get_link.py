from discord.ext import commands

# Ignore this file


class GetLink(commands.Cog):
    # innitialization of the GetLink class
    def __init__(self, bot):
        self.bot = bot

# the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # parameter ctx as context
    async def link(self, ctx: commands.Context):
        if len(ctx.message.attachments) == 0:
            # image is not added with the command
            await ctx.send("Please attach an image to the message.")
            return
        # stores the url of the image provided with the command
        file_url = ctx.message.attachments[0].url

        # sends the url to the channel
        await ctx.send(file_url)


# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the GetLink Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await Client.add_cog(GetLink(Client))
