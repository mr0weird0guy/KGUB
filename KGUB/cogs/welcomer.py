from discord.ext import commands
from KGUB import *
import discord 

#setup function is necessary for the bot to understand the cog
async def setup(Client: commands.Bot):
    await Client.add_cog(Welcomer(Client))

# Welcomer class 
class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Work in progress this is just a sample code ! do not touch it :)
    @Client.event
    async def on_member_join(member):
        channel = member.guild.system_channel
        await channel.send(f'Welcome {member.mention} to {member.guild.name}!')







