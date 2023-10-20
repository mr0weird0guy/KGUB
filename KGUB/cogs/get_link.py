from discord.ext import commands


class GetLink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def link(self, ctx: commands.Context):
        if len(ctx.message.attachments) == 0:
            await ctx.send("Please attach an image to the message.")
            return
        file_url = ctx.message.attachments[0].url

        await ctx.send(file_url)


async def setup(Client: commands.Bot):
    await Client.add_cog(GetLink(Client))
