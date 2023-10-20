import csv
import os
import openpyxl
import discord
from discord.ext import commands


class Attendance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def attendance(self: commands.Bot, ctx: commands.Context, args: str = None):
        try:
            channel = ctx.message.author.voice.channel
        except AttributeError:
            return await ctx.send(
                "User is not in a voice channel, can't take attendance."
            )

        await ctx.send("Attendance is being taken, please wait...")

        members = channel.members

        with open(f"{channel.id}_members.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Global Name", "Username", "Nickname"])
            for member in members:
                writer.writerow(
                    [member.id, member.global_name, member.name, member.nick]
                )

        if args and args.strip().lower() == "excel":
            wb = openpyxl.Workbook()
            ws = wb.active
            with open(f"{channel.id}_members.csv", "r") as f:
                for row in csv.reader(f):
                    ws.append(row)

            wb.save(f"{channel.id}_members.xlsx")
            await ctx.send(file=discord.File(f"{channel.id}_members.xlsx"))
            os.remove(f"{channel.id}_members.xlsx")
        else:
            await ctx.send(file=discord.File(f"{channel.id}_members.csv"))

        await self.remove_file(f"{channel.id}_members.csv")

    async def remove_file(self, file_path: str):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error removing file: {e}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Attendance(bot))
