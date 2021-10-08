import discord
import os
from dotenv import load_dotenv
from datetime import datetime
import time

client = discord.Client()

load_dotenv()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f"Loggato come {client.user}".format(client))

@client.event
async def on_connect():
    print('È entrato un buffone')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'mamo help':
        await message.channel.send('Ciao sono Mamo, un bot creato da un fallito e non faccio praticamente un cazzo'
        '\n\nI miei comandi sono(per ora):\nmamo help\nmamo ora'
        '\nmamo ricorda tra')

    if message.content == 'mamo ora':
        ora = datetime.now()
        ora_formattata = ora.strftime("%H:%M:%S")
        await message.channel.send(f'Ora: {ora_formattata}')

    if message.content.startswith('mamo ricorda tra'):
        if len(message.content.split('mamo ricorda tra ')) == 2:
            msg = message.content.split(' ')[5:]
            tempo = int(message.content.split(' ')[3])
            unita = str(message.content.split(' ')[4])
            if unita == 'secondi' or unita == 'secondo':
                await message.channel.send(f'OK {message.author.mention} te lo ricorderò')
                time.sleep(tempo) 
                await message.channel.send(f'{message.author.mention}' + ' '.join(msg))
            elif unita == 'minuti' or unita == 'minuto':
                await message.channel.send(f'OK {message.author.mention} te lo ricorderò')
                time.sleep(tempo * 60)
                await message.channel.send(f'{message.author.mention}' + ' '.join(msg))
            elif unita == 'ora' or unita == 'ore':
                await message.channel.send(f'OK {message.author.mention} te lo ricorderò')
                time.sleep(tempo * 3600)
                await message.channel.send(f'{message.author.mention}' + ' '.join(msg))
            else:
                await message.channel.send('USO: mamo ricorda tra X secondi/minuti/ora ...')
                
client.run(token)