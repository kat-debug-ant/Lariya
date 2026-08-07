import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
print("Token nalezen:", TOKEN is not None)

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

        print("Připojují se na Discord...")
            
        if not TOKEN:
            raise RuntimeError("Chybí DISCORD_TOKEN.")

            print("Spouštím bot.run...")
            bot.run(TOKEN)
