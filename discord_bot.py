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

client.run('MTEzNDgwMTQ2NjMxODY1OTYzNA.G0SRp4.-x3F0lhsGS2Sc7PqZYegOU7FPo6PQ0bCFcDfHQ')
