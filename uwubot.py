#! /usr/bin/python3

import os

from discord.ext import commands
from dotenv import load_dotenv

import uwulib

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', help="I am the bot of puwe cancew uwu")



# Bot Commands

@bot.command(name='hello', help=uwulib.uwu("Responds to a user!"))
async def hello_uwu(ctx):
    hello = uwulib.uwu(f'Hello {ctx.author.mention}!')
    await ctx.send(hello)

@bot.command(name="uwu", help=uwulib.uwu("Coming soon! ;)"))
async def uwuify(ctx, user):
    # find user's last message
        # kind of a challenge because there are a few different ways a
        # user can be referred (mention, whole user, partial user)
    # uwuify it
    # post it
    # hash the message and add to list so we can check if it's already been uwu'd
    # don't uwu uwubot's own messages - respond with "nyo u"
    await ctx.send(uwulib.uwu("nothing to uwu!"))

# Bot Event Responses

@bot.event
async def on_ready():
    print(uwulib.uwu(f'{bot.user.name} has connected to Discord!'))

@bot.event
async def on_message(message):
    if 'linux' in message.content:
        await message.channel.send(combative_linux_guy)
    await bot.process_commands(message)

# Internal Functions
    
combative_linux_guy = 'I\'d just like to interject for a moment. What you\'re referring to as Linux, is in fact, GNU/Linux, ' \
            'or as I\'ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, ' \
            'but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, ' \
            'shell utilities and vital system components comprising a full OS as defined by POSIX.\n\n' \
            'Many computer users run a modified version of the GNU system every day, without realizing it. Through a '\
            'peculiar turn of events, the version of GNU which is widely used today is often called "Linux", and many '\
            'of its users are not aware that it is basically the GNU system, developed by the GNU Project.\n\n'\
            'There really is a Linux, and these people are using it, but it is just a part of the system they use. '\
            'Linux is the kernel: the program in the system that allocates the machine\'s resources to the other programs '\
            'that you run. The kernel is an essential part of an operating system, but useless by itself; it can only '\
            'function in the context of a complete operating system. Linux is normally used in combination with the GNU '\
            'operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called "Linux" '\
            'distributions are really distributions of GNU/Linux.' 


def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()


