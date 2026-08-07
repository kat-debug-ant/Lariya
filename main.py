import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
        command_prefix="!",
            intents=intents
)
print("Bot se spouští...")

@bot.event
async def on_ready():
    print(f"Antirōs bot je přihlášen jako {bot.user}")


    @bot.command()
    async def hello(ctx):
        await ctx.send("Vítej v Antirōsu.")


        if not TOKEN:
            raise RuntimeError("Chybí DISCORD_TOKEN.")

            print("Připojují se na Discord...")bot.run(TOKEN)
