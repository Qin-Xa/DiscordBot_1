import discord
import os

client = discord.Client()

trigger_words = ["you", "getting", "tonight", "hunt", "playing", "zoomer" "yo", "guys", "around"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if any(word in msg for word in trigger_words):
      await message.channel.send('What would you know of struggle, Perfect Son?')

  if 'where' in message.content:
    await message.channel.send('Dont worry about what im doing everytime im doing it.')
  

client.run(os.getenv('TOKEN'))