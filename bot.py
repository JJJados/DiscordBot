# Work with Python 3.6
import discord
from discord.ext import commands
import localtoken
import praw
import random

TOKEN = localtoken.LOCALTOKEN

bot = commands.Bot(command_prefix='$')
reddit = praw.Reddit(client_id=localtoken.CLIENTID, client_secret=localtoken.CLIENTSECRET, user_agent=localtoken.USERAGENT)

@bot.command()
async def greet(ctx):
    
    msg = 'Hello {0.author.mention}! :wave:'.format(ctx)
    await ctx.send(msg)

@bot.command()
async def math(ctx, a: int, arg, b: int):

    if (arg == '*'):
        await ctx.send(a * b)
    elif (arg == '+'):
        await ctx.send(a + b)
    elif (arg == '-'):
        await ctx.send(a - b)
    elif (arg == '/'):
        await ctx.send(a // b)
    else:
        await ctx.send("Sorry {0.author.mention}, that command isn't something I can do!".format(ctx))

@bot.command()
async def codehumor(ctx):
    memes = reddit.subreddit('ProgrammerHumor').hot()
    post = random.randint(1, 50)

    for x in range(0, post):
        submission = next(x for x in memes if not x.stickied)

    await ctx.send(submission.url)
    
@bot.event
async def on_ready(ctx):
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)