# KGUB

![GDSC Kristu Jayanti College](https://github.com/KJC-GDSC/KGUB/assets/85097731/5592c432-e39a-4a03-8b0b-6c8d4d4888cc)

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
python -m KGUB
```

If you face an error mentioning "this system does not have Windows Long Path support enabled."
run the following command in powershell

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

## Bot Command

```python
bot = commands.Bot(command_prefix='kgub')
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

`kgub alive` - check if the bot is active<br>
`kgub attendance` - gives attendance for active participants in a channel<br>
`kgub ping` - checks the ping status<br>
`kgub summup` - summerizes a message<br>
`kgub popular` - counts and return the number of reactions on top (10 - max) messages<br>

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Collaborators

![Collaborators](https://contrib.rocks/image?repo=KJC-GDSC/KGUB)

## License

[MIT](https://choosealicense.com/licenses/mit/)
