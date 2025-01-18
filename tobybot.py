
import discord
from dotenv import load_dotenv
import os
load_dotenv()

class Client(discord.Client):
  async def on_ready(self): #onready function is a built in discord function that runs when connected to discord
    print(f'Logged on as {self.user}!')

  async def on_message(self,message):
    print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default() # using default permissions
intents.message_content = True

client = Client (intents=intents)
token = os.environ(DISCORD_BOT_TOKEN)
client.run(token)
