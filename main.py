import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if 'you' in message.content:
    await message.channel.send('hello boomer')
  

client.run(os.getenv('TOKEN'))
