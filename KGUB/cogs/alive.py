from discord.ext import commands


# Not working
class Alive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["p"])
    async def alive(self, ctx: commands.Context):
        print("Alive func is working.")
        await ctx.send("Hey {0.author.mention}! How are you?".format(ctx.message))


async def setup(Client: commands.Bot):
    print("Alive Cog is working.")
    await Client.add_cog(Alive(Client))
