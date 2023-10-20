import time
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self: commands.Bot, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Pinging...")
        end_time = time.time()
        ping_time = round((end_time - start_time) * 1000, 3)

        await message.edit(content="PONG: {}ms".format(ping_time))


async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
