import nextcord
from nextcord.ext import commands
import asyncio
import random
import aiohttp
import dateutil.parser
import dataset
import json
from urllib.parse import quote_plus

botver = "Mewtwo v2.1" #--Bot's version, obviously--#

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
    'https://sks316.s-ul.eu/YRaq87pI',
    'https://sks316.s-ul.eu/X0LZFRSw',
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
    'https://sks316.s-ul.eu/kqNeFiph',
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
        embed = nextcord.Embed(title='😔 Today, we pay our respects to those that have left us.', color=0x8253c3)
        embed.set_image(url=random.choice(f_meme))
        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def meloetta(self, ctx):
        embed = nextcord.Embed(title="<:meloetta_aria:598168128345604127> Here you go, a cute Meloetta! :smile:",color=0x9fdf42)
        embed.add_field(name='List of image sources:', value="https://pastebin.com/cRd5vguH")
        embed.set_image(url=random.choice(melo))
        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def sylveon(self, ctx):
        embed = nextcord.Embed(title="<:sylveon:597725070764277786> Here, have some cute Sylveon art :3",color=0xffccfe)
        embed.add_field(name='List of image sources:', value="https://pastebin.com/RwGHXDmS")
        embed.set_image(url=random.choice(sylv))
        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command(aliases=["pokemon", "pkmn"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pokedex(self, ctx, *, arg):
        #--Some Pokemon with several forms are named differently on the API, so if one of those Pokemon are specified, we replace the query with the correct name--#
        pkmn = {
            'meloetta': 'Meloetta - Aria Forme',
            'keldeo': 'Keldeo - Ordinary Form',
            'burmy': 'Burmy - Plant Cloak',
            'wormadam': 'Wormadam - Plant Cloak',
            'cherrim': 'Cherrim - Overcast Form',
            'giratina': 'Giratina - Altered Forme',
            'shaymin': 'Shaymin - Land Forme',
            'basculin': 'Basculin - Red-Striped Form',
            'deerling': 'Deerling - Spring Form',
            'tornadus': 'Tornadus - Incarnate Forme',
            'thundurus': 'Thundurus - Incarnate Forme',
            'landorus': 'Landorus - Incarnate Forme',
            'flabebe': 'Flabébé',
            'zygarde': 'Zygarde - Complete Forme',
            'hoopa': 'Hoopa Confined',
            'oricorio': 'Oricorio - Baile Style',
            'lycanroc': 'Lycanroc - Midday Form',
            'wishiwashi': 'Wishiwashi - Solo Form',
            'minior': 'Minior - Meteor Form',
            'mimikyu': 'Mimikyu - Disguised Form',
        }.get(arg.lower(), arg)

        #--First we connect to the Pokedex API and download the Pokedex entry--#
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://pokeapi.glitch.me/v1/pokemon/{pkmn}') as dex_entry:
                data = await dex_entry.json()
                #--Now we attempt to extract information--#
                for x in data:
                    try:
                        pkmn_name = x['name']
                        pkmn_no = x['number']
                        pkmn_desc = x['description']
                        pkmn_img = x['sprite']
                        pkmn_height = x['height']
                        pkmn_weight = x['weight']
                        pkmn_species = x['species']
                        pkmn_type1 = x['types'][0]
                        pkmn_gen = str(x['gen'])
                        pkmn_ability1 = x['abilities']['normal'][0]
                        #--Detect if Pokemon has a second ability--#
                        try:
                            pkmn_ability2 = x['abilities']['normal'][1]
                        except IndexError:
                            pkmn_ability2 = None
                        #--Detect if Pokemon has a hidden ability--#
                        try:
                            pkmn_hiddenability = x['abilities']['hidden'][0]
                        except IndexError:
                            pkmn_hiddenability = None
                        #--Detect if Pokemon has a second type--#
                        try:
                            pkmn_type2 = x['types'][1]
                        except IndexError:
                            pkmn_type2 = None
                        #--Finally, we format it into a nice little embed--#
                        embed = nextcord.Embed(title=f"<:pokeball:609749611321753669> Pokédex information for {pkmn_name} (#{pkmn_no})", description=pkmn_desc, color=0xd82626)
                        embed.add_field(name='Height', value=pkmn_height)
                        embed.add_field(name='Weight', value=pkmn_weight)
                        embed.add_field(name='Species', value=pkmn_species)
                        #--Detect if type2 is defined--#
                        if pkmn_type2 == None:
                            embed.add_field(name='Type', value=pkmn_type1)
                        else:
                            embed.add_field(name='Types', value=f"{pkmn_type1}, {pkmn_type2}")
                        #--Detect if ability2 and hiddenability defined--#
                        if pkmn_ability2 == None:
                            if pkmn_hiddenability == None:
                                embed.add_field(name='Ability', value=pkmn_ability1)
                            else:
                                embed.add_field(name='Abilities', value=f"{pkmn_ability1};\n**Hidden:** {pkmn_hiddenability}")
                        else:
                            if pkmn_hiddenability == None:
                                embed.add_field(name='Abilities', value=f"{pkmn_ability1}, {pkmn_ability2}")
                            else:
                                embed.add_field(name='Abilities', value=f"{pkmn_ability1}, {pkmn_ability2};\n**Hidden:** {pkmn_hiddenability}")
                        embed.add_field(name='Generation Introduced', value=f"Gen {pkmn_gen}")
                        embed.set_thumbnail(url=pkmn_img)
                        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        await ctx.send(embed=embed)
                    except (KeyError, TypeError):
                        return await ctx.send(":x: I couldn't find any Pokémon with that name. Double-check your spelling and try again. \nIf you're certain that this Pokémon exists, file a bug report with **>bug**.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def amiibo(self, ctx, *, arg):
        #--First we connect to the Amiibo API and download the Amiibo information--#
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://amiiboapi.com/api/amiibo/?name={arg}') as amiibo:
                data = await amiibo.json()
                #--Now we attempt to extract information--#
                try:
                    series = data['amiibo'][0]['amiiboSeries']
                    character = data['amiibo'][0]['character']
                    name = data['amiibo'][0]['name']
                    game = data['amiibo'][0]['gameSeries']
                    atype = data['amiibo'][0]['type']
                    na_release = data['amiibo'][0]['release']['na']
                    eu_release = data['amiibo'][0]['release']['eu']
                    jp_release = data['amiibo'][0]['release']['jp']
                    au_release = data['amiibo'][0]['release']['au']
                    image = data['amiibo'][0]['image']
                    #--Finally, we format it into a nice little embed--#
                    embed = nextcord.Embed(title=f"<:amiibo:688255989060730880> Amiibo information for {name} ({series} series)", color=0xd82626)
                    embed.add_field(name='Character Represented', value=character)
                    embed.add_field(name='Amiibo Series', value=f"{series} series")
                    embed.add_field(name='Game of Origin', value=game)
                    embed.add_field(name='Type', value=atype)
                    embed.add_field(name='Released', value=f":flag_us: {na_release}\n:flag_eu: {eu_release}\n:flag_jp: {jp_release}\n:flag_au: {au_release}")
                    embed.set_thumbnail(url=image)
                    embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                    await ctx.send(embed=embed)
                except KeyError:
                    return await ctx.send(":x: I couldn't find any Amiibo with that name. Double-check your spelling and try again. \nIf you're certain that this Amiibo exists, file a bug report with **>bug**.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def urban(self, ctx, *, arg):
        msg = await ctx.send("<a:loading:598027019447435285> Looking for a definition...")
        try:
            #--First we connect to Urban Dictionary's API and get the results--#
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://api.urbandictionary.com/v0/define?term={arg}') as r:
                    #--Now we decode the JSON and get the variables, truncating definitions and examples if they are longer than 900 characters due to Discord API limitations and replacing example with None if blank--#
                    result = await r.json()
                    word = result['list'][0]['word']
                    url = result['list'][0]['permalink']
                    upvotes = result['list'][0]['thumbs_up']
                    downvotes = result['list'][0]['thumbs_down']
                    author = result['list'][0]['author']
                    definition = result['list'][0]['definition']
                    definition = definition.replace('[', '')
                    definition = definition.replace(']', '')
                    if len(definition) > 900:
                        definition = definition[0:901]
                        definition = f"{definition}[...]({url})"
                    example = result['list'][0]['example']
                    example = example.replace('[', '')
                    example = example.replace(']', '')
                    if len(example) > 900:
                        example = example[0:901]
                        example = f"{example}[...]({url})"
                    if len(example) < 1:
                        example = None
                    embed = nextcord.Embed(title=f":notebook: Urban Dictionary Definition for {word}", description=definition, url=url, color=0x8253c3)
                    if example == None:
                        pass
                    else:
                        embed.add_field(name="Example:", value=example, inline=False)
                    embed.set_footer(text=f"{botver} by PrincessLillie - Author: {author} - 👍️ {str(upvotes)} - 👎️ {str(downvotes)}", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                    await msg.edit(content='', embed=embed)
        except:
            await msg.edit(content=":x: Sorry, I couldn't find that word. Check your spelling and try again.")
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to hug! You can hug me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't hug yourself! You can hug me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/hug') as hug:
                data = await hug.json()
                result = data.get('url')
                embed = nextcord.Embed(title=f"🤗 {ctx.author.display_name} hugs {user.display_name}!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command(aliases=["pats", "pet"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to give headpats to! You can give me a headpat if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't give yourself headpats! You can give me a headpat if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/pat') as pat:
                data = await pat.json()
                result = data.get('url')
                embed = nextcord.Embed(title=f"<a:ablobheadpats:612416610556313600> {ctx.author.display_name} gives {user.display_name} some headpats!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to cuddle! You can cuddle me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't cuddle yourself! You can cuddle me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/cuddle') as cuddle:
                data = await cuddle.json()
                result = data.get('url')
                embed = nextcord.Embed(title=f"🤗 {ctx.author.display_name} cuddles {user.display_name}!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command(aliases=["smooch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to kiss! You can kiss me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't kiss yourself! You can kiss me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/kiss') as kiss:
                data = await kiss.json()
                result = data.get('url')
                embed = nextcord.Embed(title=f"❤ {ctx.author.display_name} kisses {user.display_name}!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def snuggle(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to cuddle! You can cuddle me if you want...")
        if user == ctx.author:
            return await ctx.send(":x: You can't cuddle yourself! You can cuddle me if you want...")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/cuddle') as snuggle:
                data = await snuggle.json()
                result = data.get('url')
                embed = nextcord.Embed(title=f"🤗 {ctx.author.display_name} snuggles {user.display_name}!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command(aliases=["nsl", "ns", "switch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nslookup(self, ctx, *, game):
        await ctx.send(':x: This command has been retired. The API this command used has shut down, and my developer could not find a suitable replacement. If you find a suitable replacement, please notify my developer!')
        #loading = await ctx.send('<a:loading:598027019447435285> Looking for a game on the eShop...')
        ##--First we connect to the eSho.pw API--#
        #async with aiohttp.ClientSession() as cs:
        #    async with cs.get("https://api.esho.pw/games") as r:
        #        data = await r.json(content_type="text/plain")
        #        #--Now we find information for the game and attempt to extract it--#
        #        for g in data:
        #            if g["title_lower"] == game.lower():
        #                gm = g
        #                break
        #            else:
        #                gm = None
        #        if gm is None:
        #            await loading.edit(content=":x: I couldn't find that game. Double-check your spelling and try again.")
        #            return
        #        #--Now we format this into a nice embed to send back to Discord--#
        #        embed = nextcord.Embed(title="ℹ Nintendo Switch game information", color=0xff0000)
        #        embed.add_field(name="Title", value=gm["Title"], inline=True)
        #        #embed.add_field(name="Price", value="${}.{}".format(str(gm["Prices"]["US"])[0:2], str(gm["Prices"]["US"])[-2:]), inline=True)
        #        dt = dateutil.parser.parse(gm["Published"])
        #        embed.add_field(name="Released", value="{}/{}/{}".format(dt.month, dt.day, dt.year), inline=True)
        #        embed.add_field(name="Description", value=gm["Excerpt"], inline=True)
        #        embed.add_field(name="Categories", value=", ".join(gm["Categories"]).title(), inline=True)
        #        if "metascore" in gm["Metacritic"]:
        #            embed.add_field(name="Metacritic Score", value=gm["Metacritic"]["metascore"], inline=True)
        #        else:
        #            embed.add_field(name="Metacritic Score", value="None found!", inline=True)
        #        embed.set_image(url=f'https://{gm["Image"][2:]}')
        #        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        #        await loading.edit(content='', embed=embed)

    @commands.command(aliases=["rabbit"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bunny(self, ctx, *, user: nextcord.Member = None):
        #--Get image from bunnies.io API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.bunnies.io/v2/loop/random/?media=gif,png') as bunny:
                data = await bunny.json()
                try:
                    image = data["media"]["gif"]
                except:
                    image = data["media"]["poster"]
                seen = data["thisServed"]
                total = data["totalServed"]
                id = data["id"]
                embed = nextcord.Embed(title=f"🐇 Bunny!!!", description=f"🔢 ID: {id}\n👀 This bunny has been seen {seen} times.\n🐰 {total} bunnies have been seen.\n🔗 https://www.bunnies.io/#{id}", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
