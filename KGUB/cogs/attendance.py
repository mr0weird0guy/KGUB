import csv
import os
import openpyxl
import discord
from discord.ext import commands


class Attendance(commands.Cog):
    # innitialization of the Attendance class
    def __init__(self, bot):
        self.bot = bot

# the following decorator is necessary for bot to understand the latar is a bot command
    @commands.command()
    # parameters:
    # 1st as bot,
    # 2nd as the context, and
    # Everything after them as String
    async def attendance(self: commands.Bot, ctx: commands.Context, args: str = None):
        try:
            # access the channel the author of the text is currently in
            channel = ctx.message.author.voice.channel
        except AttributeError:
            # controlles the error of user not being in any channel
            return await ctx.send("User is not in a voice channel, can't take attendance.")

        # Processing text
        await ctx.send("Attendance is being taken, please wait...")

        # List all the members of that voice channel
        members = channel.members

        # Creates and open a CSV with the the dynamic name ChannelID_memebers
        with open(
            f"{channel.id}_members.csv", mode="w", newline="", encoding="utf-8"
        ) as file:
            # Innitialize the writing
            writer = csv.writer(file)
            # common header row for all the files
            writer.writerow(["ID", "Global Name", "Username", "Nickname"])
            for member in members:
                # Addition of the detials of every member present in that channel at the runtime of the command
                writer.writerow([member.id, member.global_name, member.name, member.nick])

        # takes everything from the 3rd parameter and checks it's value
        if args and args.strip().lower() == "excel":
            # Opens and activate the workbook
            wb = openpyxl.Workbook()
            ws = wb.active

            # abbrivate the file details to attendance_file using with keyword
            with open(f"{channel.id}_members.csv", "r", encoding="utf-8") as attendance_file:
                for row in csv.reader(attendance_file):
                    # adds all the rows to the workbook
                    ws.append(row)

            # saves and sends the workbook to the server channel and removes from os the bot's storage
            wb.save(f"{channel.id}_members.xlsx")
            await ctx.send(file=discord.File(f"{channel.id}_members.xlsx"))
            os.remove(f"{channel.id}_members.xlsx")

        else:
            await ctx.send(file=discord.File(f"{channel.id}_members.csv"))
            # else sends the csv file to the server channel and removes from os the bot's storage
            await os.remove(f"{channel.id}_members.csv")

# ============================Old Code Ignore====================================
    #         await self.remove_file(f"{channel.id}_members.csv")

    # async def remove_file(self, file_path: str):
    #     try:
    #         os.remove(file_path)
    #     except Exception as e:
    #         print(f"Error removing file: {e}")
# =================Use only if error in line 65===================================

# this funtion runs as the command is executed
# bot should be of type commands.Bot
async def setup(Client: commands.Bot):
    # Calls the Attendance Object with the parameter as Client which is the command component.
    # The Object is added to the cog(short form for component)
    # Client is the bot which uses this funtion to do the work
    await bot.add_cog(Attendance(Client))
