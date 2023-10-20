import logging
import discord, os, sys
from dotenv import load_dotenv
from discord.ext import commands

# Loading .env file
load_dotenv(os.path.join(".", ".env"))

FORMAT = "[KGUB] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("ptbcontrib.postgres_persistence.postgrespersistence").setLevel(
    logging.WARNING
)

LOGGER = logging.getLogger("[KGUB]")
LOGGER.info("KGUB is starting. | Built by KJ GDSC.")


try:
    TOKEN = os.environ["TOKEN"]
except KeyError:
    print("Please define the environment variable TOKEN")
    sys.exit(1)

"""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
"""
disIntents = discord.Intents.default()
disIntents.message_content = True
Client = commands.Bot(intents=disIntents, command_prefix="?", help_command=None)
