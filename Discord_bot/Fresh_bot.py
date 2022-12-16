import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Oni Chan!')
    
@client.event
async def on_message(message):
    if message.content.startswith('!animelist'):
        await message.channel.send('pending')
        
client.run(os.getenv('DISCORD_TOKEN'))