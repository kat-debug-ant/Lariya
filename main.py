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
async def on_member_join(member):
    channel = bot.get_channel(1534186393067196476)

    if channel:
        embed = discord.Embed(
            title="🌙 Vítej v Antirōsu",
            description=(
                f"Vítej, {member.mention}!\n\n"
                "Dorazil jsi do světa plného tajemství, příběhů a objevů.\n\n"
                "✨ Než se vydáš dál, doporučujeme navštívit:"
            ),
            color=0x8A2BE2
        )

        embed.add_field(
            name="📜 Pravidla",
            value="<#1534189201774350336>",
            inline=True
        )

        embed.add_field(
            name="🎭 Role",
            value="<#1534623271721504858>",
            inline=True
        )

        embed.add_field(
            name="🧭 Kvíz biomu",
            value="<#1535375026642100286>",
            inline=True
        )

        embed.add_field(
            name="📢 Oznámení",
            value="<#1534189282854437025>",
            inline=True
        )

        embed.add_field(
            name="📖 O Antirōsu",
            value="<#1534189402132189304>",
            inline=True
        )

        embed.set_footer(
            text="Antirōs • Tvá cesta právě začíná"
        )

        await channel.send(embed=embed)

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

if not TOKEN:
    raise RuntimeError("Chybí DISCORD_TOKEN.")


bot.run(TOKEN)
