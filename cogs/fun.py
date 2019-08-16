import discord
from discord.ext import commands
import asyncio
import random
import aiohttp
import dateutil.parser
import dataset
import json
from urllib.parse import quote_plus

botver = "Mewtwo v2.0" #--Bot's version, obviously--#

melo =[ #--List of images for meloetta command--#
    'https://sks316.s-ul.eu/gKaVnpMW',
    'https://sks316.s-ul.eu/XrcEzi0D',
    'https://sks316.s-ul.eu/QhOlFzPo',
    'https://sks316.s-ul.eu/dTZahOws',
    'https://sks316.s-ul.eu/gxOaIYS4',
    'https://sks316.s-ul.eu/Nie0Y5r5',
    'https://sks316.s-ul.eu/axWfYbxq',
    'https://sks316.s-ul.eu/uQBUeHgU',
    'https://sks316.s-ul.eu/kxy3fBZR',
    'https://sks316.s-ul.eu/rR0KGQA6',
    'https://sks316.s-ul.eu/axV5qlIv',
    'https://sks316.s-ul.eu/RHcrxLUq',
    'https://sks316.s-ul.eu/OPJxBIbi',
    'https://sks316.s-ul.eu/BXfeZjyA',
    'https://sks316.s-ul.eu/lvOv7s3l',
    'https://sks316.s-ul.eu/4gHuLUIt',
    'https://sks316.s-ul.eu/gXimbOvb',
    'https://sks316.s-ul.eu/DXemfAIc',
    'https://sks316.s-ul.eu/wRa5aW45',
    'https://sks316.s-ul.eu/vFeRbpN0',
    'https://sks316.s-ul.eu/kUj7aMYn',
    'https://sks316.s-ul.eu/mhSt7XIt',
    'https://sks316.s-ul.eu/oG1C1Fdj',
    'https://sks316.s-ul.eu/l3rSSHA3',
    'https://sks316.s-ul.eu/GR0djZpM',
    'https://sks316.s-ul.eu/d3DsRTkt',
    'https://sks316.s-ul.eu/aFAdkPwl',
    'https://sks316.s-ul.eu/2Lfgxr8u',
    'https://sks316.s-ul.eu/menN6SzZ',
]

sylv =[ #--List of images for sylveon command--#
    'https://sks316.s-ul.eu/lI9yl512',
    'https://sks316.s-ul.eu/Cd3WEZbC',
    'https://sks316.s-ul.eu/3ad6iGd7',
    'https://sks316.s-ul.eu/gfAJkE9h',
    'https://sks316.s-ul.eu/koqtiQkG',
    'https://sks316.s-ul.eu/IEvNaJKG',
    'https://sks316.s-ul.eu/aCRWOb6o',
    'https://sks316.s-ul.eu/HA5kRZ82',
    'https://sks316.s-ul.eu/TtDIYyj3',
    'https://sks316.s-ul.eu/cI5m3G3d',
    'https://sks316.s-ul.eu/QXNRl1Tc',
    'https://sks316.s-ul.eu/RqyWtcwB',
    'https://sks316.s-ul.eu/thxdo9LZ',
    'https://sks316.s-ul.eu/qtE5EnkO',
    'https://sks316.s-ul.eu/chQPM1Up',
    'https://sks316.s-ul.eu/Rfv8y8Mk',
    'https://sks316.s-ul.eu/y0cDN1Ke',
    'https://sks316.s-ul.eu/unwK2yuH',
    'https://sks316.s-ul.eu/s944FXa5',
    'https://sks316.s-ul.eu/P2HPReUq',
    'https://sks316.s-ul.eu/MdflREtZ',
    'https://sks316.s-ul.eu/VAxU1Ec1',
    'https://sks316.s-ul.eu/ZBiFfWKI',
    'https://sks316.s-ul.eu/d6znfTqy',
    'https://sks316.s-ul.eu/VfyASOnw',
    'https://sks316.s-ul.eu/gwITmAHt',
    'https://sks316.s-ul.eu/mYo1KKW3',
    'https://sks316.s-ul.eu/MPbW5CLJ',
]

f_meme =[ #--List of images for F command--#
    'https://sks316.s-ul.eu/4UcpmYzH',
    'https://sks316.s-ul.eu/sRhWN9Jh',
    'https://sks316.s-ul.eu/jIz8Jr9f',
    'https://sks316.s-ul.eu/TP1QOm9m',
    'https://sks316.s-ul.eu/oX6ZAfTP',
    'https://sks316.s-ul.eu/2ALb0Hdr',
    'https://sks316.s-ul.eu/0zUx9W6J',
    'https://sks316.s-ul.eu/zv1apj1v.gif',
    'https://sks316.s-ul.eu/w92uwhgy',
    'https://sks316.s-ul.eu/uegYRi8z',
    'https://sks316.s-ul.eu/eLnNc2yC',
    'https://sks316.s-ul.eu/FhtyhBGl',
    'https://sks316.s-ul.eu/BVDgB6Yh',
    'https://sks316.s-ul.eu/DEQOBojh',
    'https://sks316.s-ul.eu/Hgl2703u.gif',
    'https://sks316.s-ul.eu/6icO2tDG',
    'https://sks316.s-ul.eu/hlno0gnA',
    'https://sks316.s-ul.eu/umOkjS6D',
]

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hey there!")

    @commands.command(aliases=["respects"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def f(self, ctx):
        embed = discord.Embed(title='😔 Today, we pay our respects to those that have left us.', color=0x8253c3)
        embed.set_image(url=random.choice(f_meme))
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def meloetta(self, ctx):
        embed = discord.Embed(title="<:meloetta_aria:598168128345604127> Here you go, a cute Meloetta! :smile:",color=0x9fdf42)
        embed.add_field(name='List of image sources:', value="https://pastebin.com/cRd5vguH")
        embed.set_image(url=random.choice(melo))
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def sylveon(self, ctx):
        embed = discord.Embed(title="<:sylveon:597725070764277786> Here, have some cute Sylveon art :3",color=0xffccfe)
        embed.add_field(name='List of image sources:', value="https://pastebin.com/RwGHXDmS")
        embed.set_image(url=random.choice(sylv))
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command(aliases=["pokemon", "pkmn"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pokedex(self, ctx, *, arg):
        #--Some Pokemon with several forms are named differently on the API, so if one of those Pokemon are specified, we replace the query with the correct name--#
        if arg == 'meloetta':
            pkmn = 'Meloetta - Aria Forme'
        elif arg == 'Meloetta':
            pkmn = 'Meloetta - Aria Forme'
        elif arg == 'keldeo':
            pkmn = 'Keldeo - Ordinary Form'
        elif arg == 'Keldeo':
            pkmn = 'Keldeo - Ordinary Form'
        elif arg == 'burmy':
            pkmn = 'Burmy - Plant Cloak'
        elif arg == 'Burmy':
            pkmn = 'Burmy - Plant Cloak'
        elif arg == 'wormadam':
            pkmn = 'Wormadam - Plant Cloak'
        elif arg == 'Wormadam':
            pkmn = 'Wormadam - Plant Cloak'
        elif arg == 'cherrim':
            pkmn = 'Cherrim - Overcast Form'
        elif arg == 'Cherrim':
            pkmn = 'Cherrim - Overcast Form'
        elif arg == 'giratina':
            pkmn = 'Giratina - Altered Forme'
        elif arg == 'Giratina':
            pkmn = 'Giratina - Altered Forme'
        elif arg == 'shaymin':
            pkmn = 'Shaymin - Land Forme'
        elif arg == 'Shaymin':
            pkmn = 'Shaymin - Land Forme'
        elif arg == 'basculin':
            pkmn = 'Basculin - Red-Striped Form'
        elif arg == 'Basculin':
            pkmn = 'Basculin - Red-Striped Form'
        elif arg == 'deerling':
            pkmn = 'Deerling - Spring Form'
        elif arg == 'Deerling':
            pkmn = 'Deerling - Spring Form'
        elif arg == 'tornadus':
            pkmn = 'Tornadus - Incarnate Forme'
        elif arg == 'Tornadus':
            pkmn = 'Tornadus - Incarnate Forme'
        elif arg == 'thundurus':
            pkmn = 'Thundurus - Incarnate Forme'
        elif arg == 'Thundurus':
            pkmn = 'Thundurus - Incarnate Forme'
        elif arg == 'landorus':
            pkmn = 'Landorus - Incarnate Forme'
        elif arg == 'Landorus':
            pkmn = 'Landorus - Incarnate Forme'
        elif arg == 'flabebe':
            pkmn = 'Flabébé'
        elif arg == 'Flabebe':
            pkmn = 'Flabébé'
        elif arg == 'zygarde':
            pkmn = 'Zygarde - Complete Forme'
        elif arg == 'Zygarde':
            pkmn = 'Zygarde - Complete Forme'
        elif arg == 'hoopa':
            pkmn = 'Hoopa Confined'
        elif arg == 'Hoopa':
            pkmn = 'Hoopa Confined'
        elif arg == 'oricorio':
            pkmn = 'Oricorio - Baile Style'
        elif arg == 'Oricorio':
            pkmn = 'Oricorio - Baile Style'
        elif arg == 'lycanroc':
            pkmn = 'Lycanroc - Midday Form'
        elif arg == 'Lycanroc':
            pkmn = 'Lycanroc - Midday Form'
        elif arg == 'wishiwashi':
            pkmn = 'Wishiwashi - Solo Form'
        elif arg == 'Wishiwashi':
            pkmn = 'Wishiwashi - Solo Form'
        elif arg == 'minior':
            pkmn = 'Minior - Meteor Form'
        elif arg == 'Minior':
            pkmn = 'Minior - Meteor Form'
        elif arg == 'mimikyu':
            pkmn = 'Mimikyu - Disguised Form'
        elif arg == 'Mimikyu':
            pkmn = 'Mimikyu - Disguised Form'
        else:
            pkmn = arg
        #--First we connect to the Pokedex API and download the Pokedex entry--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://pokeapi.glitch.me/v1/pokemon/' + pkmn) as dex_entry:
                data = await dex_entry.json()
                #--Now we attempt to extract information--#
                try:
                    pkmn_name = data[0]['name']
                    pkmn_no = data[0]['number']
                    pkmn_desc = data[0]['description']
                    pkmn_img = data[0]['sprite']
                    pkmn_height = data[0]['height']
                    pkmn_weight = data[0]['weight']
                    pkmn_species = data[0]['species']
                    pkmn_type1 = data[0]['types'][0]
                    pkmn_gen = str(data[0]['gen'])
                    pkmn_ability1 = data[0]['abilities']['normal'][0]
                    #--Detect if Pokemon has a second ability--#
                    try:
                        pkmn_ability2 = data[0]['abilities']['normal'][1]
                    except IndexError:
                        pkmn_ability2 = None
                    #--Detect if Pokemon has a hidden ability--#
                    try:
                        pkmn_hiddenability = data[0]['abilities']['hidden'][0]
                    except IndexError:
                        pkmn_hiddenability = None
                    #--Detect if Pokemon has a second type--#
                    try:
                        pkmn_type2 = data[0]['types'][1]
                    except IndexError:
                        pkmn_type2 = None
                    #--Finally, we format it into a nice little embed--#
                    embed = discord.Embed(title="<:pokeball:609749611321753669> Pokédex information for " + pkmn_name + " (#" + pkmn_no + ")", description=pkmn_desc, color=0xd82626)
                    embed.add_field(name='Height', value=pkmn_height)
                    embed.add_field(name='Weight', value=pkmn_weight)
                    embed.add_field(name='Species', value=pkmn_species)
                    #--Detect if type2 is defined--#
                    if pkmn_type2 == None:
                        embed.add_field(name='Type', value=pkmn_type1)
                    else:
                        embed.add_field(name='Types', value=pkmn_type1 + ", " + pkmn_type2)
                    #--Detect if ability2 and hiddenability defined--#
                    if pkmn_ability2 == None:
                        if pkmn_hiddenability == None:
                            embed.add_field(name='Ability', value=pkmn_ability1)
                        else:
                            embed.add_field(name='Abilities', value=pkmn_ability1 + ";\n **Hidden:** " + pkmn_hiddenability)
                    else:
                        if pkmn_hiddenability == None:
                            embed.add_field(name='Abilities', value=pkmn_ability1 + ", " + pkmn_ability2)
                        else:
                            embed.add_field(name='Abilities', value=pkmn_ability1 + ", " + pkmn_ability2 + ";\n **Hidden:** " + pkmn_hiddenability)
                    embed.add_field(name='Generation Introduced', value="Gen " + pkmn_gen)
                    embed.set_thumbnail(url=pkmn_img)
                    embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                    await ctx.send(embed=embed)
                except KeyError:
                    return await ctx.send(":x: I couldn't find any Pokémon with that name. Double-check your spelling and try again. \nIf you're certain that this Pokémon exists, file a bug report with **>bug**.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, *, user: discord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to hug! You can hug me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't hug yourself! You can hug me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/hug') as hug:
                data = await hug.json()
                result = data.get('url')
                embed = discord.Embed(title="🤗 " + ctx.author.name + " hugs " + user.name + "!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, ctx, *, user: discord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to cuddle! You can cuddle me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't cuddle yourself! You can cuddle me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/cuddle') as cuddle:
                data = await cuddle.json()
                result = data.get('url')
                embed = discord.Embed(title="🤗 " + ctx.author.name + " cuddles " + user.name + "!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, *, user: discord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to kiss! You can kiss me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't kiss yourself! You can kiss me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/kiss') as kiss:
                data = await kiss.json()
                result = data.get('url')
                embed = discord.Embed(title="❤ " + ctx.author.name + " kisses " + user.name + "!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def snuggle(self, ctx, *, user: discord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to cuddle! You can cuddle me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't cuddle yourself! You can cuddle me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/cuddle') as snuggle:
                data = await snuggle.json()
                result = data.get('url')
                embed = discord.Embed(title="🤗 " + ctx.author.name + " snuggles " + user.name + "!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command(aliases=["nsl", "ns", "switch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nslookup(self, ctx, *, game):
        #return await ctx.send(":x: Sorry, nslookup is not functioning right now. The esho.pw API, which is what I use for getting information on Nintendo Switch games, is down for (presumably) upgrades and maintenance. This is not something I can fix, and I have no idea when it'll be back. Please have patience! Thank you!")
        loading = await ctx.send('<a:loading:598027019447435285> Looking for a game on the eShop...')
        #--First we connect to the eSho.pw API--#
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.esho.pw/games") as r:
                data = await r.json(content_type="text/plain")
                #--Now we find information for the game and attempt to extract it--#
                for g in data:
                    if g["title_lower"] == game.lower():
                        gm = g
                        break
                    else:
                        gm = None
                if gm is None:
                    await loading.edit(content=":x: I couldn't find that game. Double-check your spelling and try again.")
                    return
                #--Now we format this into a nice embed to send back to Discord--#
                embed = discord.Embed(title="ℹ Nintendo Switch game information", color=0xff0000)
                embed.add_field(name="Title", value=gm["Title"], inline=True)
                #embed.add_field(name="Price", value="${}.{}".format(str(gm["Prices"]["US"])[0:2], str(gm["Prices"]["US"])[-2:]), inline=True)
                dt = dateutil.parser.parse(gm["Published"])
                embed.add_field(name="Released", value="{}/{}/{}".format(dt.month, dt.day, dt.year), inline=True)
                embed.add_field(name="Description", value=gm["Excerpt"], inline=True)
                embed.add_field(name="Categories", value=", ".join(gm["Categories"]).title(), inline=True)
                if "metascore" in gm["Metacritic"]:
                    embed.add_field(name="Metacritic Score", value=gm["Metacritic"]["metascore"], inline=True)
                else:
                    embed.add_field(name="Metacritic Score", value="None found!", inline=True)
                embed.set_image(url="https://" + gm["Image"][2:])
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await loading.edit(content='', embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))