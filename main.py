import discord
from discord.ext import commands

# Intents (required for bots in 2025)
intents = discord.Intents.default()
intents.messages = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    """Responds with a greeting."""
    await ctx.send(f"Hello, {ctx.author.mention}! How can I help you today?")

# Run the bot
bot.run("YOUR_BOT_TOKEN")
