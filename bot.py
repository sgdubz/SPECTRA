
import discord
from discord.ext import commands

# SPECTRA configuration
TOKEN = "YOUR_BOT_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"SPECTRA is online as {bot.user}")
    await bot.change_presence(
        activity=discord.Game(name="Watching the Protocol...")
    )

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

bot.run(TOKEN)
