from discord.ext import commands
from discord import Embed
import spacy

class TextSummarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Load the spaCy model
        self.nlp = spacy.load('en_core_web_sm')

    @commands.command()
    async def summarize(self, ctx, *, text):
        # Summarize the input text
        summary = self.summarize_text(text)

        # Create an embed to display the summary
        embed = Embed(title="Text Summary", description=summary, color=0x3498db)

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

        summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]
        summary = ' '.join(str(sentence) for sentence in summary_sentences)
        return summary

def setup(bot: commands.Bot):
    bot.add_cog(TextSummarizer(bot))
