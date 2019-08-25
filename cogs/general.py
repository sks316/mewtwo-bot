import discord
from discord.ext import commands
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

botver = "Mewtwo v2.0"

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
                async with session.get('https://www.googleapis.com/customsearch/v1?key=' + config.google_api_key + '&cx=' + config.google_search_engine + '&q=' + arg) as cse:
                    search = await cse.json()
            #--Now we attempt to extract the results--#
            try:
                result = search['items'][0]['link']
            #--Throw an error if no results found--#
            except KeyError:
                return await loading.edit(content=':x: No search results were found. Check your spelling and try again.')
            await loading.edit(content='<:google:598024418920366080> Search result for **' + arg + '**: ' + result)

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
                async with session.get('https://www.googleapis.com/youtube/v3/search?key=' + config.google_api_key + '&part=snippet&type=video&q=' + arg) as yts:
                    search = await yts.json()
            #--Now we attempt to extract the results--#
            try:
                result = search['items'][0]['id']['videoId']
            #--Throw an error if no results found--#
            except IndexError:
                return await loading.edit(content=':x: No search results were found. Check your spelling and try again.')
            await loading.edit(content="<:youtube:609300907343216650> Search result for **" + arg + "**: http://www.youtube.com/watch?v=" + result)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f":ping_pong: Ping! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command(aliases=["avy"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def avatar(self, ctx, *, user: discord.Member = None):
      if user == None:
            user = ctx.author
      embed = discord.Embed(title="🖼 " + user.name + "#" + user.discriminator + "'s avatar",  color=0x8253c3)
      embed.set_image(url=user.avatar_url_as(format=None, size=1024))
      embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
      await ctx.send(embed=embed)

    @commands.command(aliases=["serverinfo"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def server(self, ctx):
        level = str(ctx.guild.premium_tier)
        boosts = str(ctx.guild.premium_subscription_count)
        if boosts is 'None':
            boosts = 'Zero'
        embed = discord.Embed(title="ℹ Information about " + ctx.guild.name, color=0x8253c3)
        embed.add_field(name="Nitro Boost", value='Level ' + level + ", " + boosts + " boost(s)", inline=True)
        embed.add_field(name="Owner", value="{}#{}".format(ctx.guild.owner.name, ctx.guild.owner.discriminator), inline=True)
        embed.add_field(name="Created On", value="{}/{}/{}".format(ctx.guild.created_at.month, ctx.guild.created_at.day, ctx.guild.created_at.year), inline=True)
        embed.add_field(name="Member Count", value=len(ctx.guild.members), inline=True)
        embed.add_field(name="Channel Count", value=len(ctx.guild.channels), inline=True)
        embed.add_field(name="Region", value=ctx.guild.region, inline=True)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title=botver, description="The command prefix is `>`. To run a command, you must begin a message with `>`. \nFor those that don't want to see them, I've given NSFW commands their own help message. To see them, run `>nsfwhelp`.", color=0x8253c3)
        embed.add_field(name="General:", value="**>help** - DMs you this help message. \n**>nsfwhelp** - DMs you the help message for NSFW commands. \n**>info** - Info about Mewtwo. \n**>ping** - Pong! Returns the bot's latency. Aliases: **>pong** \n**>avatar** - Gets the avatar for a specified user. If no user is specified, your avatar is sent instead. Aliases: **>avy**\n**>google** - Searches Google for a specified query and returns the first result. Aliases: **>g, >gsearch** \n**>youtube** - Searches YouTube for a specified query and returns the first result. Aliases: **>yt, >ytsearch** \n**>server** - Shows information about the server. Aliases: **>serverinfo**", inline=False)
        embed.add_field(name="Fun:", value="**>echo** - I'll say whatever you want me to! Aliases: **>say** \n**>greet** - Hello there. \n**>f** - Press F to pay respects. Aliases: **>respects** \n**>sylveon** - Posts some cute as heck Sylveon art! \n**>meloetta** - Posts some cute as heck Meloetta art! \n**>hug** - Hug someone and brighten up their day! \n**>cuddle** - Snuggle with someone! Aliases: **>snuggle** \n**>kiss** - Kiss someone! Show them your love! Aliases: **>smooch** \n**>pat** - Give someone headpats! Aliases: **>pats, >pet** \n**>nslookup** - Gets information for a Nintendo Switch game. Aliases: **>nsl, >ns, >switch** \n**>pokedex** - Gets information for a specified Pokémon. Uses the [Pokédex API by PokéDevs](https://pokedevs.gitbook.io/pokedex/). Aliases: **>pokemon, >pkmn**", inline=False)
        embed.add_field(name="Other:", value="**>bug** - Submit a bug report if anything goes wrong. \n**>suggest** - Want to see something added to the bot? Suggest it!", inline=False)
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("✅")

    @commands.command(pass_context=True)
    async def nsfwhelp(self, ctx):
        embed = discord.Embed(title=botver, description="The command prefix is `>`. To run a command, you must begin a message with `>`. \n**NSFW commands will work only in NSFW channels or DMs.**", color=0x8253c3)
        embed.add_field(name="NSFW commands:", value="**>rule34** - Gets a random image from Rule34.xxx that matches the provided query. Aliases: **>r34** \n**>e621** - Gets a random image from e621 that matches the provided query. \n**>gelbooru** - Gets a random image from Gelbooru that matches the provided query. \n**>boobs** - Boobies! Gets a random titty image or GIF from the nekos.life API. Aliases: **>booby, >tiddy, >tits** \n**>fuck** - Fuck somebody, make them feel good! :wink:", inline=False)
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("🔞")

def setup(bot):
    bot.add_cog(General(bot))