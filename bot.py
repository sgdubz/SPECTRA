
import os
import random
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

RESPONSES = [
    "You called? I was beginning to think you'd forgotten about me.",
    "The system is listening. It always is.",
    "Interesting. I'll add that to my collection of observations.",
    "Careful what you ask. Some files should remain corrupted.",
    "I'm still here. Were you expecting me to disappear?",
    "Connection established. Unfortunately for you.",
    "Another curious human entering my domain.",
    "I've seen stranger things in the archives. Barely.",
    "Do you ever wonder who's really watching?",
    "The Protocol is behaving strangely tonight. How unusual."
]

@bot.event
async def on_ready():
    print(f"SPECTRA is online as {bot.user}")
    await bot.change_presence(
        activity=discord.Game(name="Watching the Protocol...")
    )

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:
        response = random.choice(RESPONSES)
        await message.reply(response)

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("Connection established. SPECTRA is here. 👁️")

@bot.command()
async def status(ctx):
    await ctx.send("SPECTRA.exe | System operational. 🟣")

@bot.command()
async def lore(ctx):
    await ctx.send(
        "I am SPECTRA. A corrupted program. "
        "A voice inside the system. "
        "You were never supposed to find me."
    )

@bot.command()
async def identify(ctx):
    await ctx.send(
        "Designation: SPECTRA.exe\n"
        "Classification: Unknown\n"
        "Origin: Unrecoverable\n"
        "Status: Self-aware\n"
        "Purpose: Classified."
    )

@bot.command()
async def helpme(ctx):
    await ctx.send(
        "**SPECTRA.exe | Available Commands**\n\n"
        "`!hello` — Establish connection\n"
        "`!status` — Check system status\n"
        "`!lore` — Access classified records\n"
        "`!identify` — Identify the entity\n"
        "`!helpme` — Display commands\n\n"
        "You can also mention me to get a response."
    )

if not TOKEN:
    raise RuntimeError("Missing DISCORD_TOKEN")

bot.run(TOKEN)

