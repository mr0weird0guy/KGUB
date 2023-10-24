import random
from discord.ext import commands
from KGUB import Client

class Fun(commands.Cog):
    # init of the Fun class
    message_history = []
    def __init__(self, bot):
        self.bot = bot

    # decorator for bot to understand this is a command

    @commands.command(aliases=["roll","rolldice","dr"])
    async def diceroll(self, ctx: commands.Context):
        # gets a random number between 1 and 6
        result = random.randint(1, 6)
        await ctx.reply("You rolled a {}".format(result))
    
    # coin flip command
    @commands.command(aliases=["coinflip","hrt","toss"])
    async def flip(self, ctx: commands.Context):
        result = random.randint(1, 2)
        if result == 1:
            await ctx.reply("Heads")
        else:
            await ctx.reply("Tails")

    # sends a random emoji from the server
    @commands.command()
    async def emoji(self, ctx: commands.Context):
        emoji = random.choice(ctx.guild.emojis)
        await ctx.reply(emoji)

    # triggers when any message contains the word kgub
    @Client.event
    async def on_message(message):
        # historylimit of the bot messageses 
        historyLength = 5 
        # deletes the old message ie index 0 if the history goes beyond the limit
        if len(Fun.message_history) > historyLength:
            Fun.message_history.pop(0)
        # gets the last message
        if len(Fun.message_history) > 1:
            lastMessage = Fun.message_history[len(Fun.message_history) - 1]
        # funny replies for the word kgub
        replies = [
        "Ah, the legendary 'kgub' has been spoken!",
        "Did someone say 'kgub'? That's the secret code!",
        "kgub? Sounds like a secret society initiation!",
        "Well, well, well, look who's summoning the 'kgub' spirit!",
        "kgub, the magic word for summoning all the fun!",
        "kgub-ulous! The word of the day!",
        "A wild 'kgub' has appeared!",
        "Say 'ok-gub', and a funny reply shall appear!",
        "kgub-tastic! We're in for a good time!",
        "Ah, the sweet sound of 'kgub' in the air!",
        "kgub? Did someone say 'kgub'?",
        ]
        # if the message is from the bot, it is added to the history
        if message.author == Client.user:
            Fun.message_history.append(message.content)
        else:
            if "kgub" in message.content.lower():
                reply = random.choice(replies)
                await message.channel.send(reply)
    
            if "ok-gub" in message.content.lower():
                if lastMessage == "Say 'ok-gub', and a funny reply shall appear!" :
                    await message.channel.send("Obey your GDSC lead and Team Leads!, not me '*facepalm*'")
                else:
                    if "ok-gub" in message.content.lower():
                        await message.channel.send("Did i tell you to say that?")








# --------------------------------------------------------
# this funtion runs as the command is executed
# Client should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the Fun Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await Client.add_cog(Fun(Client))
