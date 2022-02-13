# [Mewtwo Bot](https://mewtwo-bot.carrd.co)
[![server-badge][]][server] [![invite-badge][]][invite] [![secondary-invite-badge][]][secondary-invite]

Oh hello. Welcome to the repo for Mewtwo, my little bot written under Nextcord. This is still a HEAVY WIP, expect some heckin' messy code. Open a PR if you wanna fix some of the places that I inevitably fucked up in.

# How to run the bot
Oh... I didn't expect that. You actually wanna run it, huh? Some emojis won't work, but that's fine I guess...
## Cloning the repo
Just do a good ol `git clone` like so:
```
git clone https://github.com/sks316/mewtwo-bot.git
```
## Installing dependencies
First of all, make sure you've got Python installed. If you don't, what the hell are you even doing here install Python first you idiot

Once you've installed Python or if you already had it installed like a good human, cd into the cloned directory and run the following:
```
pip install -r requirements.txt
```
This will install (hopefully) everything Mewtwo needs to run ~~(i still have no idea why you want to self-host this piece of shit)~~
## Config file
So we kinda sorta actually need to set up a config file first

Go to the directory containing `mewtwo.py` then make a new file called `mewtwo_config.py`. This will be our config file.
Next (hopefully you've already done this), go to the [Discord Developer Portal](https://discordapp.com/developers/applications/) and create an application. Once done, go to `Bot` and hit the `Add Bot` button. Once done, you should be able to get your token! **DO NOT SHARE THIS WITH ANYONE, IT WILL GIVE FULL ACCESS TO YOUR BOT.**

You'll also want to enable both the Presence Intent and Server Members Intent.

Now open `mewtwo_config.py` in your favorite text editor and paste the following:
```
token = 'YOUR-TOKEN-HERE'
google_api_key = 'YOUR-API-KEY-HERE'
google_search_engine = 'YOUR-SEARCH-ENGINE-HERE'
owner = YOUR-USER-ID-HERE
```
Replace `YOUR-TOKEN-HERE` with your bot's token and `YOUR-USER-ID-HERE` with ***your*** User ID, not your bot's. If you want to use the Google and YouTube functions, you'll have to get and add a Google API key and a Google Custom Search ID. There are numerous tutorials online for this, I won't bother typing it here since this thing is already too fucking long
## Running the bot
Finally, we run the bot. cd into the directory you cloned the repo to and run:
```
py mewtwo.py
```
Or, if you're using Linux:
```
python3 mewtwo.py
```


[server]: https://discord.gg/kDC9tW7
[server-badge]: https://img.shields.io/discord/444344089878724619.svg?style=for-the-badge&logo=discord&colorB=7289DA

[invite]: https://discordapp.com/oauth2/authorize?client_id=442154636028280843&scope=bot&permissions=8&redirect_uri=https%3A%2F%2Fsks316.github.io%2Fmewtwo%2Fthanks&response_type=code&prompt=none
[invite-badge]: https://img.shields.io/badge/invite%20mewtwo-click%20here-black.svg?style=for-the-badge&colorB=8253C3

[secondary-invite]: https://discordapp.com/oauth2/authorize?client_id=442154636028280843&scope=bot&permissions=388160&redirect_uri=https%3A%2F%2Fsks316.github.io%2Fmewtwo%2Fthanks&response_type=code&prompt=none
[secondary-invite-badge]: https://img.shields.io/badge/or%20use%20this%20invite-click%20here-black.svg?style=for-the-badge&colorB=8253C3
