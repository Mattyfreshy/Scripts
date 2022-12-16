import discord
import os
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message):
        if message.content.startswith('!test'):
            await message.channel.send('pending')
            
    client.run(os.getenv('DISCORD_TOKEN'))
    
    
def main():
    run_discord_bot()
    
if __name__ == '__main__':
    main()