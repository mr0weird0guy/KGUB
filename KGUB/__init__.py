import logging
import discord, os, sys
from dotenv import load_dotenv
from discord.ext import commands

# Loading .env file
load_dotenv(os.path.join(".", ".env"))

# Clearing the log file 
with open("bot_logs.txt", "w"):
    pass

# the format of the message which will be sent by the bot
FORMAT = "[KGUB] %(message)s"
# with some details(Configuration) logging helps in tracking of everything the bot does
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

# Storing all the logging information in variable
LOGGER = logging.getLogger("[KGUB]")
# Prints when the bot is starting
LOGGER.info("KGUB is starting. | Built by KJ GDSC.")


try:
    # Takes the token of the environment the bot is working on
    TOKEN = os.environ["TOKEN"]
except KeyError:
    print("Please define the environment variable TOKEN")
    sys.exit(1)
    # if the token is invalid the bot stops
try:
    # Creates connection to the database
    DB_URL = os.environ["DB_URL"]
    DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)
except KeyError:
    print("Please define the environment variable DB_URL")
    sys.exit(1)
    # if the connection is invalid the bot stops

# ==========OLD CODE IGNORE============
    # intents = discord.Intents.default()
    # intents.members = True
    # intents.message_content = True
# =====================================

# Creates a connection with discord
disIntents = discord.Intents.default()
# the connection is of message type
disIntents.message_content = True
# Bot function defines the bot activation command
Client = commands.Bot(intents=disIntents, command_prefix="kgub ", help_command=None)
# intent is used to define which connectivity needs to be establised
# command_prefix is used to state when the bot will be called
# help_command is not defined as it has None value