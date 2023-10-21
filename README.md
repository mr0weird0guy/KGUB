# KGUB - Discord bot by KJ GDSC

![GDSC](https://logogen.gdscasu.com/logos/gdsc-logo.png)

Sample .env file

```
TOKEN="TOKEN"
```

Running the Bot

```python
pip3 install -r requirements.txt
py -m KGUB
```

Sample cog file example

```python
from discord.ext import commands


class Alive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def alive(self, ctx: commands.Context):
        await ctx.send("Hey {0.author.mention}! How are you?".format(ctx.message))


async def setup(Client: commands.Bot):
    await Client.add_cog(Alive(Client))

```
