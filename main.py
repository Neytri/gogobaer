#! /usr/bin/env python3
"""
# install discord.py/rewrite
$ git clone https://github.com/Rapptz/discord.py.git -b rewrite

# check with
$ cd discord.py
$ git branche

# install
$ python3 -m pip install -U discord.py
"""
import discord
from discord.ext import commands
import time
import config

description = None
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as: ' + bot.user.name)
    print('user-ID: ' + bot.user.id)
    print('---------------------------')
    await bot.change_presence(game=discord.Game(name='Pokémon Go'))


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
@bot.command(pass_context=True)
async def test(ctx):
    embed = discord.Embed(title="Test", description="... wohl bestanden")
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)
'''
Feldforschung: Usern ermöglicen über den bot quests in dem dafür vorgesehenen
channel zu posten/bearbeiten. tägleich 0:00 soll der channel bis auf die
angepinnten nachrichten gelehrt werden.
'''
@bot.command(pass_context=True)
async def research(ctx):
    print("research send embed.")
    embed = discord.Embed(
        #title = "Titel",
        colour = discord.Colour.dark_orange(),
        description = "**Auftrag:** Brüte 5 Eier aus.\n"
                    "**Belohnung:** Pokémon _(Chaneira)_\n"
                    "**Pokéstop:** Kapelle-Ufer-Ecke Unterbaumstrasse\n"
                    "**Ort:** Reinhardtstraße 58 (Mitte)\n"
                    "**Maps:** https://goo.gl/maps/TymcjjRwEJ62"
    )
    embed.set_thumbnail(url="https://files.pokefans.net/images/pokemon-go/modelle/113.png")
    embed.set_author(
        name="Feldforschung",
        url="https://pokefans.net/spiele/pokemon-go/liste-aller-feldforschungen",
        icon_url="http://files.pokefans.net/images/pokemon-go/findenicons/forschung.png"
    )
    #embed.set_image(url="http://files.pokefans.net/images/pokemon-go/findenicons/forschung.png")
    #embed.set_footer(text="das ist der Footer")
    #await bot.delete_message(message)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)

@bot.command()
async def ping():
    t1 = time.perf_counter()
    msg = await bot.say(":zap: **calculating**")
    t2 = time.perf_counter()
    speed = t2 - t1
    await bot.edit_message(msg, f":zap: **{round(speed * 1000)}**ms")

bot.run(config.TOKEN_DISCORD_BOT)
