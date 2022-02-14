import nextcord
from nextcord.ext import commands
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
            async with session.get(f'https://r34-json.herokuapp.com/posts?tags={search}') as r34:
                data = await r34.json()
                #--Now we attempt to extract information--#
                try:
                    posts = data['posts']
                    post = random.choice(posts)
                    score = post['score']
                    post_id = post['id']
                    image = post['file_url']
                    image = image.replace("https://r34-json.herokuapp.com/images?url=", "")
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=f":underage: Rule34 image for **{search}** \n\n:arrow_up: **Score:** {score}\n\n:link: **Post URL:** <https://rule34.xxx/index.php?page=post&s=view&id={post_id}>\n\n:link: **Video URL:** {image}")
                    else:
                        embed = nextcord.Embed(title=f":underage: Rule34 image for **{search}**", description=f"_ _ \n:arrow_up: **Score:** {score}\n\n:link: **[Post URL](https://rule34.xxx/index.php?page=post&s=view&id={post_id})**", color=0x8253c3)
                        embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

    @commands.command(aliases=["derpy"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def derpibooru(self, ctx, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on Derpibooru...')
        #--Check NSFW status of channel. Return only NSFW results if NSFW, return safe results if not--#
        channel = self.bot.get_channel(ctx.channel.id)
        try:
            if channel.is_nsfw():
                nsfw_toggle = "explicit"
                derpi_filter = "56027"
            else:
                nsfw_toggle = "safe"
                derpi_filter = "100073"
        except AttributeError:
            nsfw_toggle = "safe"
            derpi_filter = "100073"
        #--Connect to Derpibooru JSON API and download search data--#
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://derpibooru.org/api/v1/json/search/images?q={nsfw_toggle}, {search}&filter_id={derpi_filter}') as derp:
                data = await derp.json()
                #--Now we attempt to extract information--#
                try:
                    posts = data['images']
                    post = random.choice(posts)
                    score = post['score']
                    post_id = post['id']
                    image = post['view_url']
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=f":horse: Derpibooru image for **{search}** \n\n:arrow_up: **Score:** {score}\n\n:link: **Post URL:** <https://derpibooru.org/images/{post_id}>\n\n:link: **Video URL:** {image}")
                    else:
                        embed = nextcord.Embed(title=f":horse: Derpibooru image for **{search}**", description=f"_ _ \n:arrow_up: **Score:** {score}\n\n:link: **[Post URL](https://derpibooru.org/images/{post_id})**", color=0x8253c3)
                        embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
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
            async with session.get(f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={search}') as gel:
                data = await gel.json()
                #--Now we attempt to extract information--#
                try:
                    data = data['post']
                    post = random.choice(data)
                    score = str(post['score'])
                    post_id = str(post['id'])
                    image = post['file_url']
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=f":underage: Gelbooru image for **{search}** \n\n:arrow_up: **Score:** {score}\n\n:link: **Post URL:** <https://gelbooru.com/index.php?page=post&s=view&id={post_id}>\n\n:link: **Video URL:** {image}")
                    else:
                        embed = nextcord.Embed(title=f":underage: Gelbooru image for **{search}**", description=f"_ _ \n:arrow_up: **Score:** {score}\n\n:link: **[Post URL](https://gelbooru.com/index.php?page=post&s=view&id={post_id})**", color=0x8253c3)
                        embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")
                except TypeError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

    @commands.command(aliases=["booby", "tiddy", "tits"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def boobs(self, ctx, user: nextcord.Member = None):
        boobs =[
            'https://nekos.life/api/v2/img/boobs',
            'https://nekos.life/api/v2/img/tits',
        ]
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get(random.choice(boobs)) as tiddy:
                data = await tiddy.json()
                result = data.get('url')
                embed = nextcord.Embed(title="🔞 Boobies!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def fuck(self, ctx, *, user: nextcord.Member = None):
        if user == None:
            return await ctx.send(":x: You need someone to fuck! Make sure they consent to it first...")
        if user == ctx.author:
            return await ctx.send(":x: You can't fuck yourself! You can masturbate, but you can't self-fuck.")
        #--Get image from NekosLife API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/classic') as fuck:
                data = await fuck.json()
                result = data.get('url')
                embed = nextcord.Embed(title=f"🔞 {ctx.author.display_name} fucks {user.display_name}!",  color=0x8253c3)
                embed.set_image(url=result)
                embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def yandere(self, ctx, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on yande.re...')
        #--Connect to yande.re and get first 100 results--#
        yande_agent = {'User-Agent': 'Mewtwo Discord Bot/v2.0 https://github.com/sks316/mewtwo-bot'}
        async with aiohttp.ClientSession(headers=yande_agent) as session:
            async with session.get(f'https://yande.re/post/index.json?tags={search}&limit=100') as yande:
                data = await yande.json()
                #--Now we attempt to extract information--#
                try:
                    post = random.choice(data)
                    score = str(post['score'])
                    post_id = str(post['id'])
                    image = post['file_url']
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=f":underage: yande.re image for **{search}** \n\n:arrow_up: **Score:** {score}\n\n:link: **Post URL:** <https://yande.re/post/show/{post_id}>\n\n:link: **Video URL:** {image}")
                    else:
                        embed = nextcord.Embed(title=f":underage: yande.re image for **{search}**", description=f"_ _ \n:arrow_up: **Score:** {score}\n\n:link: **[Post URL](https://yande.re/post/show/{post_id})**", color=0x8253c3)
                        embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    async def e621(self, ctx, *, search: str):
        loading = await ctx.send('<a:loading:598027019447435285> Looking for an image on e621...')
        #--Connect to e621 and get first 100 results--#
        e621_agent = {'User-Agent': 'Mewtwo Discord Bot/v2.0 https://github.com/sks316/mewtwo-bot'}
        async with aiohttp.ClientSession(headers=e621_agent) as session:
            async with session.get(f'https://e621.net/posts.json?tags={search}&limit=100') as esix:
                data = await esix.json()
                #--Now we attempt to extract information--#
                try:
                    data = data['posts']
                    post = random.choice(data)
                    score = str(post['score']['total'])
                    post_id = str(post['id'])
                    image = post['file']['url']
                    if image.endswith(".webm") or image.endswith(".mp4"):
                        await loading.edit(content=f":underage: e621 image for **{search}**\n\n:arrow_up: **Score:** {score}\n\n:link: **Post URL:** <https://e621.net/posts/{post_id}>\n\n:link: **Video URL:** {image}")
                    else:
                        embed = nextcord.Embed(title=f":underage: e621 image for **{search}**", description=f"_ _ \n:arrow_up: **Score:** {score}\n\n:link: **[Post URL](https://e621.net/posts/{post_id})**", color=0x8253c3)
                        embed.set_footer(text=f"{botver} by PrincessLillie#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
                        embed.set_image(url=image)
                        await loading.edit(content='', embed=embed)
                except IndexError:
                    return await loading.edit(content=":x: No results found for your query. Check your spelling and try again.")

def setup(bot):
    bot.add_cog(NSFW(bot))
