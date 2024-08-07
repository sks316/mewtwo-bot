import nextcord
from nextcord.ext import commands
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import re
import requests
import datetime
import mewtwo_config as config

botver = "Mewtwo v2.1"

async def get_dev(self):
    dev = self.bot.get_user(config.owner)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["g", "gsearch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def google(self, ctx, *, arg):
        if ctx.message.mention_everyone:
            return await ctx.send(":x: Sorry, you may not tag everyone/here in this command.")
        elif ctx.message.raw_mentions:
            return await ctx.send(":x: Sorry, you may not tag other users in this command.")
        if ctx.message.raw_role_mentions:
            return await ctx.send(":x: Sorry, you may not tag roles in this command.")
        elif '@everyone' in ctx.message.content:
            return await ctx.send(":x: Sorry, you may not tag everyone/here in this command.")
        elif '@here' in ctx.message.content:
            return await ctx.send(":x: Sorry, you may not tag everyone/here in this command.")
        else:
            loading = await ctx.send('<a:loading:598027019447435285> Looking for a search result on Google...')
            #--First we connect to the Custom Search API and download the search results--#
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://www.googleapis.com/customsearch/v1?key={config.google_api_key}&cx={config.google_search_engine}&q={arg}') as cse:
                    search = await cse.json()
            #--Now we attempt to extract the results--#
            try:
                result = search['items'][0]['link']
            #--Throw an error if no results found--#
            except KeyError:
                return await loading.edit(content=':x: No search results were found. Check your spelling and try again.')
            await loading.edit(content=f"<:google:598024418920366080> Search result for **{arg}**: {result}")

    @commands.command(pass_context=True, aliases=["yt", "ytsearch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtube(self, ctx, *, arg):
        if ctx.message.mention_everyone:
            return await ctx.send(":x: Sorry, you may not tag everyone/here in this command.")
        elif ctx.message.raw_mentions:
            return await ctx.send(":x: Sorry, you may not tag other users in this command.")
        if ctx.message.raw_role_mentions:
            return await ctx.send(":x: Sorry, you may not tag roles in this command.")
        elif '@everyone' in ctx.message.content:
            return await ctx.send(":x: Sorry, you may not tag everyone/here in this command.")
        elif '@here' in ctx.message.content:
            return await ctx.send(":x: Sorry, you may not tag everyone/here in this command.")
        else:
            loading = await ctx.send('<a:loading:598027019447435285> Looking for a video on YouTube...')
            #--First we connect to the YouTube Data API and download the search results--#
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://www.googleapis.com/youtube/v3/search?key={config.google_api_key}&part=snippet&type=video&q={arg}') as yts:
                    search = await yts.json()
            #--Now we attempt to extract the results--#
            try:
                result = search['items'][0]['id']['videoId']
            #--Throw an error if no results found--#
            except IndexError:
                return await loading.edit(content=':x: No search results were found. Check your spelling and try again.')
            await loading.edit(content=f"<:youtube:609300907343216650> Search result for **{arg}**: http://www.youtube.com/watch?v={result}")

    @commands.command(aliases=["definition", "dictionary"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def define(self, ctx, *, arg):
        msg = await ctx.send("<a:loading:598027019447435285> Looking for a definition...")
        try:
            #--Connect to unofficial Google Dictionary API and get results--#
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.dictionaryapi.dev/api/v1/entries/en/{arg}') as r:
                    #--Now we decode the JSON and get the variables, replacing them with None if they fail to define--#
                    result = await r.json()
                    word = result[0]['word']
                    try:
                        origin = result[0]['origin']
                    except KeyError:
                        origin = None
                    try:
                        noun_def = result[0]['meaning']['noun'][0]['definition']
                    except KeyError:
                        noun_def = None
                    try:
                        noun_eg = result[0]['meaning']['noun'][0]['example']
                    except KeyError:
                        noun_eg = None
                    try:
                        verb_def = result[0]['meaning']['verb'][0]['definition']
                    except KeyError:
                        verb_def = None
                    try:
                        verb_eg = result[0]['meaning']['verb'][0]['example']
                    except KeyError:
                        verb_eg = None
                    try:
                        prep_def = result[0]['meaning']['preposition'][0]['definition']
                    except KeyError:
                        prep_def = None
                    try:
                        prep_eg = result[0]['meaning']['preposition'][0]['example']
                    except KeyError:
                        prep_eg = None
                    try:
                        adverb_def = result[0]['meaning']['adverb'][0]['definition']
                    except KeyError:
                        adverb_def = None
                    try:
                        adverb_eg = result[0]['meaning']['adverb'][0]['example']
                    except KeyError:
                        adverb_eg = None
                    try:
                        adject_def = result[0]['meaning']['adjective'][0]['definition']
                    except KeyError:
                        adject_def = None
                    try:
                        adject_eg = result[0]['meaning']['adjective'][0]['example']
                    except KeyError:
                        adject_eg = None
                    try:
                        pronoun_def = result[0]['meaning']['pronoun'][0]['definition']
                    except KeyError:
                        pronoun_def = None
                    try:
                        pronoun_eg = result[0]['meaning']['pronoun'][0]['example']
                    except KeyError:
                        pronoun_eg = None
                    try:
                        exclaim_def = result[0]['meaning']['exclamation'][0]['definition']
                    except KeyError:
                        exclaim_def = None
                    try:
                        exclaim_eg = result[0]['meaning']['exclamation'][0]['example']
                    except KeyError:
                        exclaim_eg = None
                    try:
                        poss_determ_def = result[0]['meaning']['possessive determiner'][0]['definition']
                    except KeyError:
                        poss_determ_def = None
                    try:
                        poss_determ_eg = result[0]['meaning']['possessive determiner'][0]['example']
                    except KeyError:
                        poss_determ_eg = None
                    try:
                        abbrev_def = result[0]['meaning']['abbreviation'][0]['definition']
                    except KeyError:
                        abbrev_def = None
                    try:
                        abbrev_eg = result[0]['meaning']['abbreviation'][0]['example']
                    except KeyError:
                        abbrev_eg = None
                    try:
                        crossref_def = result[0]['meaning']['crossReference'][0]['definition']
                    except KeyError:
                        crossref_def = None
                    try:
                        crossref_eg = result[0]['meaning']['crossReference'][0]['example']
                    except KeyError:
                        crossref_eg = None
                    embed = nextcord.Embed(title=f":blue_book: Google Definition for {word}", color=0x8253c3)
                    #--Then we add see if the variables are defined and if they are, those variables to an embed and send it back to Discord--#
                    if origin == None:
                        pass
                    else:
                        embed.add_field(name="Origin:", value=origin, inline=False)
                    if noun_def == None:
                        pass
                    else:
                        if noun_eg == None:
                            embed.add_field(name="As a Noun:", value=f"**Definition:** {noun_def}", inline=False)
                        else:
                            embed.add_field(name="As a Noun:", value=f"**Definition:** {noun_def}\n**Example:** {noun_eg}", inline=False)
                    if verb_def == None:
                        pass
                    else:
                        if verb_eg == None:
                            embed.add_field(name="As a Verb:", value=f"**Definition:** {verb_def}", inline=False)
                        else:
                            embed.add_field(name="As a Verb:", value=f"**Definition:** {verb_def}\n**Example:** {verb_eg}", inline=False)
                    if prep_def == None:
                        pass
                    else:
                        if prep_eg == None:
                            embed.add_field(name="As a Preposition:", value=f"**Definition:** {prep_def}", inline=False)
                        else:
                            embed.add_field(name="As a Preposition:", value=f"**Definition:** {prep_def}\n**Example:** {prep_eg}", inline=False)
                    if adverb_def == None:
                        pass
                    else:
                        if adverb_eg == None:
                            embed.add_field(name="As an Adverb:", value=f"**Definition:** {adverb_def}", inline=False)
                        else:
                            embed.add_field(name="As a Adverb:", value=f"**Definition:** {adverb_def}\n**Example:** {adverb_eg}", inline=False)
                    if adject_def == None:
                        pass
                    else:
                        if adject_eg == None:
                            embed.add_field(name="As an Adjective:", value=f"**Definition:** {adject_def}", inline=False)
                        else:
                            embed.add_field(name="As an Adjective:", value=f"**Definition:** {adject_def}\n**Example:** {adject_eg}", inline=False)
                    if pronoun_def == None:
                        pass
                    else:
                        if pronoun_eg == None:
                            embed.add_field(name="As a Pronoun:", value=f"**Definition:** {pronoun_def}", inline=False)
                        else:
                            embed.add_field(name="As a Pronoun:", value=f"**Definition:** {pronoun_def}\n**Example:** {pronoun_eg}", inline=False)
                    if exclaim_def == None:
                        pass
                    else:
                        if exclaim_eg == None:
                            embed.add_field(name="As an Exclamation:", value=f"**Definition:** {exclaim_def}", inline=False)
                        else:
                            embed.add_field(name="As an Exclamation:", value=f"**Definition:** {exclaim_def}\n**Example:** {exclaim_eg}", inline=False)
                    if poss_determ_def == None:
                        pass
                    else:
                        if poss_determ_eg == None:
                            embed.add_field(name="As a Possessive Determiner:", value=f"**Definition:** {poss_determ_def}", inline=False)
                        else:
                            embed.add_field(name="As a Possessive Determiner:", value=f"**Definition:** {poss_determ_def}\n**Example:** {poss_determ_eg}", inline=False)
                    if abbrev_def == None:
                        pass
                    else:
                        if abbrev_eg == None:
                            embed.add_field(name="As an Abbreviation:", value=f"**Definition:** {abbrev_def}", inline=False)
                        else:
                            embed.add_field(name="As an Abbreviation:", value=f"**Definition:** {abbrev_def}\n**Example:** {abbrev_eg}", inline=False)
                    if crossref_def == None:
                        pass
                    else:
                        if crossref_eg == None:
                            embed.add_field(name="As a Cross-Reference:", value=f"**Definition:** {crossref_def}", inline=False)
                        else:
                            embed.add_field(name="As a Cross-Reference:", value=f"**Definition:** {crossref_def}\n**Example:** {crossref_eg}", inline=False)
                    embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                    await msg.edit(content='',embed=embed)
        except:
            #--Send error message if command fails, as it's assumed a definition isn't found--#
            await msg.edit(content=":x: Sorry, I couldn't find that word. Check your spelling and try again.")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f":ping_pong: Ping! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command(aliases=["avy"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def avatar(self, ctx, *, user: nextcord.Member = None):
      if user == None:
            user = ctx.author
      embed = nextcord.Embed(title=f"🖼 {user.display_name}'s avatar",  color=user.color)
      embed.set_image(url=user.display_avatar.url)
      embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
      await ctx.send(embed=embed)

    @commands.command(aliases=["serverinfo"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def server(self, ctx):
        level = str(ctx.guild.premium_tier)
        region = str(ctx.guild.region)
        boosts = str(ctx.guild.premium_subscription_count)
        if not ctx.guild.premium_subscription_count:
            boosts = 'Zero'
        sregion = {
            'brazil': ':flag_br: Brazil',
            'europe': ':flag_eu: Europe',
            'hongkong': ':flag_hk: Hong Kong',
            'india': ':flag_in: India',
            'japan': ':flag_jp: Japan',
            'russia': ':flag_ru: Russia',
            'singapore': ':flag_sg: Singapore',
            'southafrica': ':flag_za: South Africa',
            'sydney': ':flag_au: Sydney',
            'us-central': ':flag_us: US Central',
            'us-east': ':flag_us: US East',
            'us-south': ':flag_us: US South',
            'us-west': ':flag_us: US West',
        }.get(region)
        embed = nextcord.Embed(title=f"ℹ Information about {ctx.guild.name}", color=0x8253c3)
        embed.add_field(name="Nitro Boost", value=f'Level {level}, {boosts} boost(s)', inline=True)
        embed.add_field(name="Owner", value=f"{ctx.guild.owner.name}#{ctx.guild.owner.discriminator}", inline=True)
        embed.add_field(name="Created On", value=f"{ctx.guild.created_at.month}/{ctx.guild.created_at.day}/{ctx.guild.created_at.year}", inline=True)
        embed.add_field(name="Member Count", value=len(ctx.guild.members), inline=True)
        embed.add_field(name="Channel Count", value=len(ctx.guild.channels), inline=True)
        embed.add_field(name="Region", value=sregion, inline=True)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = nextcord.Embed(title=botver, description="The help message got too long, so it's been moved to a Carrd website to prevent clutter and DM spam. Please see [my Carrd site](https://mewtwo-bot.carrd.co) for the command list as well as the invite link. Apologies for any inconveniences this may cause.", color=0x8253c3)
        embed.set_thumbnail(url="https://sks316.s-ul.eu/bsHvTCLJ")
        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def nsfwhelp(self, ctx):
        embed = nextcord.Embed(title=botver, description="The command prefix is `>`. To run a command, you must begin a message with `>`. \n**NSFW commands will work only in NSFW channels or DMs.**", color=0x8253c3)
        embed.add_field(name="NSFW commands:", value="**>rule34** - Gets a random image from Rule34.xxx that matches the provided query. Aliases: **>r34** \n**>e621** - Gets a random image from e621 that matches the provided query. \n**>gelbooru** - Gets a random image from Gelbooru that matches the provided query. \n**>yandere** - Gets a random image from yande.re that matches the provided query. \n**>derpibooru** - Gets a random explicit image from Derpibooru that matches the provided query. Aliases: **>derpy** \n**>fuck** - Fuck somebody, make them feel good! :wink:", inline=False)
        embed.set_footer(text=f"{botver} by PrincessLillie", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("🔞")

def setup(bot):
    bot.add_cog(General(bot))
