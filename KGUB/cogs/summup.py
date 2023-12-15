import datetime
import discord
from KGUB import *
from discord.ext import commands
from discord import Embed
from SummerSearch import summerSearch


class TextSummarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.searchsum = summerSearch()
        self.textsum = summerSearch()
        self.convosum = summerSearch()
        self.summary_model_s = "t5-small"
        self.summary_model_l = "facebook/bart-large-cnn"
        self.conversational_model = "kabita-choudhary/finetuned-bart-for-conversation-summary"

    @commands.command()
    async def searchsum(self, ctx: commands.Context, *, search_query: str = None):
        # # Check if the command was triggered by a reply
        # if not text and ctx.message.reference:
        #     replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
        #     text = replied_message.content

        # Summarize the input text
        if not search_query:
            return await ctx.reply("Please provide some query to search.")
        else:
            try:
                message = await ctx.reply("Gathering information...")
                time = datetime.datetime.now()
                raw = self.searchsum.search(search_query=search_query,filter="accuracy",filter_value=2)
                summary = self.searchsum.summarize(raw, self.summary_model_s)
                # Create an embed to display the summary
                embed = Embed(title=search_query, description=summary["summary"],url=summary["reference"], color=discord.Color.random())
                embed.add_field(name="Reference", value=summary["reference"], inline=False)
                embed.add_field(name="Learn More", value=summary["learn_more"], inline=False)
                embed.set_footer(text=f"\nLatency: {(datetime.datetime.now()-time).seconds + 1}s \nSummarized by KGUB")
                await message.edit(content="",embed=embed)
            except Exception as e: 
                await message.edit(content=f"Couldn't find enough information!, Please try again...\nException: {e}")
    

    @commands.command()
    async def textsum(self, ctx: commands.Context, *, text: str = None):
        time = datetime.datetime.now()
        if not text:
            return await ctx.reply("Please provide some text to summarize.")
        else:
            try:
                message = await ctx.reply("Generating summary...")
                summary = self.searchsum.summarize(text, self.summary_model_l)
                # Create an embed to display the summary
                embed = Embed(title="Text Summary", description=summary["summary"], color=discord.Color.random())
                embed.set_footer(text=f"\nLatency: {(datetime.datetime.now()-time).seconds + 1}s \nSummarized by KGUB")
                await message.edit(content="",embed=embed)
            except Exception as e:
                await message.edit(content=f"Could not summarize the text, Please try again...\nException: {e}")


    @commands.command()
    async def convosum(self, ctx: commands.Context, *, text: str = None):
        time = datetime.datetime.now()
        # Check if the command was triggered by a reply
        if not ctx.message.reference:
            return await ctx.reply(
                "Please reply to a message to summarize all messages from replied message till the last message in the channel."
            )
        else:
            try:
                init_message = await ctx.reply("Generating summary...")
                # Get the replied message
                replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
                # Get all the messages after the replied message in the channel
                messages = {}
                async for message in ctx.channel.history(after=replied_message):
                    messages[message.author.name] = message.content
                # Combine all the messages into a single string
                text = '\n'.join([f'{author} : {message}' for author, message in messages.items()])
                LOGGER.info(messages)
                LOGGER.info(text)
                # Summarize the combined text
                summary = self.searchsum.summarize(text, self.conversational_model)
                # Create an embed to display the summary
                embed = Embed(title="Conversation Summary", description=summary["summary"], color=discord.Color.random())
                embed.set_footer(text=f"\nLatency: {(datetime.datetime.now()-time).seconds + 1}s \nSummarized by KGUB")
                await init_message.edit(content="",embed=embed)
            except Exception as e:
                await init_message.edit(content=f"Could not summarize the conversation, Please try again...\nException: {e}")





async def setup(bot: commands.Bot):
    await bot.add_cog(TextSummarizer(bot))



# @commands.command()
#     async def summarize(self: commands.Bot, ctx: commands.Context, *, text: str = None):
#         # Check if the command was triggered by a reply
#         if not text and ctx.message.reference:
#             replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
#             text = replied_message.content

#         # Summarize the input text
#         if not text:
#             return await ctx.send("Please provide some text to summarize.")

#         summary = self.summarize_text(text)

#         # Create an embed to display the summary
#         embed = Embed(title="Text Summary", description=summary, color=0x3498DB)

#         await ctx.send(embed=embed)

#     @commands.command()
#     async def summup(self: commands.Bot, ctx: commands.Context):
#         # Check if the command was triggered by a reply
#         if not ctx.message.reference:
#             return await ctx.send(
#                 "Please reply to a message to summarize all messages from that message till the last message in the channel."
#             )

#         # Get the replied message
#         replied_message = await ctx.fetch_message(ctx.message.reference.message_id)

#         # Get all the messages after the replied message in the channel
#         messages = []
#         async for message in ctx.channel.history(after=replied_message):
#             messages.append(message)

#         # Combine all the messages into a single string
#         text = "\n".join([message.content for message in messages])

#         # Summarize the combined text
#         summary = self.summarize_text(text)

#         # Create an embed to display the summary
#         embed = Embed(title="Text Summary", description=summary, color=0x3498DB)

#         await ctx.send(embed=embed)

#     def summarize_text(self, text):
#         doc = self.nlp(text)
#         sentences = list(doc.sents)
#         sentence_scores = {}

#         for sentence in sentences:
#             for word in sentence:
#                 if word.is_alpha:
#                     if sentence not in sentence_scores:
#                         sentence_scores[sentence] = 1
#                     else:
#                         sentence_scores[sentence] += 1

#         summary_sentences = sorted(
#             sentence_scores, key=sentence_scores.get, reverse=True
#         )[:5]
#         summary = " ".join(str(sentence) for sentence in summary_sentences)
#         return summary