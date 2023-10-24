from datetime import datetime, timedelta
from collections import defaultdict
from discord import Embed
import re
from discord.ext import commands


class Popular(commands.Cog):
    # innitialization of the Ping class
    def __init__(self, bot):
        self.bot = bot

# the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # parameters:
    # 1st as bot,
    # 2nd as the context
    async def popular(self: commands.bot, ctx: commands.Context, str : None):
        # takes the current datetime
        now = datetime.utcnow()
        # pattern to match for date
        pattern = re.compile(r"/d/d-/d/d")
        if str==None :
            # no time is mentioned the consider last 7 days
            end = now
            start = now - timedelta(days=7)
        else :
            args = str.split()
            # if contains more args then store the dates if they are in the right format
            start = args[0] if pattern.search(args[0]) else None
            end = args[1] if pattern.search(args[1]) else None
            if start == None or end == None :
            # if the args are not in the right format then retuns error text
                ctx.send("Command error")
                return

        # next_sunday = now + timedelta(days=(6 - now.weekday()))

        # prev_sunday = next_sunday - timedelta(days=7)

        image_reaction_counts = defaultdict(lambda: defaultdict(int))

        async for message in ctx.channel.history(after=start, before=end):
            # reads all the text within the mentioned dates
            if message.attachments:
                for reaction in message.reactions:
                    # counts the reaction of those texts
                    image_reaction_counts[message.id][reaction.emoji] += reaction.count
                    # TODO: each emoji ka count + total count

# sort the count in descending order
        sorted_image_counts = {
            k: dict(sorted(v.items(), key=lambda x: x[1], reverse=True))
            for k, v in image_reaction_counts.items()
        }

# takes only the top 10 in count
        top_10 = sorted(
            sorted_image_counts.items(), key=lambda x: sum(x[1].values()), reverse=True
        )[:10]

        response = ""

        for i, (message_id, counts) in enumerate(top_10):
            message = await ctx.fetch_message(message_id)
            response += "{}. {}:\n\t{}- {}\n".format(
                i + 1, message.author.mention, message.jump_url, sum(counts.values())
            )

        embed = Embed(
            title="Top {} posts from {} to {}:".format(
                top_10.__len__(), start.strftime("%d-%m-23"), end.strftime("%d-%m-23")
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
