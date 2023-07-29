import os
import discord

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

# Pour lancer le bot
client.run('MTEzNDgwMTQ2NjMxODY1OTYzNA.GTAHuy.KDeaYdOaM2NN4YUWlmJTGAqjO44JL_ox4kHdEY')
