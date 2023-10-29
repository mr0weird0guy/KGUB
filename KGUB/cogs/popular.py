from datetime import datetime, timedelta
from collections import defaultdict
from discord import Embed
import re
import discord
from discord.ext import commands


class Popular(commands.Cog):
    # initialization of the Ping class
    def __init__(self, bot):
        self.bot = bot

    # the following decorator is necessary for bot to understand the later is a bot command
    @commands.command()
    # parameters:
    # 1st as bot,
    # 2nd as the context
    async def popular(self: commands.bot, ctx: commands.Context, *dates):
        # takes the current datetime
        now = datetime.utcnow()
        # pattern to match for date
        pattern = re.compile(r"\d{2}-\d{2}")
        # no time is mentioned the consider last 7 days
        end = now
        start = now - timedelta(days=7)
        if dates:
            if dates.__len__() != 2:
                # if arguments are more or less than 2 then kills the function
                await ctx.reply(
                    f"I need exactly 2 dates before I start going out with you {ctx.author.mention}"
                )
                return
            # if dates are provided by the user then iterate over them
            for date in dates:
                if re.fullmatch(pattern, date) != None:
                    # if the dates are not in the right format then cancel the function call
                    await ctx.reply(
                        "Get this straight {ctx.author.mention},\nDate format should be 'DD-MM'"
                    )
                    return
            # if the dates are in right format and right count
            start, end = dates[:2]

        # loading text
        reply = await ctx.reply(f"Don't rush me!\nFinding the best takes time")

        # creating dictionary of dictionaries for each message like a json object
        image_reaction_counts = defaultdict(lambda: defaultdict(int))

        async for message in ctx.channel.history(after=start, before=end):
            # reads all the text within the mentioned dates and check if any file is attached or not
            if message.attachments:
                for reaction in message.reactions:
                    # counts total reaction of attachments
                    image_reaction_counts[message.id][reaction.emoji] += reaction.count

        # sort the count in descending order
        sorted_image_counts = {
            k: dict(sorted(v.items(), key=lambda x: x[1], reverse=True))
            for k, v in image_reaction_counts.items()
        }
        # loading text
        await reply.edit(content="Don't rush me!\nFinding the best takes time.")

        # takes only the top 10 in count
        top_10 = sorted(
            sorted_image_counts.items(), key=lambda x: sum(x[1].values()), reverse=True
        )[:10]

        response = ""
        # generate response with index, messageId and count of reactions
        for i, (message_id, counts) in enumerate(top_10):
            # takes all the messages with attachment
            message = await ctx.fetch_message(message_id)
            score = ""
            for k, v in image_reaction_counts[message.id].items():
                emoji = f"{(f'<a:{k.name}:{k.id}>' if k.animated else f'<:{k.name}:{k.id}>') if isinstance(k, discord.Emoji) else k}"
                # counts each type of reaction and creates score
                score += f"{emoji}: {v} "

            response += "{}. {}\n\tMeme: {}\n\tScore: {}\n\t\t{}\n".format(
                i + 1,
                message.author.mention,
                message.jump_url,
                sum(counts.values()),
                score,
            )
        
        # loading text
        await reply.edit(content="Don't rush me!\nFinding the best takes time..")
        
        # formatted response in the form of embed
        embed = Embed(
            title="Top {} posts from {} to {}:".format(
                top_10.__len__(), start.strftime("%d-%m-23"), end.strftime("%d-%m-23")
            ),
            description=response,
            color=0x3498DB,
        )

        # loading text
        await reply.edit(content="Don't rush me!\nFinding the best takes time...")
        # final response
        await reply.edit(content="Here we go!", embed=embed)


# this function runs as the command is executed
# bot should be of type commands.Bot
async def setup(bot: commands.Bot):
    # Calls the Popular Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this function to do the work
    await bot.add_cog(Popular(bot))
