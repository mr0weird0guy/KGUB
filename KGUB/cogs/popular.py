from datetime import datetime, timedelta
from collections import defaultdict
from discord import Embed
from discord.ext import commands


class Popular(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def popular(self: commands.bot, ctx: commands.Context):
        now = datetime.utcnow()

        next_sunday = now + timedelta(days=(6 - now.weekday()))

        prev_sunday = next_sunday - timedelta(days=7)

        image_reaction_counts = defaultdict(lambda: defaultdict(int))

        async for message in ctx.channel.history(after=prev_sunday, before=next_sunday):
            if message.attachments:
                for reaction in message.reactions:
                    image_reaction_counts[message.id][reaction.emoji] += reaction.count

        sorted_image_counts = {
            k: dict(sorted(v.items(), key=lambda x: x[1], reverse=True))
            for k, v in image_reaction_counts.items()
        }

        top_10 = sorted(
            sorted_image_counts.items(), key=lambda x: sum(x[1].values()), reverse=True
        )[:10]

        response = ""

        for i, (message_id, counts) in enumerate(top_10):
            message = await ctx.fetch_message(message_id)
            response += "{}. Sender: {} {}: {}\n".format(
                i + 1, message.author.mention, message.jump_url, sum(counts.values())
            )

        embed = Embed(
            title="Top 10 posts from {} to {}:".format(
                prev_sunday.strftime("%d-%m-%Y"), next_sunday.strftime("%d-%m-%Y")
            ),
            description=response,
            color=0x3498DB,
        )

        await ctx.send(embed=embed)


# this function runs as the command is executed
# bot should be of type commands.Bot
async def setup(bot: commands.Bot):
    # Calls the Popular Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this function to do the work
    await bot.add_cog(Popular(bot))
