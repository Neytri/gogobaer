#! /usr/bin/env python3
'''
Erste versuche einen eigenen Discordbot zu Schreiben.
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

@client.event
async def on_message(message):
    if message.content.lower().startswith('.instinct'):
        role_instinct = discord.utils.get(message.server.roles, name="Instinct")
        await client.add_roles(message.author, role_instinct)
        await client.send_message(message.channel, 'funzt?')


    if message.content.lower().startswith('.mystic'):
        for role in message.author.roles:
            if role.name == "Mystic":
                await client.send_message(message.channel, "Du bist bereits im Team Mystic")
#            if role.name == 'Instinct' or 'Valor':
#                await client.send_message(message.channel, "Du kannst nicht in diese rolle, da du schon einer gegnerischen rolle Angehörst")



    if message.content.lower().startswith('.res'):
        embed = discord.Embed(
            color=config.COL_RESEARCH,
            description="**Auftrag:** Drehe 6 PokéStops, die du noch nicht besucht hast.\n"
                        "**Belohnung:** Pokémon (Aerodactyl)\n"
                        "**Pokéstop:** Stolperstein P. Poppelauer\n"
                        "**Ort:** Jessnerstraße 1 (Friedrichshain)\n"
                        "**Maps:** https://goo.gl/maps/TB3qUu4PudP2\n"
        )
        embed.set_author(
            name="Feldforschung",
            icon_url="http://files.pokefans.net/images/pokemon-go/findenicons/forschung.png",   # Feldforschung (Kiste)
            url="https://pokefans.net/spiele/pokemon-go/liste-aller-feldforschungen"
        )
        embed.set_thumbnail(
            #url="https://files.pokefans.net/images/pokemon-go/items/sternenstaub.png"   # Sternenstaub
            #url="https://files.pokefans.net/images/pokemon-go/items/sonderbonbon.png"   # Sonderbonbon
            url="https://files.pokefans.net/images/pokemon-go/modelle/142.png"          # Aerodactyl
            #url="https://files.pokefans.net/images/pokemon-go/modelle/082.png"          # Magneton
            #url="https://files.pokefans.net/images/pokemon-go/modelle/113.png"          # Chaneira
            #url="https://files.pokefans.net/images/pokemon-go/modelle/114.png"          # Tangela
            #url="https://files.pokefans.net/images/pokemon-go/modelle/129.png"          # Karpador
            #url="https://files.pokefans.net/images/pokemon-go/modelle/246.png"          # Larvitar
        )
        await client.delete_message(message)
        await client.send_message(message.channel, embed=embed)

client.run(config.TOKEN_DISCORD_BOT)
