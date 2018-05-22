#! /usr/bin/env python3
'''
Erste versuche einen eigenen Discordbot zu Schreiben.
'''
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('user-ID: ' + client.user.id)
    print('----------------------------------')
    await client.change_presence(game=discord.Game(name='Pokémon Go'))

@client.event
async def on_message(message):
    if message.content.startswith('.instinct'):
        role_instinct = discord.utils.find(lambda r: r.name == "Instinct", discord.Server.roles)
        await client.add_roles(user, role_instinct)
        await client.send_message(message.channel, 'Hellor?')

client.run('TOKEN')
