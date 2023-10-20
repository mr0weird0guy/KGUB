from discord.ext import commands


class Alive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def alive(self, ctx: commands.Context):
        await ctx.send("Hey {0.author.mention}! How are you?".format(ctx.message))


async def setup(Client: commands.Bot):
    await Client.add_cog(Alive(Client))
