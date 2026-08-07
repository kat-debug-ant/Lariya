import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
        command_prefix="!",
            intents=intents
)


@bot.event
async def on_ready():
    print(f"Antirōs bot je přihlášen jako {bot.user}")
        
@bot.event
async def one_member_join():
        channel = bot.get_channel(1533279934435561634/1534186393067196476)
  
if channel:
await channel.send(
            f"🌙 Vítej v Antirōsu, {member.mention}!\n\n"
            "Nový poutník dorazil do našeho světa.\n\n"
            "Než se vydáš dál, navštiv tato místa:\n\n"
            "📜 Pravidla → <#1534189201774350336>\n"
            "🎭 Role → <#1534623271721504858>\n"
            "🧭 Kvíz → <#1535375026642100286>\n"
            "📢 Oznámení → <#1534189282854437025>\n"
            "📖 O Antirōsu → <#1534189402132189304>\n\n"
            "✨ Tvá cesta začíná právě teď."
        )

@bot.command()
async def start(ctx):
    await ctx.send(
        f"🌙 Vítej v Antirōsu, {ctx.author.mention}!\n\n"
        "Před tebou se otevírá nový svět plný příběhů, tajemství a objevů.\n\n"
        "Než se vydáš dál, doporučuji navštívit tato místa:\n\n"
        "📜 Pravidla → <#1534189201774350336>\n"
        "🎭 Role → <#1534623271721504858>\n"
        "🧭 Kvíz → <#1535375026642100286>\n"
        "📢 Oznámení → <#1534189282854437025>\n"
        "📖 O Antirōsu → <#1534189402132189304>\n\n"
        "✨ Až budeš připravený, začni svou cestu."
    )

if not TOKEN:
    raise RuntimeError("Chybí DISCORD_TOKEN.")


bot.run(TOKEN)
