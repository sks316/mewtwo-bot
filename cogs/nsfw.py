import discord
from discord.ext import commands
import aiohttp
import asyncio
import random
from random import shuffle
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import aiohttp
import xml.etree.ElementTree
import requests
import typing
import json
import rule34

botver = "Mewtwo v2.0"
user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3803.0 Safari/537.36 Edg/76.0.176.1"}

r34 = rule34.Sync()

async def r34_s(tags: str):
        #--First we connect to the Rule34 API and get search results--#
        async with aiohttp.ClientSession() as session:
            async with session.get(r34.URLGen(tags, 1200, deleted=False)) as url:
                rget = await url.text()
        #--Now we attempt to extract the information--#
        root = xml.etree.ElementTree.fromstring(rget)
        try:
                numeros = []
                num = root.attrib["count"]
                if num == 0:
                        return None
                random_pos = random.randint(0, len(root))
                position = random_pos
                link = root[position].attrib["file_url"]
                #--Now we return the information to the invoker--#
                return (link, root[position].attrib["tags"], root[position].attrib["score"], root.attrib["count"], root[position].attrib["id"])
        except ValueError:
                return None
        except Exception as e:
                pass
class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["r34"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def rule34(self, ctx, advanced: typing.Optional[bool] = False, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on Rule34...')
        try:
            #--Invoke a search from the Rule34 API--#
            image = await r34_s(search)
            #--Check if no results were found--#
            if image is None:
                return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")
            if image[0] == "I":
                while image[0] == "I":
                    image = r34_s(search)
            #--return information to Discord in an embed--#
            embed = discord.Embed(title=":underage: Rule34 image for **" + search + "**", description="_ _ \n:hash: **Number of posts:** "+str(image[3])+"\n\n--------POST--------"+"\n\n**`ID:`** "+str(image[4])+"\n\n**`tags:`** "+str(image[1])+"\n\n:arrow_up: **Score:** "+str(image[2]), color=0x8253c3)
            embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
            if not advanced:
                embed = discord.Embed(title=":underage: Rule34 image for **" + search + "**", description="_ _ \n:arrow_up: **Score:** "+str(image[2]), color=0x8253c3)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
            embed.set_image(url=str(image[0]))
            await loading.edit(content='', embed=embed)
        except IndexError:
            return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

    @commands.command(aliases=["booby", "tiddy", "tits"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def boobs(self, ctx, user: discord.Member = None):
        boobs =[
            'https://nekos.life/api/v2/img/boobs',
            'https://nekos.life/api/v2/img/tits',
        ]
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get(random.choice(boobs)) as tiddy:
                data = await tiddy.json()
                result = data.get('url')
                embed = discord.Embed(title="🔞 Boobies!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def fuck(self, ctx, *, user: discord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to fuck! Make sure they consent to it first...")
        if user == ctx.author:
            return await ctx.send(":x: You can't fuck yourself! You can masturbate, but you can't self-fuck.")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/classic') as fuck:
                data = await fuck.json()
                result = data.get('url')
                embed = discord.Embed(title="🔞 " + ctx.author.name + " fucks " + user.name + "!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def e621(self, ctx, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on e621...')
        #--Connect to e621 and get first 100 results--#
        e621_agent = {'User-Agent': 'Mewtwo Discord Bot/v2.0 https://github.com/sks316/mewtwo-bot'}
        async with aiohttp.ClientSession(headers=e621_agent) as session:
            async with session.get('https://e621.net/post/index.json?tags=' + search + '&limit=100') as esix:
                data = await esix.json()
                number = random.randint(0, 99)
                #--Now we attempt to extract information--#
                try:
                    score = str(data[number]['score'])
                    image = data[number]['file_url']
                    embed = discord.Embed(title=":underage: e621 image for **" + search + "**", description="_ _ \n:arrow_up: **Score:** " + score, color=0x8253c3)
                    embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                    embed.set_image(url=image)
                    await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

def setup(bot):
    bot.add_cog(NSFW(bot))