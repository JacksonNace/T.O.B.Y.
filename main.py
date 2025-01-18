import os
import discord
from dotenv import load_dotenv
load_dotenv()

class Client(discord.Client):
  async def on_ready(self): #onready function is a built in discord function that runs when connected to discord
    print(f'Logged on as {self.user}!')

intents = discord.Intents.default() # using default permissions
intents.message_content = True

client = Client (intents=intents)
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not DISCORD_BOT_TOKEN:
    print("Error: DISCORD_BOT_TOKEN is not defined in the .env file.")
else:
    client.run(DISCORD_BOT_TOKEN)
