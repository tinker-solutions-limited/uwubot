#! /usr/bin/python3

import os

from discord.ext import commands
from dotenv import load_dotenv

import uwulib

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', help="I am the bot of puwe cancew uwu")

@bot.command(name='hello', help=uwulib.uwu("Responds to a user!"))
async def hello_uwu(ctx):
    hello = uwulib.uwu(f'Hello {ctx.author.mention}!')
    await ctx.send(hello)

@bot.command(name="uwu", help=uwulib.uwu("Coming soon! ;)"))
async def uwuify(ctx, usr):
    # find usr's last message
        # kind of a challenge because there are a few different ways a
        # user can be referred (mention, whole user, partial user)
    # uwuify it
    # post it
    # hash the message and add to list so we can check if it's already been uwu'd
    # don't uwu uwubot's own messages - respond with "nyo u"
    await ctx.send(uwulib.uwu("nothing to uwu!"))

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()


