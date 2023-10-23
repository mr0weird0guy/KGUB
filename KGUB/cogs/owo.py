from discord.ext import commands
import random
from KGUB.database.owo import *


# Need Fixing
class OwO(commands.Cog):
    # innitialization of the Attendance class
    def __init__(self, bot):
        self.bot = bot

# the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # parameters:
    # 1st as context,
    # Everything after it as String
    async def owo(self, ctx: commands.Context, args: str = None):
        user = ctx.message.author
        # stores the author of the command and access the id
        user_id = user.id

        if not is_user(user_id):
            add_user(user_id)

        if args and args.strip().lower() == "balance":
            await ctx.send(f"Your balance is {get_balance(user_id).balance}")
        elif args and args.strip().split(" ")[0].lower() == "flip":
            await ctx.send(
                f"{user.nick} spent :cowoncy: {int(args.strip(' ').split()[1])} and chose heads"
            )

            num = random.randint(0, 1)

            if num == 0:
                await ctx.send(f"The coin spins... :tail: and you lost it all... :c ")
            else:
                await ctx.send(
                    f"The coin spins... :head: and you won {int(args.strip(' ').split()[1]) * 2} :cowoncy: "
                )
                update_balance(user_id, get_balance(user_id).balance * 2)


# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the Attendance Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await Client.add_cog(OwO(Client))
