# KGUB 

## Introduction

This is a simple Discord bot written in Python using the discord.py library. The bot responds to specific commands and performs certain actions.

## Requirements

- Python 3.11.4 or higher
- discord.py library
```bash
pip install -r requirements.txt
```

## Installation

- Install Python from the official website.
- Install discord.py using pip:


```python
pip3 install -r requirements.txt
py -m KGUB
```

## Usage

- Import the discord library in your Python script:
```python
import discord
from discord.ext import commands
```
- Create an instance of the `Bot` class:
```python
bot = commands.Bot(command_prefix='!')
```
- Define a command using the `@bot.command()` decorator:
```python
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, World!')
```
- Run the bot using your token:
```python
bot.run('your-token-here')
```
## Sample COG file exp

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

## Commands

- `!hello`: The bot responds with "Hello, World!"
- new features commands arriving soon -->


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)



