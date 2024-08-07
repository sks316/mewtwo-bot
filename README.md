# [Mewtwo Bot](https://mewtwo-bot.carrd.co)
[![server-badge][]][server] [![invite-badge][]][invite] [![secondary-invite-badge][]][secondary-invite]

[![love-badge][]][love] [![nextcord-badge][]][nextcord]

Welcome to the repo for Mewtwo, my little bot written under Nextcord. This is still a HEAVY WIP, expect messy code. Please feel free to help out by opening a pull request.

# How to run the bot
Some of the custom emojis won't work unless manually replaced.
## Installing dependencies
First of all, ensure that you have Python installed.

Move to the project directory and install dependencies with pip:
```
pip install -r requirements.txt
```
This will install (hopefully) everything Mewtwo needs to run.
## Config file
Mewtwo needs to store some things, like API tokens, in a config file.

Go to the directory containing `mewtwo.py` then make a new file called `mewtwo_config.py`. This will be our config file.
Next (hopefully you've already done this), go to the [Discord Developer Portal](https://discordapp.com/developers/applications/) and create an application. Once done, go to `Bot` and hit the `Add Bot` button. Once done, you should be able to get your token! **DO NOT SHARE THIS WITH ANYONE, IT WILL GIVE FULL ACCESS TO YOUR BOT.**

You'll also want to enable the Presence Intent, the Server Members Intent, and the Message Content Intent.

Now open `mewtwo_config.py` in your favorite text editor and paste the following:
```
token = 'YOUR-TOKEN-HERE'
google_api_key = 'YOUR-API-KEY-HERE'
google_search_engine = 'YOUR-SEARCH-ENGINE-HERE'
owner = YOUR-USER-ID-HERE
```
Replace `YOUR-TOKEN-HERE` with your bot's token and `YOUR-USER-ID-HERE` with ***your*** User ID, not your bot's. If you want to use the Google and YouTube functions, you'll have to get and add a Google API key and a Google Custom Search ID. There are numerous tutorials online for this.
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

[love]: https://lillie2523.carrd.co
[love-badge]: https://custom-icon-badges.herokuapp.com/badge/-Made%20with%20love...-555555?style=for-the-badge&logo=heart

[nextcord]: https://github.com/nextcord/nextcord
[nextcord-badge]: https://custom-icon-badges.herokuapp.com/badge/-...and%20Nextcord-555555?style=for-the-badge&logo=nextcord
