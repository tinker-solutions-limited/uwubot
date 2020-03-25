#! /usr/bin/python3

import os

import discord
from dotenv import load_dotenv

import uwulib

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(uwulib.uwu(f'{client.user} has connected to Discord!'))

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(uwulib.uwu(f'{client.user} is connected to the following guild:\n'))
    print(uwulib.uwu(f'{guild.name}(id: {guild.id})'))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(uwulib.uwu(
        f'Hi {member.name}, welcome to the {guild.name} Discord server!'
        ))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send(uwulib.uwu(f'Hello {message.author.mention}!'))
    elif message.content.startswith("!uwu"):
        usr = message.content.split()[1]
        print(f'{usr} vs {client.user}')
        if usr == client.user:
            await message.channel.send(uwulib.uwu("no u!"))


def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()


