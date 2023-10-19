import discord, env


disIntents = discord.Intents.default()
disIntents.message_content = True
Client = discord.Client(intents=disIntents)

# when bot is ready (Bot start)
@Client.event 
async def on_ready():
  print("Bot is Ready and Online")

#jab user apna msg type karega wo message me jayega and waha se reply ...
@Client.event
async def on_message(message):
  if message.author == Client.user:
    return

  if message.content == "hi":
    await message.channel.send("hello world!")

Client.run(env.TOKEN)
