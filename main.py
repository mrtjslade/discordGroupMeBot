import os
import discord
import aiohttp
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GROUPME_BOT_ID = os.getenv('GROUPME_BOT_ID')
CHANNEL_WEBHOOK_URL = os.getenv('CHANNEL_WEBHOOK_URL')

client = discord.Client(intents=discord.Intents.all())

endpoint = f'https://api.groupme.com/v3/bots/post?bot_id={GROUPME_BOT_ID}'

async def post(message):
    payload = {'text': f'{message.content}'}
    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, json=payload) as response:
            print(await response.json())

@client.event
async def on_message(message):
    if message.webhook_id == CHANNEL_WEBHOOK_URL:
        return await post(message)

@client.event
async def on_ready():
    print('Bot is ready')

client.run(DISCORD_TOKEN)