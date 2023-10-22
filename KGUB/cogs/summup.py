from discord.ext import commands
from discord import Embed
import spacy


class TextSummarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Load the spaCy model
        self.nlp = spacy.load("en_core_web_sm")

    @commands.command()
    async def summarize(self: commands.Bot, ctx: commands.Context, *, text: str = None):
        # Check if the command was triggered by a reply
        if not text and ctx.message.reference:
            replied_message = await ctx.fetch_message(ctx.message.reference.message_id)
            text = replied_message.content

        # Summarize the input text
        if not text:
            return await ctx.send("Please provide some text to summarize.")

        summary = self.summarize_text(text)

        # Create an embed to display the summary
        embed = Embed(title="Text Summary", description=summary, color=0x3498DB)

        await ctx.send(embed=embed)

    def summarize_text(self, text):
        doc = self.nlp(text)
        sentences = list(doc.sents)
        sentence_scores = {}

        for sentence in sentences:
            for word in sentence:
                if word.is_alpha:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = 1
                    else:
                        sentence_scores[sentence] += 1

        summary_sentences = sorted(
            sentence_scores, key=sentence_scores.get, reverse=True
        )[:5]
        summary = " ".join(str(sentence) for sentence in summary_sentences)
        return summary


async def setup(bot: commands.Bot):
    await bot.add_cog(TextSummarizer(bot))
