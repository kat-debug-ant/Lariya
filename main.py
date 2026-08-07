import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(
        command_prefix="!",
            intents=intents
)


@bot.event
async def on_ready():
    print(f"Antirōs bot je přihlášen jako {bot.user}")


@bot.command()
async def hello(ctx):
        print("Přišel příkaz hello")
        await ctx.send("Vítej v Antirōsu.")

            
if not TOKEN:
    raise RuntimeError("Chybí DISCORD_TOKEN.")


bot.run(TOKEN)
