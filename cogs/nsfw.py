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

botver = "Mewtwo v2.0"


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["r34"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def rule34(self, ctx, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on Rule34...')
        #--Connect to Rule34 JSON API and download search data--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://r34-json.herokuapp.com/posts?tags=' + search) as r34:
                data = await r34.json()
                #--Now we attempt to extract information--#
                try:
                    posts = data['posts']
                    post = random.choice(posts)
                    score = post['score']
                    image = post['file_url']
                    image = image.replace("https://r34-json.herokuapp.com/images?url=", "")
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=":underage: Rule34 image for **" + search + "** \n\n:arrow_up: **Score:** " + score + "\n\n**Video URL:** " + image)
                    else:
                        embed = discord.Embed(title=":underage: Rule34 image for **" + search + "**", description="_ _ \n:arrow_up: **Score:** " + score, color=0x8253c3)
                        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def gelbooru(self, ctx, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on Gelbooru...')
        #--Connect to Gelbooru JSON API and download search data--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=' + search) as gel:
                data = await gel.json()
                #--Now we attempt to extract information--#
                try:
                    post = random.choice(data)
                    score = str(post['score'])
                    image = post['file_url']
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=":underage: Gelbooru image for **" + search + "** \n\n:arrow_up: **Score:** " + score + "\n\n**Video URL:** " + image)
                    else:
                        embed = discord.Embed(title=":underage: Gelbooru image for **" + search + "**", description="_ _ \n:arrow_up: **Score:** " + score, color=0x8253c3)
                        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")
                except TypeError:
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
                #--Now we attempt to extract information--#
                try:
                    post = random.choice(data)
                    score = str(post['score'])
                    image = post['file_url']
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=":underage: e621 image for **" + search + "** \n\n:arrow_up: **Score:** " + score + "\n\n**Video URL:** " + image)
                    else:
                        embed = discord.Embed(title=":underage: e621 image for **" + search + "**", description="_ _ \n:arrow_up: **Score:** " + score, color=0x8253c3)
                        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

def setup(bot):
    bot.add_cog(NSFW(bot))
