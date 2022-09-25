# Discord bot example script found at: https://realpython.com/how-to-make-a-discord-bot-python/
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('discord_token')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)