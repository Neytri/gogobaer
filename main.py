#! /usr/bin/env python3
'''
Problemstellung: Teamwahl
- Teams: Instinct, Mystic, Valor
- Bedingung: man soll einem Team joinen können, aber nicht mehr als einem
- Infos:  - jedes Team bekommt eine Rolle. neben diesen Rollen gibt es auch
            andere.
          - ein späterer wechsel soll nicht ermöglicht werden (außer
            durch Admins)
          - 
'''
import discord
import asyncio

import config

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('user-ID: ' + client.user.id)
    print('----------------------------------')
    await client.change_presence(game=discord.Game(name='Pokémon Go'))

def check_role_availability(role_name, roles):
    """
        Testet ob role_name als Rolle (role.name) in dem Array roles enthalten ist.

        Returns: True, wenn Rolle vorhanden
        Returns: False, wenn Rolle nicht vorhanden
    """
    for role in roles:
        if role.name == role_name:
            return True

    return False

@client.event
async def on_message(message):
    if message.content.lower() == '.instinct':
        role_instinct = discord.utils.get(message.server.roles, name="Instinct")
        await client.add_roles(message.author, role_instinct)
        await client.send_message(message.channel, 'funzt?')

    if message.content.lower() == '.mystic':
        role_name = "Mystic"
        if check_role_availability(role_name, message.author.roles):
            print("Mystic ist bereits in der Rolle {} ({})".format(role_name, message.author.roles))
            await client.send_message(message.channel, "Du bist bereits im Team Mystic")
        else:
            print("Fuege dich der Rolle {} hinzu.".format(role_name))
            role = discord.utils.get(message.server.roles, name=role_name)
            await client.add_roles(message.author, role)

client.run(config.TOKEN_DISCORD_BOT)
