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


@bot.event
async def on_ready():
    print(f"Antirōs bot je přihlášen jako {bot.user}")


@bot.command()
async def hello(ctx):
        await ctx.send(f"🌙 Vítej v Antirōsu,{ctx.author.mention}!\n\n"
                      "Než se vydáš dál,projdi si tyhle důležité části severu:\n\n"
                      "📜 <#ID_rules>\n"
                      "📖 <#ID_informations>\n"
                      "🧭 <#ID_quiz>\n"
                      "Až budeš připraven/a, začni v <#ID_quiz>."
                      )

if not TOKEN:
    raise RuntimeError("Chybí DISCORD_TOKEN.")


bot.run(TOKEN)
