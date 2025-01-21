
import discord
from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv
import os
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID")) # .env imports variables as strings by default

class Client(commands.Bot): #discord.client must be capitalized
  async def on_ready(self): #onready function is a built in discord function that runs when connected to discord
    print(f'Logged on as {self.user}!')

    try:
      guildObject = discord.Object(id=GUILD_ID)
      synced = await self.tree.sync(guild=guildObject)
      print(f'Synced {len(synced)} commands to guild{guildObject.id}')
    except Exception as e:
      print(f'Error syncing commands: {e}')


  async def on_message(self,message):
    if message.author == self.user:
      return
    
    if message.content.startswith('hello'):
      await message.channel.send(f'Hi there {message.author}')

############################################################################

intents = discord.Intents.default() # using default permissions
intents.message_content = True
client = Client(command_prefix="!", intents =intents) # command prefix is the / or command

############################################################################

@client.tree.command(name="hello", description="Say hello!", guild=discord.Object(id = GUILD_ID)) # guild is for the specific server id youre testing in
async def sayHello(interaction:discord.Interaction):
  await interaction.response.send_message("Hi there! ")

@client.tree.command(name="printer", description="I will copy you!", guild=discord.Object(id = GUILD_ID)) # guild is for the specific server id youre testing in
async def printer(interaction:discord.Interaction, printer: str):
  await interaction.response.send_message(printer)

client.run(DISCORD_BOT_TOKEN)
