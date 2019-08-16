import discord
from discord.ext import commands
import os

botver = "Mewtwo v2.0"

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def adminhelp(self, ctx):
        embed = discord.Embed(title=botver, description="Administrator commands for Mewtwo. \n The command prefix is `>`. To run a command, you must begin a message with `>`.", color=0x8253c3)
        embed.add_field(name="Commands:", value="**>shutdown** - Shuts down the bot. Aliases: **>logout** \n**>changestatus** - Changes the bot's Playing status. \n**>reload** - Reloads all cogs.\n**>serverlist** - Outputs a list of servers the bot is in to the terminal. \n**>clearterm** - Clears the terminal.", inline=False)
        embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("✅")

    @commands.command()
    @commands.is_owner()
    async def changestatus(self, ctx, *, arg):
        await bot.change_presence(activity=discord.Game(name=arg))
        await ctx.send(":ok_hand: Done.")

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def clearterm(self, ctx):
        os.system('clear')
        print('Mewtwo, rewritten in Python!')
        print('v2.0 by sks316#2523 - Support: https://discord.gg/kDC9tW7')
        print('Logged into: ' + self.bot.user.name + "#" + self.bot.user.discriminator)
        print('------')
        await ctx.send("✅ Done! Check your console!")

    @commands.command()
    @commands.is_owner()
    async def announce(self, ctx):
        embed = discord.Embed(description="I have a small update on the above situation. I've been able to secure hosting for Mewtwo!\nSomeone (I won't say who to protect their privacy) has graciously volunteered to provide hosting for the bot over the next few months! Hopefully uptime won't be as sporadic and we'll experience fewer slowdowns now. You may already notice that some commands such as `>r34` and `>google` are much faster. Once these few months are over I'll have to find another place to host the bot, but let's not worry about that. Let's just enjoy what we have now!\n\nOnce again, thank you for your continued interest in Mewtwo!", color=0x8253c3)
        embed.set_author(name=botver + " Announcement", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
        embed.set_footer(text="Announced by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by sks316#2523", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def serverlist(self, ctx):
        print('------')
        print('A list of servers was requested.')
        print('Connected to:')
        async for guild in self.bot.fetch_guilds(limit=150):
            print(guild.name)
        print('------')
        await ctx.send("✅ Done! Check your console!")

def setup(bot):
    bot.add_cog(Admin(bot))