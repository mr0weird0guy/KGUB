from discord.ext import commands
from discord import Embed
from gensim.summarization import summarize

class TextSummarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def summarize(self, ctx, *, text):
        # Summarize the input text
        summary = summarize(text, ratio=0.2)  # You can adjust the ratio for the summary length

        # Create an embed to display the summary
        embed = Embed(title="Text Summary", description=summary, color=0x3498db)

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(TextSummarizer(bot))
