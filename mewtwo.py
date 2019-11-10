import discord
from discord.ext import tasks, commands
import asyncio
import random
import traceback
import sys
import datetime
import mewtwo_config as config

print('Starting Mewtwo.py... This may take some time.')
print('')

bot = commands.Bot(command_prefix='>!', owner_id=config.owner, case_insensitive=True)
cogs = ["cogs.general", "cogs.fun", "cogs.nsfw", "cogs.other", "cogs.admin"]

start_time = datetime.datetime.utcnow()

botver = "Mewtwo v2.0"

botstatus =[
        'with >help',
        'Now in Python!',
        '#BringBackNationalDex!',
        'try >help!',
        'try >google!',
        'try >info!',
        'try >avatar!',
        'try >nslookup!',
        'try >sylveon!',
        'try >meloetta!',
        'in the Kanto region!',
        'in Cerulean Cave',
        'Pokémon Red',
        'Pokémon Green',
        'Pokémon Blue',
        'Pokémon Yellow',
        'with hugs! 🤗',
        'with Mew under the truck',
        'Silver is valid!',
        '#TeamTrees',
        'with Mega Evolution',
        'as Mega Mewtwo X',
        'as Mega Mewtwo Y',
        'outside of Galar',
]
        
@bot.event
async def on_ready():
    dev = bot.get_user(config.owner)
    for c in cogs:
        bot.load_extension(c)
    print('Mewtwo, rewritten in Python!')
    print('v2.0 by ' + dev.name + "#" + dev.discriminator + ' - Support: https://discord.gg/kDC9tW7')
    print('Logged into: ' + bot.user.name + "#" + bot.user.discriminator)
    print('------')

@tasks.loop(minutes=10.0)
async def change_status():
    playing = random.choice(botstatus)
    await bot.change_presence(activity=discord.Game(name=playing))

@change_status.before_loop
async def before_change_status():
    await bot.wait_until_ready()

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(":wave: Done! See ya!")
    await bot.logout()

@bot.command()
@commands.is_owner()
async def reload(ctx):
    for c in cogs:
        bot.unload_extension(c)
        bot.load_extension(c)
    await ctx.send(":white_check_mark: Successfully reloaded all cogs!")

@bot.command(aliases=["say"])
@commands.cooldown(5, 5, commands.BucketType.user)
async def echo(ctx, *, arg):
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
        await ctx.message.delete()
        await ctx.send(arg)

@bot.command()
async def info(ctx):
    dev = bot.get_user(config.owner)
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    embed = discord.Embed(title=botver, description="A bot by " + dev.name + "#" + dev.discriminator+ ". It's not much at the moment, but I aim to make it something better in the future.", color=0x8253c3)
    embed.add_field(name="Made by:", value=dev.name + "#" + dev.discriminator)
    embed.add_field(name="This bot is currently in:", value=f"{len(bot.guilds)} server(s)")
    embed.add_field(name="Invite:", value="Want to invite me to your server? [You can do so here!](https://discordapp.com/oauth2/authorize?client_id=442154636028280843&scope=bot&permissions=8) \nDon't want to give me administrator permissions? Use [this invite link](https://discordapp.com/oauth2/authorize?client_id=442154636028280843&scope=bot&permissions=388160) instead. (You may need to manually edit my permissions if new features are added though...)")
    embed.add_field(name="Source Code:", value="You can view Mewtwo's source code on [GitHub](https://github.com/sks316/mewtwo-bot)!")
    embed.add_field(name="Uptime:", value="Mewtwo has been online for {}".format(uptime_stamp))
    embed.add_field(name="Support Server:", value="[Mewtwo Dev](https://discord.gg/kDC9tW7)")
    embed.set_footer(text=botver + " by sks316#2523", icon_url='https://sks316.s-ul.eu/bsHvTCLJ')
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)
        
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            err = await ctx.send(f':x: Sorry, **{ctx.command}** has been disabled.')
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.UserInputError):
            err = await ctx.send(f':x: Please provide a valid argument and try again. For example, **>{ctx.command} Mewtwo**.')
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.NotOwner):
            err = await ctx.send(f':x: Sorry, you are not permitted to use the command **{ctx.command}**.')
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.CommandOnCooldown):
            err = await ctx.send(":x: Sorry, you're being ratelimited for this command. Try again in **{:.2f}".format(error.retry_after) + "** seconds.")
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, discord.Forbidden):
            err = await ctx.send(f":x: I don't have sufficient permissions to do something. If you tried running **>help**, make sure your DMs are open. Otherwise, please have an administrator check my permissions.")
            await ctx.message.delete(delay=10)
            return await err.delete(delay=10)

        elif isinstance(error, commands.NSFWChannelRequired):
            err = await ctx.send(f":x: You'll, uh, have to run that one in an NSFW channel.")
            await ctx.message.delete(delay=5)
            return await err.delete(delay=5)

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                err = await ctx.author.send(f':x: Sorry, **{ctx.command}** can not be used in Private Messages.')
                await ctx.message.delete(delay=5)
                return await err.delete(delay=5)
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                err = await ctx.send(':x: I could not find that member. Please try again.')
                await ctx.message.delete(delay=5)
                return await err.delete(delay=5)
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        err = await ctx.send(':x: Sorry, an unknown error occurred. Please use **>bug** to submit a bug report. Make sure you provide as many details as possible. \nYou can also join Mewtwo Dev to submit bug reports. **>info** contains an invite.')
        await ctx.message.delete(delay=10)
        await err.delete(delay=10)

change_status.start()
bot.run(config.token)
