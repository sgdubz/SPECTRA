import os
import discord

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"TEST BOT CONNECTED: {bot.user}")

bot.run(os.environ["DISCORD_TOKEN"])
